from django.contrib import admin

# Register your models here.
from .models import OgloszenieDetail, OgloszeniaKategoria, Comment, Dodaj

admin.site.register(OgloszenieDetail)
admin.site.register(OgloszeniaKategoria)
admin.site.register(Comment)
admin.site.register(Dodaj)