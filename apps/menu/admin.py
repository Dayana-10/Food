from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

class resourcetipo_de_dulce(resources.ModelResource):
    class Meta:
        model = tipo_de_dulce

class Admintipo_de_dulce(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['sabor']
    resource_class = resourcetipo_de_dulce
admin.site.register(tipo_de_dulce,Admintipo_de_dulce)

class resourcedisponible(resources.ModelResource):
    class Meta:
        model = disponible

class Admindisponible(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['cantidad']
    resource_class = resourcedisponible
admin.site.register(disponible,Admindisponible)

#separador
class resourceproducto(resources.ModelResource):
    class Meta:
        model = producto

class Adminproducto(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['cantidad_de_venta','marca','precio','fk_tipo_de_dulce','fk_disponible']
    resource_class = resourceproducto

admin.site.register(producto,Adminproducto)

class resourceventa(resources.ModelResource):
    class Meta:
        model = venta

class Adminventa(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['cantidad']
    resource_class = resourceventa
admin.site.register(venta,Adminventa)