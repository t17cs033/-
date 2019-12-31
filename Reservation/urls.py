from django.urls import path

from . import views
from .views import BillingView, BillingBase

appname='Reservation'
urlpatterns = [
    path('', views.index, name='index'),
    path('Billing/',BillingBase.as_view(),name='billbase'),
    path('Billing/<int:pk>/',BillingView.as_view(),name='billing'),
]