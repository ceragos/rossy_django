from django.urls import path

from aplicacion.utilidades.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name = 'index'),
]