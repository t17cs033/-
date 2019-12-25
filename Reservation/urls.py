from django.urls import path

from . import views
from Reservation.views import BillingView

appname='Reservation'
urlpatterns = [
    path('', views.index, name='index'),
    path('Billing',BillingView.as_view(),name='billing'),
]