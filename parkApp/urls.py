"""parkApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from backoffice.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('index/', IndexClass.as_view(), name='index'),

    path('add/', DepartamentoAdd, name='departamento-add'),
    path('list/', DepartamentoList, name='departamento-list'),
    path('edit/<int:pk>', DepartamentoEdit, name='departamento-edit'),
    path('delete/<int:pk>', DepartamentoDelete, name='departamento-delete'),
    path('detail/<int:pk>', DepartamentoDetail, name='departamento-detail'),

    path('add_class/', DepartamentoAddClass.as_view(), name='departamento-class-add'),
    path('list_class/', DepartamentoListClass.as_view(), name='departamento-class-list'),
    path('edit_class/<int:pk>', DepartamentoEditClass.as_view(), name='departamento-class-edit'),
    path('delete_class/<int:pk>', DepartamentoDeleteClass.as_view(), name='departamento-class-delete'),
    path('detail_class/<int:pk>', DepartamentoDetailClass.as_view(), name='departamento-class-detail'),

]
