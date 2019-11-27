from django.contrib.auth.decorators import login_required
from django.urls import path

from aplicacion.bodega.views import ProductosVencidosListView

urlpatterns = [
    path('producto_vencer/', login_required(ProductosVencidosListView.as_view()), name = 'bodega.producto_vencer'),
]
