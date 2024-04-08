from django.forms import ModelForm
from operaciones.models import Producto, Foto

class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields= "__all__"
        exclude=["estado",]
        

class ProductoEditarForm(ModelForm):
    class Meta:
        model= Producto
        fields= "__all__"
        exclude=["estado",]


class FotoForm(ModelForm):
    class Meta:
        model= Foto
        fields= "__all__"
        exclude=["estado",]
        

class FotoEditarForm(ModelForm):
    class Meta:
        model= Foto
        fields= "__all__"
        exclude=["estado",]