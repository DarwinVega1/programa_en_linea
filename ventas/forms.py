from django import forms
from .models import Venta, Cliente
from productos.models import Producto


class VentaForm(forms.ModelForm):

    class Meta:

        model = Venta

        fields = [
            'cliente',
            'producto',
            'cantidad',
            'precio',
            'metodo_pago',
        ]

        widgets = {

            'cliente': forms.Select(attrs={
                'class': 'form-control'
            }),

            'producto': forms.Select(attrs={
                'class': 'form-control'
            }),

            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'cantidad'
            }),

            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),

        }

    cliente = forms.ModelChoiceField(

        queryset=Cliente.objects.all(),

        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'cliente'
        })
    )

    producto = forms.ModelChoiceField(

        queryset=Producto.objects.all(),

        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'producto'
        })
    )
class ClienteForm(forms.ModelForm):

    class Meta:

        model = Cliente

        fields = [
            'documento',
            'nombres',
            'direccion'
        ]

        widgets = {

            'documento': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'nombres': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'direccion': forms.TextInput(attrs={
                'class': 'form-control'
            }),

        }