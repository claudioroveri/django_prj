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
from django.contrib import admin
from django.urls import path, include
from app.views import formUsuario, formCliente, home, form, formMarca, create, createMarca, createCliente, carro, marca, view, delete, deleteMarca, deleteCarros, update, updateMarca, edit, editMarca, formUsuario, usuario, removeUsuario, createUser, addUser
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('carro/', carro, name='carro'),
    path('marca/', marca, name='marca'),
    path('usuarios/', usuario, name='usuario'),
    path('usuarios/<int:pk>/', removeUsuario, name='removeUsuario'),
    path('form/', form, name='form'),
    path('formMarca/', formMarca, name='formMarca'),
    path('create/', create, name='create'),
    path('createMarca/', createMarca, name='createMarca'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('deleteCarros/<int:pk>/', deleteCarros, name='delete2'),
    path('deleteMarca/<int:pk>/', deleteMarca, name='deleteMarca'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('editMarca/<int:pk>/', editMarca, name='editmarca'),
    path('update/<int:pk>/', update, name='update'),
    path('updateMarca/<int:pk>/', updateMarca, name='updateMarca'),
    path('view//', view, name="view"),
    path('api/v1/', include('app.api.urls', namespace='api')), # APIs REST
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')), 
    path('formUsuario/', formUsuario, name='formUsuario'),
    path('formCliente/', formCliente, name='formCliente'),
    path('createCliente/', createCliente, name='createCliente'),
    path('createUser/', createUser, name='createUser'), #interface de criacao de usuario
    path('addUser/', addUser, name='addUser'), #action de criacao de usuario autenticavel no framework
    path('accounts/', include('django.contrib.auth.urls')), #telas de login (exceto criação de usuario)
    
]




