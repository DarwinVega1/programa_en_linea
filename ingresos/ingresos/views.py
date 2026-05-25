from django.shortcuts import render, redirect
from .models import Ingreso
from .forms import IngresoForm

def lista_ingresos(request):

    ingresos = Ingreso.objects.all().order_by('-id')

    return render(request, 'ingresos/lista_ingresos.html', {
        'ingresos': ingresos
    })


def nuevo_ingreso(request):

    form = IngresoForm(request.POST or None)

    if form.is_valid():

        ingreso = form.save(commit=False)

        producto = ingreso.producto

        producto.stock += ingreso.cantidad

        producto.save()

        ingreso.save()

        return redirect('/ingresos/')

    return render(request, 'ingresos/nuevo_ingreso.html', {
        'form': form
    })