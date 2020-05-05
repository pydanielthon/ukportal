from django.db import models
from django.utils import timezone
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField
class Porady(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    www = models.CharField(max_length=400, blank=True, null=True)
    image = models.ImageField(upload_to='media/porady', default='static/img/backgrounds/img-2.jpg')

    image_790x160 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(790, 160)],
        format='JPEG',
        options={'quality': 85}
    )
 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class PoradyVideo(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    film = models.CharField(max_length=700)
    zdjecie = models.ImageField(upload_to='media', default='static/assets/img/backgrounds/img-2.jpg')

    def __str__(self):
        return self.title