from django.contrib.auth.decorators import login_required
from django.urls import path

from aplicacion.facturacion.views import CreditosCobrarListView

urlpatterns = [
    path('credito_cobrar/', login_required(CreditosCobrarListView.as_view()), name = 'facturacion.credito_cobrar'),
]
