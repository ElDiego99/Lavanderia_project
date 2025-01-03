"""
URL configuration for lavanderia_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from clientes.views import LoginView, ClienteList, ClienteDetail, ServicioList, ServicioDetail, OrdenList, OrdenDetail

urlpatterns = [ path('admin/', admin.site.urls), 
path('api/clientes/', ClienteList.as_view(), name='cliente-list'), 
path('api/clientes/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'), 
path('api/servicios/', ServicioList.as_view(), name='servicio-list'), 
path('api/servicios/<int:pk>/', ServicioDetail.as_view(), name='servicio-detail'), 
path('api/ordenes/', OrdenList.as_view(), name='orden-list'), 
path('api/ordenes/<int:pk>/', OrdenDetail.as_view(), name='orden-detail'),
path('api/login/', LoginView.as_view(),name='login-view')
]