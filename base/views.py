from django.shortcuts import render, redirect

from operaciones.models import Producto
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from comunidad.models import Usuario, Tienda
from operaciones.models import Pedido,Producto,Foto
from configuracion.models import Slider
from django.db.models import Count,Q
from django_select2 import forms as select2forms
from operaciones.models import Cita # Asegúrate de importar el modelo Cita desde tu archivo models.py


def principal(request):
    titulo="Bienvenido"
    sliders= Slider.objects.filter(estado=True)
    productos= Producto.objects.all()
    context={
        "titulo": titulo,
        "sliders": sliders,
        "productos":productos
    }
    return render(request, "index.html", context)
@login_required
def principal_admin(request):
    titulo = "Bienvenido"
    
    # Obtener las cantidades correctas
    usuarios = Usuario.objects.all().count()
    tiendas = Tienda.objects.all().count()  
    productos = Producto.objects.all().count() 
    pedidos = Pedido.objects.all().count()  

    # Obtener nombres de tiendas y cantidad de productos por tienda
    tiendas_con_productos = Tienda.objects.annotate(cantidad_productos=Count('producto', filter=Q(producto__estado=True))).values('nombre', 'cantidad_productos')
    
    
    usuarios_obj = Usuario.objects.all()

    context = {
        "titulo": titulo,
        "usuarios_cantidad": usuarios,
        "tiendas_cantidad": tiendas,
        "productos_cantidad": productos,
        "pedidos_cantidad": pedidos,
        "usuarios_obj": usuarios_obj,
        "tiendas_con_productos": tiendas_con_productos
    }

    return render(request, "index-admin.html", context)

def logout_user(request):
    logout(request)
    return redirect('index')

def cita_view(request):
    # Aquí puedes agregar la lógica para procesar el formulario de citas
    return render(request, 'formulario_citas.html')

def formulario_cita(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        comentarios = request.POST.get('comentarios')

        # Validar los datos del formulario (puedes agregar tu lógica de validación aquí)

        # Crear una nueva instancia de Cita y guardarla en la base de datos
        nueva_cita = formulario_cita(nombre=nombre, email=email, telefono=telefono, fecha=fecha, hora=hora, comentarios=comentarios)
        nueva_cita.save()

        # Redirigir a una página de éxito
        return render(request, 'cita_exitosa.html')

    # Si la solicitud no es POST, redirigir a una página de error o volver al formulario
    return render(request, 'formulario_cita.html')