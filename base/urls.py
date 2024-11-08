"""
URL configuration for base project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from base.views import principal, principal_admin, logout_user
from django_select2 import forms as select2forms
from . import views
from .views import formulario_cita



# para la gestion de login y contraseña
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',logout_user,name="logout"),
    path('admin/', admin.site.urls),
    path('',principal,name="index"),
    path('', include('galeria.urls')),
    path('cita/', views.cita_view, name='cita'),
    path('formulario_cita/', views.formulario_cita, name='procesar_cita'),





    path('adm/',principal_admin,name="index-admin"),
    path('comunidad/',include('comunidad.urls')),
    path('operaciones/',include('operaciones.urls')),
    path('configuraciones/',include('configuracion.urls')),
    path('reiniciar/',auth_views.PasswordResetView.as_view(),name='pass_reset'),
    path('reiniciar/enviar',auth_views.PasswordResetDoneView.as_view(),name='pass_reset_done'),
    path('reiniciar/<uid64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='pass_reset_confirm'),
    path('reiniciar/completo',auth_views.PasswordResetCompleteView.as_view(),name='pass_reset_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    path("select2/", include("django_select2.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)