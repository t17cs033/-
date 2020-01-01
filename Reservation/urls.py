from django.urls import path

from . import views
from .views import BillingView, BillingBase, GuideView

appname='Reservation'
urlpatterns = [
    path('', views.index, name='index'),
    path('Billing/',BillingBase.as_view(),name='billbase'),
    path('Billing/<int:pk>/',BillingView.as_view(),name='billing'),
    path('PriceGuide',GuideView.as_view(),name='guide')
]