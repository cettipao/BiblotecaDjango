from django.contrib import admin

# Register your models here.

from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    #exclude = ('telefono',)
    fieldsets = (
        ("Informacion Personal", {
            'fields':('nombre','direccion','telefono',)
        }),
        ('Detalle de alquileres', {
            'fields':('ejemplares',)
        }),
    )
    list_display = ('nombre','telefono')

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Ejemplar)