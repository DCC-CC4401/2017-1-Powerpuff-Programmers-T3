from django.db import models

class User(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    foto = models.ImageField('Foto de perfil')

    def __str__(self):
        return self.username

class MetodosDePago(models.Model):
    name = models.CharField(max_length = 30)

class Categoria(models.Model):
    name = models.CharField(max_length = 30)

class Localizacion(models.Model):
    posx = models.FloatField()
    posy = models.FloatField()

class Vendedor(models.Model):
    title = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pago = models.ManyToManyField(MetodosDePago)
    activo = models.BooleanField()
    hapertura = models.TimeField('Horario de apertura', null=True)
    hcierre = models.TimeField('Horario de cierre', null=True)
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

