"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ProyectoFinal.views import (index, PostDetalle, PostListar, PostCrear, PostBorrar, 
                                PostActualizar, UserSignUp, UserLogin, UserLogout,
                                AvatarActualizar, UserActualizar, MensajeListar, 
                                MensajeCrear, MensajeDetalle, MensajeBorrar)
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ProyectoFinal/', index, name = "ProyectoFinal-Index"),
    path('ProyectoFinal/<int:pk>/detalle/', PostDetalle.as_view(), name = "ProyectoFinal-Detalle"),
    path('ProyectoFinal/listar/', PostListar.as_view(), name = "ProyectoFinal-Listar"),
    path('ProyectoFinal/crear/', staff_member_required (PostCrear.as_view()), name = "ProyectoFinal-Crear"),
    path('ProyectoFinal/<int:pk>/borrar/', staff_member_required (PostBorrar.as_view()), name = "ProyectoFinal-Borrar"),
    path('ProyectoFinal/<int:pk>/actualizar/', staff_member_required (PostActualizar.as_view()), name = "ProyectoFinal-Actualizar"),    
    path('ProyectoFinal/signup/', UserSignUp.as_view(), name = "ProyectoFinal-SignUp"),
    path('ProyectoFinal/login/', UserLogin.as_view(), name = "ProyectoFinal-Login"),
    path('ProyectoFinal/logout/', UserLogout.as_view(), name = "ProyectoFinal-Logout"),
    path('ProyectoFinal/avatares/<int:pk>/actualizar/', AvatarActualizar.as_view(), name = "ProyectoFinal-Avatars-Actualizar"),
    path('ProyectoFinal/users/<int:pk>/actualizar/', UserActualizar.as_view(), name = "ProyectoFinal-User-Actualizar"),
    path('ProyectoFinal/mensajes/crear/', MensajeCrear.as_view(), name = "ProyectoFinal-Mensajes-Crear"),
    path('ProyectoFinal/mensajes/listar/', MensajeListar.as_view(), name = "ProyectoFinal-Mensajes-Listar"),
    path('ProyectoFinal/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name = "ProyectoFinal-Mensajes-Detalle"),
    path('ProyectoFinal/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name = "ProyectoFinal-Mensajes-Borrar"),
]

urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 