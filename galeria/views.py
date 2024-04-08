from django.shortcuts import render



def fotos(request):
    return render(request, 'galeria/fotos.html')

def videos(request):
    return render(request, 'galeria/videos.html')

def planos(request):
    return render(request, 'galeria/planos.html')
# Create your views here.
def galeria_fotos(request):
    return render(request, 'galeria/fotos.html')

