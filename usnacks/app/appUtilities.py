import datetime
from django.contrib.auth.models import User
from usnacks.app.models import MetodosDePago, Vendedor, Alumno, Producto, Favoritos, Historial


def add_alumno(data):
    user = Alumno(username = data['username'], password = data['password'])
    user.save()

def add_vendedor(data):
    if (data['tipo'] == 'ambulante'):
        vendedor = Vendedor(title = data['title'], username = data['username'], password = data['password'],
                            tipo = data['tipo'], foto = data['foto'], activo = data['activo'])
    else:
        vendedor = Vendedor(title = data['title'], username = data['username'], password = data['password'],
                            tipo = data['tipo'], foto = data['foto'], horarioApertura = data['horarioApertura'],
                            horarioCierre = data['horarioCierrre'])
    for pago in data['pago']:
        vendedor.pago.add(MetodosDePago.object.get(name = pago))
    vendedor.save()

def login(data):
    user = Blog.objects.get(id=14)
