from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):

    productos = Producto.objects.all()

    return render(request, 'productos/lista_productos.html', {
        'productos': productos
    })


def nuevo_producto(request):

    form = ProductoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/productos/')

    return render(request, 'productos/nuevo_producto.html', {
        'form': form
    })