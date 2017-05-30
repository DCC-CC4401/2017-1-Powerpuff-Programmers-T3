from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from models import *
from forms import *

#1. Interfaz de busqueda de vendedores
#2. Ficha de vendedor (vista por un alumno)
#3. Ficha de vendedor (vista por un vendedor)
#4. Ficha de producto

def busqueda(request):
    return render(request, 'app/landing-page.html')

def busquedalogeado(request):
    return render(request, 'app/landing-page-logeado.html')

#index y login puestos porq sino me tira error
def index(request):
    return render(request, 'app/base.html', user)

def login(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            u = User.objects.filter(username=username).first()
            if u.password == password:
                context = {
                    'user': u
                }
                return HttpResponseRedirect(reverse('busquedalogeado'))
            else:
                context = {
                    'error': "Usuario o contrasena incorrecta",
                    'form': form
                }
                return render(request, 'app/login.html', context)
    else:
        form = LogIn

        return render(request, 'app/login.html', {'form': form})

def vendedor(request, vendedor_id):
    context={
        'vendedor': Vendedor.objects.filter(title=vendedor_id)[0],
        'productos': Producto.objects.filter(vendedorId__title=vendedor_id)
    }
    return render(request, 'app/vendedor-profile-page.html',context)

def Vistavendedor(request, vendedor_id, usuario_id):
    context={
        'vendedor': Vendedor.objects.filter(title=vendedor_id)[0],
        'usuario': User.objects.filter(username=usuario_id)[0],
        'productos': Producto.objects.filter(vendedorId__title=vendedor_id)
    }
    return render(request, 'app/vendedor-profile-page.html',context)

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            tipo = form.cleaned_data.get('tipo')
            # do something with your results
            u = User(username = username, password = password, tipo = tipo)
            u.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignUp

    return render(request, 'app/signup.html', {'form': form})
    
def producto(request,producto_id):
    return render(request, 'app/gestion-productos.html')
    #return HttpResponse("Estas viendo el producto %s " % producto_id)

def create_user(request, post):
    return HttpResponse("Estas viendo el producto %s " % post)

