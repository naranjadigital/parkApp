from django import forms
from django.core.exceptions import ValidationError

from backoffice.models import *


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")

        if len(nombre) < 4:
            self.add_error('nombre', 'Nombre muy pequeño')

        existe = Departamento.objects.filter(nombre__contains=nombre).exclude(id=self.instance.pk)
        if existe:
            self.add_error('nombre', 'Nombre ya existe')


class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

