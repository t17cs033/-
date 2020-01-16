from django.urls import path
from . import views
from .views import BillingView, BillingBase, GuideView
from django.urls.conf import path
from Reservation.views import ReserveList, ReserveDetal
appname='Reservation'
urlpatterns = [
    path('', views.index, name='index'),
    path('Billing/',BillingBase.as_view(),name='billbase'),
    path('Billing/<int:pk>/',BillingView.as_view(),name='billing'),
    path('PriceGuide',GuideView.as_view(),name='guide'),
    path('reserve_list/', ReserveList.as_view(), name = 'reserve_list'),
    path('reserve_list/<int:pk>/', ReserveDetal.as_view(), name = 'reserve_detail'),
]