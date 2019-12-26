from django.urls import path

from . import views
from django.urls.conf import path
from Reservation.views import ReserveList, ReserveDetal

appname = "Reservation"

urlpatterns = [
    path('', views.index, name='index'),
    path('reserve_list/', ReserveList.as_view(), name = 'reserve_list'),
    path('reserve_list/<int:pk>/', ReserveDetal.as_view(), name = 'reserve_detail'),
]