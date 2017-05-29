from django.db import models

class Vendedor(models.Model):
    username = models.CharField(max_length=60)
    password= models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    pago = models.CharField(max_length=60)
    foto= models.ImageField('Foto de perfil')
    horarioApertura = models.TimeField('Horario de apertura', null=True)
    horarioCierre= models.TimeField('Horario de cierre', null=True)
    activo= models.BooleanField()

class Alumno(models.Model):
    username= models.CharField(max_length=20)
    password= models.CharField(max_length=20)

class Producto(models.Model):
    nombre= models.CharField(max_length=20)
    descripcion= models.CharField(max_length=200)
    foto= models.ImageField('Foto de producto')
    precio= models.IntegerField()
    stock= models.IntegerField()
    categoria= models.CharField(max_length=60)
    vendedorId= models.ForeignKey(Vendedor, on_delete=models.CASCADE)

class Favoritos(models.Model):
    alumnoId = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    vendedorId= models.ForeignKey(Vendedor, on_delete=models.CASCADE)

class Historial(models.Model):
    ProductoId= models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.TimeField('fecha')
    Hstock= models.IntegerField()

v=Vendedor(tipo="ambulante",username="chino", password="clavechino",activo="True",
           foto="../static/img/chinoavatar.jpg", pago="efectivo")
v.save()

v=Vendedor(tipo="ambulante",username="alfajores", password="clavechino",activo="True",
           foto="../static/img/alfajoresavatar.png", pago="efectivo")
v.save()
