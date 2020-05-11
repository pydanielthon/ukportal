from django.shortcuts import render
from porady.models import Porady
from blog.models import Post
from katalog.models import katalog
from porady.models import PoradyVideo
from django.views.generic import TemplateView, ListView
# Create your views here.
def homepage(request):
    porady = Porady.objects.all()[:2]
    wpisy = Post.objects.all()[:3]
    firmy = katalog.objects.filter(premium = True)
    wideo = PoradyVideo.objects.all()[:2]
    context = {
        'porady': porady,
        'wpisy': wpisy,
        'firmy': firmy,
        'wideo': wideo
    }
    return render(request, 'homepage.html', context)


def kup(request):

    context = {}

    return render(request, 'kup.html', context)

def profil(request):

    return render(request, 'konto.html')

def platnosc(request):

    context = {}

    return render(request, 'platnosc.html', context)


