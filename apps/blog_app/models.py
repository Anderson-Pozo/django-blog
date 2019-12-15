from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
# ------------------------MODELO CATEGORIA----------------------
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la categoría', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Activo/Inactivo', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_modificacion = models.DateField('Fecha de modificación', auto_now = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['nombre']

    def __str__(self):
        return self.nombre


# ------------------------MODELO AUTOR ----------------------
class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField('Nombres', max_length = 150, null = False, blank = False)
    apellidos = models.CharField('Apellidos', max_length = 150, null = False, blank = False)
    descripcion = RichTextField('Descripción', default = 'No hay información')
    imagen = models.URLField('URL de la imagen', max_length = 250, null = False, blank = False, default = 'https://cdn.icon-icons.com/icons2/1879/PNG/512/iconfinder-7-avatar-2754582_120519.png')
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    github = models.URLField('GitHub', null = True, blank = True)
    web = models.URLField('Web', null = True, blank = True)
    correo = models.EmailField('Correo electrónico', null = False, blank = False)
    estado = models.BooleanField('Activo/Inactivo', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_modificacion = models.DateField('Fecha de modificación', auto_now = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['id']

    def __str__(self):
        return "{0}, {1}".format(self.apellidos, self.nombres)

# ------------------------MODELO POST ----------------------
class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 100 , null = False, blank = False)
    slug = models.CharField('Slug', max_length = 100, null = False, blank = False)
    descripcion = models.CharField('Descripción', max_length = 150, null = False, blank = False)
    contenido = RichTextField('Contenido')
    imagen = models.URLField('URL de la imagen', max_length = 250, null = False, blank = False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/Despublicado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_modificacion = models.DateField('Fecha de modificación', auto_now = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']

    def __str__(self):
        return self.titulo    


