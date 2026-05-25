from django import forms
from .models import Ingreso


class IngresoForm(forms.ModelForm):

    class Meta:
        model = Ingreso

        fields = ['producto', 'talla', 'cantidad', 'precio']

        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'talla': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }