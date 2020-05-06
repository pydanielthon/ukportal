from django.db import models
from django.utils import timezone
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField
class Porady(models.Model):
    title1 = models.CharField(max_length=500, default="")
    text1 = models.TextField()
    imgglowne = models.ImageField(upload_to='media', default='static/img/backgrounds/img-2.jpg')

    title2 = models.CharField(blank=True, null=True, max_length=500)
    text2 = models.TextField(blank=True, null=True, default="")
    img2 = models.ImageField(upload_to='media', blank=True, null=True)

    title3 = models.CharField(blank=True, null=True, max_length=500)
    text3 = models.TextField(blank=True, null=True, default="")
    img3 = models.ImageField(upload_to='media', blank=True, null=True)

    title4 = models.CharField(blank=True, null=True, max_length=500)
    text4 = models.TextField(blank=True, null=True, default="")

    autor = models.CharField(max_length=150, default="")

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title1


class PoradyVideo(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    film = models.CharField(max_length=700)
    zdjecie = models.ImageField(upload_to='media', default='static/assets/img/backgrounds/img-2.jpg')

    def __str__(self):
        return self.title