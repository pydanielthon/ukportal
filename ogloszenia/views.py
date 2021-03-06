from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import OgloszeniaKategoria, OgloszenieDetail, Dodaj
from katalog.models import katalog
from .forms import CommentForm, DodajForm
from blog.models import Post
def after(request):
    posty = katalog.objects.filter(premium = True)
    context = {
        'posty': posty
        }

    return render(request, 'after.html', context)
def glowna(request):
    kategorie = OgloszeniaKategoria.objects.all()
    posty = katalog.objects.filter(premium = True)
    context = {
        'kategorie': kategorie,
        'posty': posty,
    }
    return render(request, 'glowna.html', context)

def kategoria(request, pk):
    kategoriaa = get_object_or_404(OgloszeniaKategoria, pk=pk)
    ogl = kategoriaa.ogloszenie.all()
    posty = katalog.objects.all()[:4]
    context =  {'kategoriaa': kategoriaa,
                'ogl': ogl,
                'posty': posty}
    return render(request, 'kategoria.html', context)

def detail(request, pk):
    ogloszenie = get_object_or_404(OgloszenieDetail, pk=pk)
    wpisy = Post.objects.all()[:3]
    comments = ogloszenie.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.ogloszenie = ogloszenie
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'ogloszenie': ogloszenie,
                                           'wpisy': wpisy}
 
    return render(request, 'detail.html', context)
def dodaj(request):
    form = DodajForm(request.POST)   
    if form.is_valid():
        ogloszenie = form.save(commit=False)
        ogloszenie.save()
        return redirect('ogloszenia:after') 
    else:
        ogloszenie = DodajForm()
    context = {
                'form': form,}
    return render(request, 'dodaj.html', context)


