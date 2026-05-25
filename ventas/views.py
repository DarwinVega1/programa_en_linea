from django.shortcuts import render, redirect
from .models import Venta
from .forms import VentaForm


def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})


def nueva_venta(request):

    if request.method == 'POST':

        form = VentaForm(request.POST)

        if form.is_valid():

            venta = form.save(commit=False)

            # CALCULAR TOTAL
            venta.total = venta.cantidad * venta.precio

            venta.save()

            return redirect('lista_ventas')

    else:

        form = VentaForm()

    return render(request, 'ventas/nueva_venta.html', {

        'form': form

    })