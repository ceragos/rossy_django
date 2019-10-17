from django.db.models import Sum
from django.shortcuts import render

from django.views.generic import TemplateView

from aplicacion.facturacion.models import Factura, AbonoCredito


class IndexTemplateView(TemplateView):
    template_name = 'utilidades/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {
            'ventas_contado': self.get_ventas_contado(),
            'ventas_credito': self.get_ventas_credito(),
            'abonos_credito': self.get_abonos_credito(),
        }
        return context

    def get_ventas_contado(self):
        total = Factura.objects.filter(contado=True).aggregate(total=Sum('total'))['total']
        print('contado', total)
        return total

    def get_ventas_credito(self):
        total = Factura.objects.filter(credito=True).aggregate(total=Sum('total'))['total']
        print('credito', total)
        return total

    def get_abonos_credito(self):
        total = AbonoCredito.objects.aggregate(total=Sum('valor_abono'))['total']
        print('abonos', total)
        return total
