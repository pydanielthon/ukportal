from django.contrib import admin

# Register your models here.
from .models import Porady, PoradyVideo

admin.site.register(Porady)
admin.site.register(PoradyVideo)