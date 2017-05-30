import datetime
from django.contrib.auth.models import User
from app.models import MetodosDePago, Vendedor, Alumno, Producto, Favoritos, Historial, Localizacion

## hago de la localizacion un objeto
def loca(localizacion):
    x = localizacion.pop()
    y = localizacion.pop()
    return Localizacion(posx = x , posy = y)

##retornar los metodos de pago
def pagos(pagos):
    l = []
    for p in pagos:
        l.add(MetodosDePago.objects.get(name = p))
    return l

##crear un alumno nuevo
def add_alumno(data):
    user = User(username = data['username'], password = data['password'], tipo = data['tipo'], foto = data['foto'])
    user.save()
    alumno = Alumno(user = user)
    alumno.save()
    return alumno

def add_vendedor(data):
    user = User(username=data['username'], password=data['password'], tipo=data['tipo'], foto=data['foto'])
    user.save()
    if (data['tipo'] == 'ambulante'):
        vendedor = Vendedor(title = data['title'], user = user, activo = data['activo'], hapertura = data['apertura'],
    hcierre = data['cierre'], localizacion = loca(data['localizacion']))
    else:
        vendedor = Vendedor(title = data['title'], username = data['username'], password = data['password'],
                            tipo = data['tipo'], foto = data['foto'], horarioApertura = data['horarioApertura'],
                            horarioCierre = data['horarioCierrre'])
    for pago in data['pago']:
        vendedor.pago.add(MetodosDePago.object.get(name = pago))
    vendedor.save()
    return vendedor

## verifico si es el usuario y si esta bien retorno el usuario para buscar si es vendedor o alumno y si no falso
def login_user(user, password):
    u = User.objects.filter(username = user).first()
    if u.password == password:
        return True
    return False

##listo creo
def edit_vendedor(data):

    user = User.objects.get(username=data['id'])
    if user.tipo == 'ambulante' or user.tipo == 'fijo':
        vendedor = Vendedor.objects.get(user = user)
        vendedor.user.username = data['username']
        vendedor.user.password = data['password']
        vendedor.user.foto = data['foto']
        for p in data['pago']:
            vendedor.pago.add(MetodosDePago.objects.get(name=p))
        vendedor.horario = data['horario']
        vendedor.localizacion = loca(data['localizacion'])
        vendedor.save()
    else:
        alumno = Alumno.objects.get(user = user)
        alumno.user.username = data['username']
        alumno.user.password = data['password']
        alumno.user.foto = data['foto']
        alumno.save()
