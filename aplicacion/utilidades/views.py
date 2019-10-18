from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render

from django.views.generic import TemplateView

from aplicacion.facturacion.models import Factura, AbonoCredito
from aplicacion.utilidades.forms import FiltroRangoFechaForm


class IndexTemplateView(TemplateView):
    template_name = 'utilidades/index.html'
    fecha_inicial = None
    fecha_final = None

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = FiltroRangoFechaForm()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final')
        if fecha_inicial and fecha_final:
            self.fecha_inicial = datetime.strptime(fecha_inicial, '%Y-%m-%d')
            self.fecha_final = datetime.strptime(fecha_final, '%Y-%m-%d')
        form = FiltroRangoFechaForm(request.POST)
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {
            'total_facturas': self.get_total_facturas(),
            'ventas_contado': self.get_ventas_contado(),
            'ventas_credito': self.get_ventas_credito(),
            'abonos_credito': self.get_abonos_credito(),
        }
        return context

    def get_total_facturas(self):
        queryset_factura = Factura.objects.all()
        if self.fecha_inicial and self.fecha_final:
            queryset_factura = queryset_factura.filter(fecha_compra__range=[self.fecha_inicial, self.fecha_final])
        total = queryset_factura.aggregate(total=Sum('total'))['total']
        return total if total else 0

    def get_ventas_contado(self):
        queryset_factura = Factura.objects.filter(contado=True)
        if self.fecha_inicial and self.fecha_final:
            queryset_factura = queryset_factura.filter(fecha_compra__range=[self.fecha_inicial, self.fecha_final])
        total = queryset_factura.aggregate(total=Sum('total'))['total']
        return total if total else 0

    def get_ventas_credito(self):
        queryset_factura = Factura.objects.filter(credito=True)
        if self.fecha_inicial and self.fecha_final:
            queryset_factura = queryset_factura.filter(fecha_compra__range=[self.fecha_inicial, self.fecha_final])
        total = queryset_factura.aggregate(total=Sum('total'))['total']
        return total if total else 0

    def get_abonos_credito(self):
        queryset_abonos = AbonoCredito.objects.all()
        if self.fecha_inicial and self.fecha_final:
            queryset_abonos = queryset_abonos.filter(fecha_abono__range=[self.fecha_inicial, self.fecha_final])
        total = queryset_abonos.aggregate(total=Sum('valor_abono'))['total']
        return total if total else 0
