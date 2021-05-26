# Generated by Django 3.2.3 on 2021-05-26 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nonft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nonft_name', models.CharField(max_length=280, unique=True)),
                ('slug', models.SlugField(max_length=280, unique=True)),
                ('nonft_description', models.TextField(blank=True, max_length=500)),
                ('price', models.IntegerField()),
                ('images', models.ImageField(upload_to='photos/products')),
                ('quantity', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]