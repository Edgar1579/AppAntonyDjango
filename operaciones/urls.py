from django.urls import path
from operaciones.views import *
urlpatterns = [
    path("productos-admin/", producto_crear, name="productos"),
    path("productos/eliminar/<int:pk>/", producto_eliminar, name="producto-eliminar"),
    path("productos/editar/<int:pk>/", producto_editar, name="producto-editar"),
    
    path("fotos-admin/", foto_crear, name="fotos"),
    path("fotos/eliminar/<int:pk>/", foto_eliminar, name="foto-eliminar"),
    path("fotos/editar/<int:pk>/", foto_editar, name="foto-editar")

]