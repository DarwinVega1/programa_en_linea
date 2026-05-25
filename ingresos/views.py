from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingreso
from .forms import IngresoForm


def lista_ingresos(request):
    ingresos = Ingreso.objects.select_related('producto').all()
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

        return redirect('lista_ingresos')

    return render(request, 'ingresos/nuevo_ingreso.html', {'form': form})


def editar_ingreso(request, id):
    ingreso = get_object_or_404(Ingreso, id=id)

    stock_anterior = ingreso.cantidad

    form = IngresoForm(request.POST or None, instance=ingreso)

    if form.is_valid():
        data = form.save(commit=False)

        producto = data.producto

        # revertir stock anterior
        producto.stock -= stock_anterior

        # aplicar nuevo stock
        producto.stock += data.cantidad

        producto.save()
        data.save()

        return redirect('lista_ingresos')

    return render(request, 'ingresos/nuevo_ingreso.html', {'form': form})