from django.db import models

# Create your models here.
class KategoriaRandki(models.Model):

    nazwa = models.CharField(max_length=250)
    def __str__(self):
        return self.nazwa
class RandkaDetail(models.Model):
    men = "Mężczyzna"
    women = 'Kobieta'
    ono = 'Inna'

    PLEC_CHOICES= [
        (men, 'Mężczyzna'),
        (women, 'Kobieta'),
        (ono, 'Inna')
    ]
    plec = models.CharField(
        max_length=30,
        choices=PLEC_CHOICES,
        default=men,
    )
    miasto = models.CharField(max_length=40, default="")
    kategoria = models.ForeignKey(KategoriaRandki, 
                                    related_name='ogloszenie',
                                    on_delete=models.CASCADE,
                                    default=None)
    tytul = models.CharField(max_length=700)
    opis = models.TextField()
    img = models.ImageField(upload_to='media', default='static/assetss/img/backgrounds/img-2.jpg', blank=True, null=True)

    def __str__(self):
        return self.tytul



class Comment(models.Model):
    ogloszenie = models.ForeignKey(RandkaDetail,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

