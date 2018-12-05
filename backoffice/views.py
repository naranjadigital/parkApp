from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from backoffice.forms import DepartamentoForm
from backoffice.models import *


def DepartamentoList(request):
    ctx = {'object_list': Departamento.objects.all()}
    return render(request, 'departamento/list.html', ctx)


def DepartamentoAdd(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('departamento-list')
        else:
            ctx = {'form': form}
            return render(request, 'departamento/add.html', ctx)

    ctx = {'form': DepartamentoForm()}
    return render(request, 'departamento/add.html', ctx)


def DepartamentoDetail(request, pk):
    departamento = Departamento.objects.get(pk=pk)
    ctx = {'object': departamento}

    return render(request, 'departamento/detail.html', ctx)


def DepartamentoEdit(request, pk):
    departamento = Departamento.objects.get(pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('departamento-list')
        else:
            ctx = {'form': form}
            return render(request, 'departamento/add.html', ctx)

    ctx = {'form': DepartamentoForm(instance=departamento)}
    return render(request, 'departamento/edit.html', ctx)


def DepartamentoDelete(request, pk):
    departamento = Departamento.objects.get(pk=pk)
    if request.method == 'POST':
        departamento.delete()
        return redirect('departamento-list')

    ctx = {'object': departamento}
    return render(request, 'departamento/delete.html', ctx)


def Index(request):
    ctx = {'msg' : 'Hola'}
    return render(request, 'index.html', ctx)


class IndexClass(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'Hola Con clase'
        return context


class DepartamentoListClass(ListView):
    template_name = 'departamento-clases/list.html'
    model = Departamento


class DepartamentoAddClass(CreateView):
    template_name = 'departamento-clases/add.html'
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('departamento-class-list')


class DepartamentoEditClass(UpdateView):
    template_name = 'departamento-clases/edit.html'
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('departamento-class-list')


class DepartamentoDeleteClass(DeleteView):
    template_name = 'departamento-clases/delete.html'
    model = Departamento
    success_url = reverse_lazy('departamento-class-list')


class DepartamentoDetailClass(DetailView):
    template_name = 'departamento-clases/detail.html'
    model = Departamento
