from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Porady, PoradyVideo
from katalog.models import katalog
from blog.models import Post
def porady_list(request):
    posts = Porady.objects.all()
    najlepszy = Porady.objects.all()[:3]
    video = PoradyVideo.objects.all()[:3]
    firmy = katalog.objects.all()[:6]
    context = {
        'posts': posts,
        'najlepszy': najlepszy,
        'video': video,
        'firmy': firmy
    }
    return render(request, 'porady.html', context)

def porady_detail(request, pk):
    post = get_object_or_404(Porady, pk=pk)
    firmy = katalog.objects.all()[:4]
    posty = Post.objects.all()[:3]
    context =  {
        'post': post,
        'firmy': firmy,
        'posty': posty
        }
    return render(request, 'porady_detail.html', context)