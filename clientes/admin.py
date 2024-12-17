from django.contrib import admin

# Register your models here.
from .models import Cliente, Servicio,Orden

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_servicio', 'precio', 'descripcion')
    search_fields = ('tipo_servicio',)
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'telefono')
    search_fields = ('nombre', 'correo')
    
@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_creacion', 'estado', 'total')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('cliente__nombre','id')