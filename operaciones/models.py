from django.db import models
from comunidad.models import Tienda, Usuario



def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}-{instance.tienda.nombre}.{ext}"
    return f"operaciones/productos/{filename}"

# Create your models here.
class Pedido(models.Model):
    pass 
class Producto(models.Model):
    imagen = models.ImageField(upload_to=get_image_filename, blank=True, null=True,default="operaciones/productos/default-product.png")
    nombre= models.CharField(max_length=45,verbose_name="Nombre")
    precio= models.PositiveIntegerField(verbose_name="Precio")
    tienda= models.ForeignKey(Tienda, verbose_name="Tienda", on_delete=models.CASCADE)
    descripcion=models.TextField(verbose_name="Descripción")
    estado=models.BooleanField(default=True)
    
class Foto(models.Model):
    imagen = models.ImageField(upload_to=get_image_filename, blank=True, null=True, default=r"operaciones\fotos\default-Product.png")
    nombre= models.CharField(max_length=45,verbose_name="Nombre")
    tienda= models.ForeignKey(Tienda, verbose_name="Tienda", on_delete=models.CASCADE)
    descripcion=models.TextField(verbose_name="Descripción")
    estado=models.BooleanField(default=True)
    
    
class Cita(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f'Cita de {self.nombre} el {self.fecha} a las {self.hora}'
