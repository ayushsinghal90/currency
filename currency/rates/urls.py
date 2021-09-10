from django.urls import path

from .views import RatesView

urlpatterns = [
    path('', RatesView.as_view())
]
