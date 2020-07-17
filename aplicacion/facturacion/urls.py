from django.contrib.auth.decorators import login_required
from django.urls import path

from aplicacion.facturacion.views import CreditosCobrarListView, FacturaPDF

urlpatterns = [
    path('credito_cobrar/', login_required(CreditosCobrarListView.as_view()), name = 'facturacion.credito_cobrar'),
    path('factura_pdf/<str:factura_id>/', FacturaPDF.as_view(), name='factura_pdf'),
]
