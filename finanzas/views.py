from django.shortcuts import render

from ventas.models import Venta
from gastos.models import Gasto
from productos.models import Producto

from django.db.models import Sum, F
from django.db.models.functions import TruncDate, TruncMonth


def dashboard_finanzas(request):

    # =========================
    # TOTALES
    # =========================

    total_ventas = Venta.objects.aggregate(
        total=Sum('total')
    )['total'] or 0

    total_gastos = Gasto.objects.aggregate(
        total=Sum('valor')
    )['total'] or 0

    total_productos = Producto.objects.count()

    valor_inventario = Producto.objects.aggregate(
        total=Sum(F('stock') * F('precio'))
    )['total'] or 0

    ganancia = total_ventas - total_gastos

    # =========================
    # VENTAS POR DÍA
    # =========================

    ventas_por_dia = (
        Venta.objects
        .annotate(fecha_dia=TruncDate('fecha'))
        .values('fecha_dia')
        .annotate(total=Sum('total'))
        .order_by('fecha_dia')
    )

    # =========================
    # GASTOS POR DÍA
    # =========================

    gastos_por_dia = (
        Gasto.objects
        .annotate(fecha_dia=TruncDate('fecha'))
        .values('fecha_dia')
        .annotate(total=Sum('valor'))
        .order_by('fecha_dia')
    )

    # =========================
    # VENTAS POR MES
    # =========================

    ventas_por_mes = (
        Venta.objects
        .annotate(mes=TruncMonth('fecha'))
        .values('mes')
        .annotate(total=Sum('total'))
        .order_by('mes')
    )

    # =========================
    # GASTOS POR MES
    # =========================

    gastos_por_mes = (
        Gasto.objects
        .annotate(mes=TruncMonth('fecha'))
        .values('mes')
        .annotate(total=Sum('valor'))
        .order_by('mes')
    )

    context = {

        'total_ventas': total_ventas,
        'total_gastos': total_gastos,
        'ganancia': ganancia,
        'total_productos': total_productos,
        'valor_inventario': valor_inventario,

        'ventas_por_dia': ventas_por_dia,
        'gastos_por_dia': gastos_por_dia,

        'ventas_por_mes': ventas_por_mes,
        'gastos_por_mes': gastos_por_mes,

    }

    return render(
        request,
        'finanzas/dashboard.html',
        context
    )