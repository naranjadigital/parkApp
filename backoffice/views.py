from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework import generics

from backoffice.forms import *
from backoffice.models import *
from backoffice.serializer import *


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'Inicio'
        return context


class DepartamentoList(ListView):
    template_name = 'departamento/list.html'
    model = Departamento


class DepartamentoAdd(CreateView):
    template_name = 'base/add.html'
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('bo:departamento-list')


class DepartamentoEdit(UpdateView):
    template_name = 'base/edit.html'
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('bo:departamento-list')


class DepartamentoDelete(DeleteView):
    template_name = 'departamento/delete.html'
    model = Departamento
    success_url = reverse_lazy('bo:departamento-list')


class DepartamentoDetail(DetailView):
    template_name = 'departamento/detail.html'
    model = Departamento


class EstacionamientoList(ListView):
    template_name = 'estacionamiento/list.html'
    model = Estacionamiento


class EstacionamientoAdd(CreateView):
    template_name = 'estacionamiento/add_edit.html'
    model = Estacionamiento
    form_class = EstacionamientoForm
    success_url = reverse_lazy('bo:estacionamiento-list')


class EstacionamientoEdit(UpdateView):
    template_name = 'estacionamiento/add_edit.html'
    model = Estacionamiento
    form_class = EstacionamientoForm
    success_url = reverse_lazy('bo:estacionamiento-list')


class ApiDepartamentoList(generics.ListCreateAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class ApiProvinciaList(generics.ListCreateAPIView):
    serializer_class = ProvinciaSerializer

    def get_queryset(self):

        queryset = Provincia.objects.all()

        departamento = self.request.query_params.get('departamento', None)
        if departamento is not None:
            queryset = queryset.filter(departamento__nombre__contains=departamento)


        departamento_id = self.request.query_params.get('departamento_id', None)
        if departamento_id is not None:
            queryset = queryset.filter(departamento__id=departamento_id)

        return queryset


class ApiDistritoList(generics.ListCreateAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer


class ApiEstacionamientoList(generics.ListCreateAPIView):
    serializer_class = EstacionamientoSerializer

    def get_queryset(self):

        queryset = Estacionamiento.objects.all()

        nombre = self.request.query_params.get('nombre', None)
        if nombre is not None:
            queryset = queryset.filter(nombre__contains=nombre)

        return queryset


class ApiEstacionamientoEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EstacionamientoSerializer
    queryset = Estacionamiento.objects.all()

