from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
import requests
import json
from store.models import Nonft
# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have successfully registered!'))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have successfully logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Invalid login information.'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have successfully logged out.'))
    return redirect('login')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have successfully updated your profile information!'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have successfully changed your password!'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)



def home(request):
    # Gets Price Data From CryptoCompare
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,ADA&tsyms=USD")
    price = json.loads(price_request.content)

    # Gets ALL News From CryptoCompare
    btc_news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?categories=BTC,ETH,ADA/?lang=EN")
    btc_news = json.loads(btc_news_request.content)
    return render(request, 'crypto/home.html', {'btc_news': btc_news, 'price': price})

def prices(request):
    if request.method == "POST":
        quote = request.POST['quote']
        quote = quote.upper()
        searched_price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=USD")
        searched_price = json.loads(searched_price_request.content)
        return render(request, 'crypto/prices.html', {'quote': quote, 'searched_price': searched_price})
    else:
        not_valid_ticker = "Please enter a valid ticker. Examples: 'BTC', 'ada'..." 
        return render(request, 'crypto/prices.html', {'not_valid_ticker': not_valid_ticker})

def all_nft(request):
    nonfts = Nonft.objects.all().filter(is_available = True)
    context = {
        'nonfts': nonfts
    }
    return render(request, 'crypto/all_nft.html', context)

