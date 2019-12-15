from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria, Autor
from django.db.models import Q 
from django.core.paginator import Paginator

# Create your views here.
#-----------------------VISTA DE INICIO---------------
def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter( estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    posts = paginador(posts,request)

    return render(request,'index.html', {'posts':posts})

#-----------------------VISTAS DE CATEGORIAS---------------
def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
    )
    if queryset:
        posts = busqueda(queryset,'Tecnologia')

    posts = paginador(posts,request)

    return render(request,'tecnologia.html', {'posts':posts})


def programacion(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
    )
    if queryset:
        posts = busqueda(queryset,'Programacion')
    posts = paginador(posts,request)

    return render(request,'programacion.html',{'posts':posts}) 

def actualidad(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Actualidad')
    )

    if queryset:
        posts = busqueda(queryset,'Actualidad')

    posts = paginador(posts,request)
    
    return render(request,'actualidad.html',{'posts':posts})

#---------------------VISTA DE CONTACTO------------------------------

def contacto(request):
    return render(request,'contacto.html')


#---------------------DETALLE POST------------------------------
def detallePost(request,slug,id):
    post = get_object_or_404(Post, slug = slug , id = id)
    return render(request,'post.html',{'detalle_post':post})

#--------------------------VISTA DE AUTOR---------------------------
def autor(request,id):
    autor = get_object_or_404(Autor, id = id)
    if autor.facebook is None:
        autor.facebook = '#'
    if autor.twitter is None:
        autor.twitter = '#'
    if autor.github is None:
        autor.github = '#'         
    return render(request,'autor.html',{'autor':autor})


"""
Funciones para buscar y paginar utilizadas en cada categoria
"""
#------------------BUSQUEDA-----------------------------------
def busqueda(queryset,categoria):
    posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = categoria),
    ).distinct()
    return posts    

#------------------PAGINADOR-----------------------------------
def paginador(posts, request):
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return posts
