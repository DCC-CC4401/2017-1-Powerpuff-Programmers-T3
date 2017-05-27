from django.http import HttpResponse

#1. Interfaz de busqueda de vendedores
#2. Ficha de vendedor (vista por un alumno)
#3. Ficha de vendedor (vista por un vendedor)
#4. Ficha de producto

def busqueda(request):
    return HttpResponse("Hello, world. You're at usnacks index.")

def vendedorPorVendedor(request, vendedor_id):
    return HttpResponse("ficha de vendedor %s vista por vendedor" % vendedor_id)

def vendedorPorAlumno(request, vendedor_id):
    return HttpResponse("ficha de vendedor %s vista por alumno" % vendedor_id)

def producto(request,producto_id):
    return HttpResponse("Estas viendo el producto %s " % producto_id)
