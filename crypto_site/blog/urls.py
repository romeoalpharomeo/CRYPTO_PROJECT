from django.urls import path
from . import views

urlpatterns = [
    path("all_posts/", views.all_posts, name="all_posts"),
    path("single_post/<slug:slug>", views.single_post, name="single_post") #slug can be a unique append to an url
]