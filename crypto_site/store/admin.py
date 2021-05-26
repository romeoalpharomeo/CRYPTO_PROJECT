from django.contrib import admin
from .models import Nonft
# Register your models here.
class NonftAdmin(admin.ModelAdmin):
    list_display = ('nonft_name', 'price', 'quantity', 'category', 'modified_date','is_available',)
    prepopulated_fields = {'slug': ('nonft_name',)}


admin.site.register(Nonft, NonftAdmin)
