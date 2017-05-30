from django.db import models

# Create your models here.
class Vendedor(models.Model):
    VEN_USERNAME = models.CharField(max_length = 255)
    VEN_PASSWORD = models.CharField(max_length = 255)
    VEN_TIPO = models.CharField(max_lenghth = 255)
    VEN_PAGO = models.CharField(max_length = 255)
    VEN_FOTO = models.ImageField('Foto de perfil')
    VEN_HORARIOA = models.TimeField('Horario de apertura')
    VEN_HORARIOC = models.TimeField('Horario de cierre')
    VEN_ACTIVO = models.BooleanField()

class Alumno(models.Model):
    ALU_USERNAME = models.CharField(max_length = 255)
    ALU_PASSWORD = models.CharField(max_length = 255)

class Producto(models.Model):
    PRO_NOMBRE = models.CharField(max_length = 255)
    PRO_DESCRIPCION = models.CharField(max_length = 255)
    PRO_FOTO = models.ImageField('Foto de producto')
    PRO_PRECIO = models.IntegerField()
    PRO_STOCK = models.IntegerField()
    PRO_CATEGORIA = models.CharField(max_length = 255)
    PRO_IDVENDEDOR = models.ForeignKey(Vendedor, on_delete = models.CASCADE)

class Favoritos(models.Model):
    FAV_IDALUMNO = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    FAV_IDVENDEDOR = models.ForeignKey(Vendedor, on_delete = models.CASCADE)

class Historial(models.Model):
    HIS_IDPRODUCTO = models.ForeignKey(Producto, on_delete = models.CASCADE)
    HIS_FECHA = models.TimeField('fecha')
    HIS_STOCK = models.IntegerField()
