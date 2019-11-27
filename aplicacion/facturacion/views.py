from datetime import date, timedelta
from django.views.generic import ListView

from aplicacion.facturacion.models import Factura


class CreditosCobrarListView(ListView):
    model = Factura
    template_name = 'facturacion/creditos_por_cobrar/creditos_cobrar.html'
    context_object_name = 'creditos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CreditosCobrarListView, self).get_context_data(**kwargs)
        hoy = date.today()
        proxima_semana = hoy + timedelta(days=8)
        context['hoy'] = hoy
        context['proxima_semana'] = proxima_semana
        return context

    def get_queryset(self):
        hoy = date.today()
        proxima_semana = hoy + timedelta(days=8)
        facturas = self.model.objects.all().order_by('fecha_pago')
        return facturas.filter(credito=True, pagada=False)
