from django.urls import path

from backoffice.views import *
from django.contrib.auth import views as auth_views

app_name = 'bo'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('departamento/add/', DepartamentoAdd.as_view(), name='departamento-add'),
    path('departamento/', DepartamentoList.as_view(), name='departamento-list'),
    path('departamento/edit/<int:pk>', DepartamentoEdit.as_view(), name='departamento-edit'),
    path('departamento/delete/<int:pk>', DepartamentoDelete.as_view(), name='departamento-delete'),
    path('departamento/detail/<int:pk>', DepartamentoDetail.as_view(), name='departamento-detail'),

    path('estacionamiento/add/', EstacionamientoAdd.as_view(), name='estacionamiento-add'),
    path('estacionamiento/', EstacionamientoList.as_view(), name='estacionamiento-list'),
    path('estacionamiento/edit/<int:pk>', EstacionamientoEdit.as_view(), name='estacionamiento-edit'),

    path('api/v1/departamento/', ApiDepartamentoList.as_view()),
    path('api/v1/provincia/', ApiProvinciaList.as_view()),
    path('api/v1/distrito/', ApiDistritoList.as_view()),
    path('api/v1/estacionamiento/', ApiEstacionamientoList.as_view()),
    path('api/v1/estacionamiento/<int:pk>', ApiEstacionamientoEdit.as_view()),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
