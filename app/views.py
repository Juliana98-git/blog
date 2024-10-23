from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def Noticias(request):
    return render(request, 'app/noticias.html')

def Perfil(request):
    return render(request, 'app/perfil.html')

def Peliculas(request):
    return render(request, 'app/peliculas.html')

def Iniciar_sesion(request):
    return render(request, 'app/inicio_sesion.html')