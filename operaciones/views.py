from django.shortcuts import render,redirect
from operaciones.models import Producto
from operaciones.forms import ProductoForm,ProductoEditarForm,FotoForm,FotoEditarForm
from django.contrib import messages
from .models import Foto


from PIL import Image
from PIL import Image
# Create your views here.
def producto_crear(request):
    titulo="Producto"
    accion="Agregar"
    productos= Producto.objects.all()
    if request.method=="POST":
        form= ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            producto= form.save()
            if producto.imagen:
                img = Image.open(producto.imagen.path)
                img= img.resize((500,500))
                img.save(producto.imagen.path)
            producto.save()
            messages.success(request, f'¡El Producto se agregó de forma exitosa!')

            return redirect("productos")
        else:
            messages.success(request, f'¡Error al agregar al Producto!')
    else:
        form=ProductoForm()
    context={
        "titulo":titulo,
        "productos":productos,
        "form":form,
        "accion":accion
    }
    return render(request,"operaciones/productos/productos.html", context)


def producto_editar(request,pk):
    producto= Producto.objects.get(id=pk)
    productos= Producto.objects.all()
    accion="Editar"
    nombre=f"{producto.nombre}"
    titulo=f"Producto {producto.id} {nombre}"

    if request.method=="POST":
        form= ProductoEditarForm(request.POST,request.FILES, instance=producto)
        if form.is_valid():
            producto= form.save()
            if producto.imagen:
                img = Image.open(producto.imagen.path)
                img= img.resize((500,500))
                img.save(producto.imagen.path)
            producto.save()
            messages.success(request, f'¡{nombre} se editó de forma exitosa!')
            return redirect("productos")
        else:
            messages.error(request, f'¡Error al editar a {nombre}!')

    else:
        form=ProductoEditarForm(instance=producto)
    context={
        "titulo":titulo,
        "productos":productos,
        "form":form,
        "accion":accion
    }
    return render(request,"operaciones/productos/productos.html", context)
def producto_eliminar(request,pk):

    producto=Producto.objects.filter(id=pk)
    producto.update(estado=False)
    
    messages.success(request, f'¡El Producto "{producto[0].nombre}" se eliminó correctamente!')
    return redirect('productos')

def foto_crear(request):
    titulo="Foto"
    accion="Agregar"
    fotos= Foto.objects.all()
    if request.method=="POST":
        form= FotoForm(request.POST,request.FILES)
        if form.is_valid():
            foto= form.save()
            if foto.imagen:
                img = Image.open(foto.imagen.path)
                img= img.resize((500,500))
                img.save(foto.imagen.path)
            foto.save()
            messages.success(request, f'¡La Foto se agregó de forma exitosa!')

            return redirect("fotos")
        else:
            messages.success(request, f'¡Error al agregar la foto!')
    else:
        form=FotoForm()
    context={
        "titulo":titulo,
        "fotos":fotos,
        "form":form,
        "accion":accion
    }
    return render(request,"operaciones/fotos/fotos.html", context)


def foto_editar(request,pk):
    foto= Foto.objects.get(id=pk)
    fotos= Foto.objects.all()
    accion="Editar"
    nombre=f"{foto.nombre}"
    titulo=f"Producto {foto.id} {nombre}"

    if request.method=="POST":
        form= FotoEditarForm(request.POST,request.FILES, instance=foto)
        if form.is_valid():
            foto= form.save()
            if foto.imagen:
                img = Image.open(foto.imagen.path)
                img= img.resize((500,500))
                img.save(foto.imagen.path)
            foto.save()
            messages.success(request, f'¡{nombre} se editó de forma exitosa!')
            return redirect("fotos")
        else:
            messages.error(request, f'¡Error al editar a {nombre}!')

    else:
        form=FotoEditarForm(instance=foto)
    context={
        "titulo":titulo,
        "fotos":fotos,
        "form":form,
        "accion":accion
    }
    return render(request,"operaciones/fotos/fotos.html", context)
def foto_eliminar(request,pk):

    foto=foto.objects.filter(id=pk)
    foto.update(estado=False)
    
    messages.success(request, f'¡La Foto "{foto[0].nombre}" se eliminó correctamente!')
    return redirect('fotos')