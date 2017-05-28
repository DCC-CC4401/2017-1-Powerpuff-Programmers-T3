from django.http import HttpResponse
from django.shortcuts import render

#1. Interfaz de busqueda de vendedores
#2. Ficha de vendedor (vista por un alumno)
#3. Ficha de vendedor (vista por un vendedor)
#4. Ficha de producto

def busqueda(request):
    return render(request, 'app/landing-page.html')

#index y login puestos porq sino me tira error
def index(request):
    return
def login(request):
    return

def vendedorPorVendedor(request, vendedor_id):
    return HttpResponse("ficha de vendedor %s vista por vendedor" % vendedor_id)

def vendedorPorAlumno(request, vendedor_id):
    return HttpResponse("ficha de vendedor %s vista por alumno" % vendedor_id)

def producto(request,producto_id):
    return HttpResponse("Estas viendo el producto %s " % producto_id)
