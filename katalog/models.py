from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absoulte_url(self):
        return reverse('katalog:lista_kategorii', args=[self.slug])

    def __str__(self):
        return self.name

class katalog(models.Model):
    category = models.ForeignKey(Category,
                                related_name='katalog',
                                on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='katalog/%Y/%m/%d', null=True, blank=True)
    adres = models.CharField(max_length=300, null=True)
    telefon = models.FloatField(blank=True, null=True)
    mail = models.EmailField(blank=True, null=True)
    www = models.CharField(max_length=150, blank=True, null=True)
    fb = models.CharField(max_length=250, blank=True, null=True)
    instagram = models.CharField(max_length=250, blank=True, null=True)
    maps = models.CharField(max_length=250, blank=True, null=True)

    description = models.TextField(blank=True)
    premium = models.BooleanField(default=False)


    def __str__(self):
        return self.name





    