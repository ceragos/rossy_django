from django.contrib.auth.decorators import login_required
from django.urls import path

from aplicacion.utilidades.views import IndexTemplateView

urlpatterns = [
    path('', (IndexTemplateView.as_view()), name = 'index'),
]