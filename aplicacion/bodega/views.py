from datetime import date, timedelta

from django.views.generic import ListView

from aplicacion.bodega.models import ProduccionProducto


class ProductosVencidosListView(ListView):
    model = ProduccionProducto
    template_name = 'bodega/productos_por_vencer/productos.html'
    context_object_name = 'productos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductosVencidosListView, self).get_context_data(**kwargs)
        hoy = date.today()
        proxima_semana = hoy + timedelta(days=8)
        context['hoy'] = hoy
        context['proxima_semana'] = proxima_semana
        return context

    def get_queryset(self):
        hoy = date.today()
        proxima_semana = hoy + timedelta(days=8)
        productos = self.model.objects.all().order_by('fecha_vencimiento')
        return productos.filter(fecha_vencimiento__range=[hoy, proxima_semana], lote_agotado=False)
