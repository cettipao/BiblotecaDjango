from django.contrib import admin
from .models import Libro,Autor

# Register your models here.

from .models import *

class LibroInLine(admin.TabularInline):
    model = Libro

class UsuarioAdmin(admin.ModelAdmin):
    #exclude = ('telefono',)
    fieldsets = (
        ("Datos", {
            'fields':('codigo','nombre',)
        }),
        ('Contacto', {
            'fields':('telefono','direccion',)
        }),
        ('Ejemplares Alquilados', {
            'fields':('ejemplares',)
        }),
    )
    list_display = ('nombre','telefono')
    filter_vertical = ('ejemplares',)

class LibroAdmin(admin.ModelAdmin):
    exclude = ('paginas','autor',)
    list_display = ('titulo','editorial')
    #list_filter = ('titulo',)
    #inlines = [AutorInLine,]

class AutorAdmin(admin.ModelAdmin):
    inlines = [LibroInLine,]
    search_fields = ['nombre']

class EjemplarAdmin(admin.ModelAdmin):
    list_filter = ('libro',)


admin.site.register(Autor,AutorAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Ejemplar,EjemplarAdmin)