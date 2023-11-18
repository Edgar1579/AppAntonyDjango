from django.shortcuts import render, redirect
from comunidad.forms import UsuarioForm
from comunidad.models import Usuario
from PIL import Image
# Create your views here.
def usuario_crear(request):
    titulo="Usuario"
    usuarios= Usuario.objects.all()
    if request.method=="POST":
        form= UsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            usuario= form.save()
            if usuario.imagen:
                img =Image.open(usuario.imagen.path)
                img= img.resize((500,500))
                img.save(usuario.imagen.path)
            usuario.save()
            ## agregar el mensaje de exito
            return redirect("usuarios")
        else:
            ## agregar mensaje de error
            pass
    else:
        form=UsuarioForm()
    context={
        "titulo":titulo,
        "usuarios":usuarios,
        "form":form,
    }
    return render(request,"comunidad/usuarios/usuarios.html", context)

def usuario_eliminar(request,pk) :

    usuario=Usuario.objects.filter(id=pk)
    usuario.update(estado=False)
    ## Agregar mensaje de exito
    return redirect('usuarios')