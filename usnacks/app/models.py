from django.db import models

class MetodosDePago(models.Model):
    name = models.CharField(max_length = 30)

class Vendedor(models.Model):
    title = models.CharField(max_length=10)
    username = models.CharField(max_length=60)
    password= models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    pago = models.ManyToManyField(MetodosDePago)
    foto= models.ImageField('Foto de perfil')
    horarioApertura = models.TimeField('Horario de apertura', null=True)
    horarioCierre = models.TimeField('Horario de cierre', null=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.username

class Alumno(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Producto(models.Model):
    title = models.CharField(max_length=10)
    nombre= models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    foto = models.ImageField('Foto de producto')
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=60)
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
