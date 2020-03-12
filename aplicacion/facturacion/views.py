from datetime import date, timedelta
from django.views.generic import ListView

from easy_pdf.views import PDFTemplateView

from aplicacion.facturacion.models import Factura, ProductoVenta


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


class FacturaPDF(PDFTemplateView):
    template_name = "impresiones/factura.html"

    def get_context_data(self, **kwargs):
        encrypted_id = kwargs['factura_id']
        factura_id = Factura.decryptId(encrypted_id)
        factura = Factura.objects.get(pk=factura_id)
        detalle_factura = ProductoVenta.objects.filter(factura=factura)
        kwargs['factura'] = factura
        kwargs['detalle_factura'] = detalle_factura
        return super(FacturaPDF, self).get_context_data(
            page_size="A4",
            title="Factura",
            **kwargs
        )
