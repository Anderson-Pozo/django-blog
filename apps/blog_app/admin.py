from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


#----------------------CATEGORIA--------------------------
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion')
    resource_class = CategoriaResource

#--------------------- AUTOR --------------------------
class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'correo']
    list_display = ('nombres', 'apellidos', 'correo', 'estado','fecha_creacion')
    resource_class = AutorResource

#--------------------- POST --------------------------
class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'slug', 'descripcion']
    list_display = ('titulo', 'slug', 'descripcion', 'fecha_creacion')
    resource_class = PostResource


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
