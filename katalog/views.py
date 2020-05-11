from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import katalog, Category
from porady.models import PoradyVideo
from .forms import DodajFirme, SearchForm
def after(request):
    posty = katalog.objects.filter(premium = True)

    context = {
        'posty': posty,
    }
    return render(request, 'after.html', context)
def katalog_list(request):
    katalogs = katalog.objects.order_by('category')
    kategoria = Category.objects.all()
    porady = PoradyVideo.objects.all()[:2]
    firmy = katalog.objects.all()
    context = {
        'katalogs': katalogs,
        'kategoria': kategoria,
        'firmy': firmy,
        'porady': porady,
    }
    return render(request, 'katalog.html', context)

def firma_detail(request, pk):
    katalogg = get_object_or_404(katalog, pk=pk)
    posty = katalog.objects.filter(premium = True)

    context = {
        'katalogg': katalogg,
        'posty': posty        
                }
    return render(request, 'firma.html', context)

def dodajfirme(request):
    form = DodajFirme(request.POST)   
    if form.is_valid():
        firma = form.save(commit=False)
        firma.save() 
        return redirect('katalog:after') 

    else:
        firma = DodajFirme()
    context = {
                'form': form,}
    return render(request, 'dodajfirme.html', context)

def kategoria(request, pk):
    kategoriaa = get_object_or_404(Category, pk=pk)
    ogl = kategoriaa.katalog.all()
    posty = katalog.objects.filter(premium = True)
    ogl2 = katalog.objects.all()
    form = SearchForm(request.GET)

    #Odbieranie instacnji get
    name = request.GET.get('name', False)
    if name:
        posty = posty.filter(name__icontains=name) 

    context =  {'kategoriaa': kategoriaa,
                'ogl': ogl,
                'posty': posty,
                'ogl2': ogl2,
                'form': form,


}
    return render(request, 'kategorie.html', context)

