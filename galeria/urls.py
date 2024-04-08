from django.urls import path
from . import views

app_name = 'galeria'

urlpatterns = [
    path('fotos/', views.galeria_fotos, name='galeria_fotos'),
    path('fotos/', views.fotos, name='fotos'),
    path('videos/', views.videos, name='videos'),
    path('planos/', views.planos, name='planos'),
]