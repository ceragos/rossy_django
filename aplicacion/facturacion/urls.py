from django.contrib.auth.decorators import login_required
from django.urls import path

from aplicacion.facturacion.views import CreditosCobrarListView, FacturaPDF

urlpatterns = [
    path('credito_cobrar/', login_required(CreditosCobrarListView.as_view()), name = 'facturacion.credito_cobrar'),
    path(r'factura_pdf/(?P<factura_id>[-_:\w\d]+)', FacturaPDF.as_view(), name='factura_pdf'),
]
