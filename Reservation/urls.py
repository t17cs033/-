from django.urls import path

from . import views
from .views import MRShowView, BigMRReservationView, MiddleMRReservationView, SmallMRReservationView
from .views import ACornerReservationView, BCornerReservationView

urlpatterns = [
    path('', views.index, name='index'),
    path('mrshow', MRShowView.as_view(),name='mrshow'),
    path('mrbig', BigMRReservationView.as_view(),name='mrbig'),
    path('mrmid', MiddleMRReservationView.as_view(),name='mrmid'),
    path('mrsml', SmallMRReservationView.as_view(),name='mrsml'),
    path('cora', ACornerReservationView.as_view(),name='cora'),
    path('corb', BCornerReservationView.as_view(),name='corb'),
]