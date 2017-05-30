from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from forms import *
from appUtilities import *

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
    user = login_user()
    if user:
        return render(request, 'app/base.html', user)
        return render(request, 'app/base.html', user)

def login(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # do something with your results
            u = User.objects.all()
            return HttpResponse(str(u.first()))
    else:
        form = LogIn
<<<<<<< HEAD

    return render(request, 'app/login.html', {'form': form})

=======

    return render(request, 'app/login.html', {'form': form})
>>>>>>> 8f17b2b676281e229fe8676fbc75c6de47406b9d

def vendedor(request, vendedor_id):
    context={
        'vendedor': Vendedor.objects.filter(title=vendedor_id)[0]
    }
    return render(request, 'app/vendedor-profile-page.html',context)

def Vistavendedor(request, vendedor_id, usuario_id):
    context={
        'vendedor': Vendedor.objects.filter(title=vendedor_id)[0],
        'usuario': User.objects.filter(username=usuario_id)[0]
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
            return HttpResponse(username + password + tipo)
    else:
        form = SignUp

    return render(request, 'app/signup.html', {'form': form})

def producto(request,producto_id):
    return render(request, 'app/gestion-productos.html')
    #return HttpResponse("Estas viendo el producto %s " % producto_id)

def create_user(request, post):
<<<<<<< HEAD
return HttpResponse("Estas viendo el producto %s " % post)
=======
    return HttpResponse("Estas viendo el producto %s " % post)
>>>>>>> 8f17b2b676281e229fe8676fbc75c6de47406b9d
