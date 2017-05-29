from django.db import models

class User(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    foto = models.ImageField('Foto de perfil')

class MetodosDePago(models.Model):
    name = models.CharField(max_length = 30)

class Categoria(models.Model):
    name = models.CharField(max_length = 30)

class Localizacion(models.Model):
    posx = models.FloatField()
    posy = models.FloatField()

class Horario(models.Model):
    apertura = models.TimeField('apertura')
    cierre = models.TimeField('cierre')

class Vendedor(models.Model):
    title = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pago = models.ManyToManyField(MetodosDePago)
    activo = models.BooleanField()
    horario = models.OneToOneField(Horario, on_delete=models.CASCADE)
    localizacion = models.OneToOneField(Localizacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Producto(models.Model):
    title = models.CharField(max_length=10)
    nombre= models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    foto = models.ImageField('Foto de producto')
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ManyToManyField(Categoria)
    vendedorId = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

class Favoritos(models.Model):
    alumnoId = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    vendedorId = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

class Historial(models.Model):
    ProductoId = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.TimeField('fecha')
    Hstock = models.IntegerField()


"""
v=Vendedor(tipo="ambulante",username="El Chino", password="clavechino",activo="True",
           foto="../static/img/chinoavatar.jpg", pago="efectivo", title="chino")
v.save()

v=Vendedor(tipo="ambulante",username="Tia de los alfajores", password="clavetia",activo="True",
           foto="../static/img/grandma.jpg", pago="efectivo", title="alfajores")
v.save()
v=Vendedor(tipo="ambulante",username="Denis", password="clavetia",activo="True",
           foto="../static/img/grandma.jpg", pago="efectivo", title="denis")
v.save()

v=Vendedor(tipo="fijo",username="Sonia", password="clavesonia",activo="True",
           foto="../static/img/sonia.jpg", pago="efectivo", title="sonia", horarioApertura='8:00', horarioCierre='6:00')
v.save()
"""

""""
c1 = Categoria(name = "Efectivo")
c2 = Categoria(name = "Debito")
c3 = Categoria(name = "Junaeb")
c1.save()
c2.save()
c3.save()

h1 = Horario(apertura = "10.30", cierre = "19.00")

L1 = Localizacion(posx = 10.234, posy = 12.4532)
L2 = Localizacion(posx = 14.234, posy = 11.4532)
L1.save()
L2.save()

u1 = User(username = "Chino", password = "chino", tipo = "ambulante", foto="../static/img/chinoavatar.jpg")
u1.save()
u2 = User(username = "Alfajores", password = "alfajores", tipo = "fijo", foto="../static/img/grandma.jpg")
u2.save()

v1 = Vendedor(title = "chino", user = User.objects.get(id=1), pago = MetodosDePago.objects.get(id=1), activo = True,
             localizacion = Localizacion.objects.get(id=1))
v2 = Vendedor(title = "tia", user = User.objects.get(id=2), pago = MetodosDePago.objects.get(id=2),
              horario = Horario.objects.get(id=2), localizacion = Localizacion.objects.get(id=2))
"""