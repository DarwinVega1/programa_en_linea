from django.shortcuts import render, redirect
from .models import Gasto
from .forms import GastoForm


def lista_gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'gastos/lista_gastos.html', {'gastos': gastos})


def nuevo_gasto(request):
    form = GastoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_gastos')

    return render(request, 'gastos/nuevo_gasto.html', {'form': form})