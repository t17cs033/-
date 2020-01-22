from django.urls.conf import path
from . import views

from .views import MRShowView, BigMRReservationView, MiddleMRReservationView, SmallMRReservationView
from .views import ACornerReservationView, BCornerReservationView
from Reservation.views import ReserveList, ReserveDetal

app_name = 'Reservation'
urlpatterns = [
    path('', views.index, name='index'),
    path('mrshow', MRShowView.as_view(), name='mr'),
    path('mrshow/<int:pk>/<int:year>-<int:month>-<int:day>/', MRShowView.as_view(),name='mrshow'),
    path('mrbig/<int:pk>/<int:year>-<int:month>-<int:day>/', BigMRReservationView.as_view(),name='mrbig'),
    path('mrmid/<int:pk>/<int:year>-<int:month>-<int:day>/', MiddleMRReservationView.as_view(),name='mrmid'),
    path('mrsml/<int:pk>/<int:year>-<int:month>-<int:day>/', SmallMRReservationView.as_view(),name='mrsml'),
    path('cora/<int:pk>/<int:year>-<int:month>-<int:day>/', ACornerReservationView.as_view(),name='cora'),
    path('corb/<int:pk>/<int:year>-<int:month>-<int:day>/', BCornerReservationView.as_view(),name='corb'),
    path('reserve_list/', ReserveList.as_view(), name = 'reserve_list'),
    path('reserve_list/<int:pk>/', ReserveDetal.as_view(), name = 'reserve_detail'),
]

