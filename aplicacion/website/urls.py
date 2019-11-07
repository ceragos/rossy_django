from django.contrib.auth.decorators import login_required
from django.urls import path

from aplicacion.website.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
]