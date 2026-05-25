from django import forms
from .models import Gasto

class GastoForm(forms.ModelForm):

    class Meta:

        model = Gasto

        fields = [
            'tipo',
            'descripcion',
            'valor',
        ]

        widgets = {

            'tipo': forms.Select(attrs={
                'class': 'form-control'
            }),

            'descripcion': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'valor': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

        }