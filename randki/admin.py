from django.contrib import admin

# Register your models here.
from .models import KategoriaRandki, Comment, RandkaDetail

admin.site.register(KategoriaRandki)
admin.site.register(Comment)
admin.site.register(RandkaDetail)

