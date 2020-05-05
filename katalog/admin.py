from django.contrib import admin
from .models import Category, katalog, darmowy, podstawowy

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    admin.site.register(Category)

class katalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    admin.site.register(katalog)
    admin.site.register(darmowy)
    admin.site.register(podstawowy)