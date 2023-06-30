from django.shortcuts import render
# Create your views here.
def Index(request):
    return render(request,'Index.html')

def Deporte(request):
    return render(request,'Deporte.html')

def Policial(request):
    return render(request,'Policial.html')

def Tendencia(request):
    return render(request,'Tendencia.html')

def Nacional(request):
    return render(request,'Nacional.html')

def Login(request):
    return render(request,'Login.html')

def Contacto(request):
    return render(request,'Contacto.html')