from django.urls import path

from . import views
from django.urls.conf import path
from Reservation.views import ReserveList, ReserveDetail, ReserveDelete
appname = "Reservation"

urlpatterns = [
    path('', views.index, name='index'),
    path('reserve_list/', ReserveList.as_view(), name = 'reserve_list'),
    path('reserve_list/<int:pk>/', ReserveDetail.as_view(), name = 'reserve_detail'),
    path('reserve_list/<int:pk>/delete/', ReserveDelete.as_view(), name = 'delete'),
    path('fcl_add/',views.fcl, name = 'fcl'),
]