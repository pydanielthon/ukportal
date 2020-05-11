from django.shortcuts import render
from .models import RandkaDetail, KategoriaRandki, Comment
from .forms import CommentForm, DodajForm
from django.shortcuts import get_object_or_404
from katalog.models import katalog
# Create your views here.
def glowna(request):
    kategorie = KategoriaRandki.objects.all()
    posty = katalog.objects.filter(premium = True)
    context = {
        'kategorie': kategorie,
        'posty': posty
    }
    return render(request, 'randki/glowna.html', context)

def kategoria(request, pk):
    kategoriaa = get_object_or_404(KategoriaRandki, pk=pk)
    ogl = kategoriaa.ogloszenie.all()

    context =  {'kategoriaa': kategoriaa,
                'ogl': ogl}
    return render(request, 'randki/kategoria.html', context)

def detail(request, pk):
    ogloszenie = get_object_or_404(RandkaDetail, pk=pk)
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
                                           'ogloszenie': ogloszenie}
 
    return render(request, 'randki/detail.html', context)
def dodaj(request):
    form = DodajForm(request.POST)   
    if form.is_valid():
        ogloszenie = form.save(commit=False)
        ogloszenie.save() 
    else:
        ogloszenie = DodajForm()
    context = {
                'form': form,}
    return render(request, 'randki/dodaj.html', context)