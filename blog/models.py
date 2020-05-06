from django.db import models
from django.utils import timezone


class Post(models.Model):
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

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)