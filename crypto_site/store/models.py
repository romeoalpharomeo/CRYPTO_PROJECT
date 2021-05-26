from django.db import models
from category.models import Category
# Create your models here.

class Nonft(models.Model):
    nonft_name = models.CharField(max_length = 280, unique = True)
    slug = models.SlugField(max_length = 280, unique = True)
    nonft_description = models.TextField(max_length = 500, blank = True)
    price = models.IntegerField()
    images = models.ImageField(upload_to = 'photos/products')
    quantity = models.IntegerField()
    is_available = models.BooleanField(default = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nonft_name
