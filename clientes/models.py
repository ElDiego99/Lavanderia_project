from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    tipo_servicio = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"
    
class Orden(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Completado', 'Completado'),
        ('Cancelado', 'Cancelado'),
    ]
    clinete = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    total = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Orden #{self.id} - {self.cliente.nombre}"
    
class OrdenServicio(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='orden_servicios')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.servicio.precio
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.cantidad} x {self.servicio.nombre} - Orden #{self.orden.id}"