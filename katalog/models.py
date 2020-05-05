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
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='katalog/%Y/%m/%d',
                                blank=True)
    adres = models.CharField(max_length=300, null=True)
    telefon = models.FloatField(blank=True, null=True)
    mail = models.EmailField(blank=True, null=True)
    www = models.CharField(max_length=150, blank=True, null=True)
    fb = models.CharField(max_length=250, blank=True, null=True)
    instagram = models.CharField(max_length=250, blank=True, null=True)
    maps = models.CharField(max_length=250, blank=True, null=True)

    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name

class darmowy(models.Model):
    kategoria = models.ForeignKey(Category,
                                related_name='darmowy',
                                on_delete=models.CASCADE,
                                )
    nazwa = models.CharField(max_length=250)
    email = models.EmailField()
    miasto = models.CharField(max_length=100)
    numer = models.FloatField()
    logo = models.ImageField(upload_to='katalog/%Y/%m/%d', blank=True, null=True)

class podstawowy(models.Model):
    kategoria = models.ForeignKey(Category,
                                related_name='podstawowy',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    nazwa = models.CharField(max_length=250)
    email = models.EmailField()
    miasto = models.CharField(max_length=100)
    numer = models.FloatField()
    logo = models.ImageField(upload_to='katalog/%Y/%m/%d', blank=True, null=True)
    www = models.CharField(max_length=400)
    fb = models.CharField(max_length=250, blank=True, null=True)
    instagram = models.CharField(max_length=250, blank=True, null=True)
    maps = models.CharField(max_length=250, blank=True, null=True)




    