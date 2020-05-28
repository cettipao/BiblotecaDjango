from django.forms import ModelForm, TextInput
from django.contrib.admin import ModelAdmin
from django.contrib import admin

# Register your models here.

from .models import *

class LibroForm(ModelForm):
    class Meta:
        widgets = {
            'titulo': TextInput(attrs={'class': 'input-mini'})
        }
        
class LibroAdmin(ModelAdmin):
    form = LibroForm


admin.site.register(Autor)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Usuario)
admin.site.register(Ejemplar)