from django.urls.conf import path
from . import views

from .views import MRShowView, BigMRReservationView, MiddleMRReservationView, SmallMRReservationView
from .views import ACornerReservationView, BCornerReservationView
from Reservation.views import ReserveCalendar

from .views import BillingView, BillingBase, GuideView

from Reservation.views import LoginView,SelectView,Select,BillingTestView, BillingTest, ReservationTestView,ReservationTest,ReserveList, ReserveDetail,ReserveDelete

app_name = 'Reservation'

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('select',SelectView.as_view(),name ='select'),
    path('select/<int:pk>',Select.as_view(),name='sel'),
    path('billing',BillingTestView.as_view(),name ='billing'),
    path('billing/<int:pk>',BillingTest.as_view(),name='t_b'),
    path('reservation',ReservationTestView.as_view(),name='reservation'),
    path('reservation/<int:pk>',ReservationTest.as_view(),name='reser'),

    path('mrshow', MRShowView.as_view(), name='mr'),
    path('mrshow/<int:pk>/<int:year>-<int:month>-<int:day>/', MRShowView.as_view(),name='mrshow'),
    path('mrbig/<int:pk>/<int:year>-<int:month>-<int:day>/', BigMRReservationView.as_view(),name='mrbig'),
    path('mrmid/<int:pk>/<int:year>-<int:month>-<int:day>/', MiddleMRReservationView.as_view(),name='mrmid'),
    path('mrsml/<int:pk>/<int:year>-<int:month>-<int:day>/', SmallMRReservationView.as_view(),name='mrsml'),
    path('cora/<int:pk>/<int:year>-<int:month>-<int:day>/', ACornerReservationView.as_view(),name='cora'),
    path('corb/<int:pk>/<int:year>-<int:month>-<int:day>/', BCornerReservationView.as_view(),name='corb'),
    path('reserve_list/', ReserveList.as_view(), name = 'reserve_list'),
    path('reserve_list/<int:pk>/', ReserveDetail.as_view(), name = 'reserve_detail'),

    path('reserve_list/<int:pk>/delete/', ReserveDelete.as_view(), name = 'delete'),
    path('fcl_add/',views.fcl, name = 'fcl'),
    
    path('Billing/',BillingBase.as_view(),name='billbase'),
    path('Billing/<int:pk>/',BillingView.as_view(),name='billing'),
    path('PriceGuide',GuideView.as_view(),name='guide'),
  
    path('month/<int:pk>/<int:year>/<int:month>/', views.ReserveCalendar.as_view(), name='month'),
    path('reserve_calender/', ReserveCalendar.as_view(), name = 'reserve_calender'),
    path('reserve_calender/<int:pk>/', ReserveCalendar.as_view(), name = 'reserve_calender'),
    path('date/<int:pk>/<int:year>-<int:month>-<int:date>/', views.ReserveList.as_view(), name='date'),
]

