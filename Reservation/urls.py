from django.urls import path

from . import views
from django.urls.conf import path
from Reservation.views import ReserveList, ReserveDetal,ReserveCalendar

appname = "Reservation"

urlpatterns = [
    path('', views.index, name='index'),
    path('reserve_list/', ReserveList.as_view(), name = 'reserve_list'),
    path('reserve_list/<int:pk>/', ReserveDetal.as_view(), name = 'reserve_detail'),
    path('month/<int:year>/<int:month>/', views.ReserveCalendar.as_view(), name='month'),
    path('reserve_calender/', ReserveCalendar.as_view(), name = 'reserve_calender'),
    path('reserve_calender/<int:pk>/', ReserveCalendar.as_view(), name = 'reserve_calender'),

    path('date/<int:pk>/<int:year>-<int:month>-<int:date>/', views.ReserveList.as_view(), name='date'),
    
]