from .views import MRShowView, BigMRReservationView, MiddleMRReservationView, SmallMRReservationView
from .views import ACornerReservationView, BCornerReservationView
from .views import BillingView, GuideView
from Reservation.views import LoginView,SelectView,Select, ReserveList, ReserveDetail,ReserveDelete,ReserveCalendar
from django.urls import path
from . import views

appname = 'Reservation'

urlpatterns = [

    path('login/',LoginView.as_view(),name='login'),
    path('select',SelectView.as_view(),name ='select'),
    path('select/<int:pk>',Select.as_view(),name='sel'),

    path('mrshow/<int:pk>/<int:year>-<int:month>-<int:day>/', MRShowView.as_view(),name='mrshow'), #会議室一覧
    path('mrbig/<int:pk>/<int:year>-<int:month>-<int:day>/', BigMRReservationView.as_view(),name='mrbig'),  #大会議室
    path('mrmid/<int:pk>/<int:year>-<int:month>-<int:day>/', MiddleMRReservationView.as_view(),name='mrmid'),  #中会議室
    path('mrsml/<int:pk>/<int:year>-<int:month>-<int:day>/', SmallMRReservationView.as_view(),name='mrsml'),  #小会議室
    path('cora/<int:pk>/<int:year>-<int:month>-<int:day>/', ACornerReservationView.as_view(),name='cora'),  #コーナーA
    path('corb/<int:pk>/<int:year>-<int:month>-<int:day>/', BCornerReservationView.as_view(),name='corb'),  #コーナーB


    path('reserve_list/', ReserveList.as_view(), name = 'reserve_list'),
    path('reserve_list/<int:mem_pk>/', ReserveList.as_view(), name = 'reserve_list'),
    path('detail', ReserveDetail.as_view(), name = 'detail'),
    path('detail/<int:mem_pk>/<int:pk>', ReserveDetail.as_view(), name = 'detail'),
    
    path('delete', ReserveDelete.as_view(), name = 'delete'), 
    path('delete/<int:mem_pk>/<int:pk>/', ReserveDelete.as_view(), name = 'delete'),

    path('fcl_add/',views.fcl, name = 'fcl'),

    path('billing', BillingView.as_view(), name = 'billing'),
    path('billing/<int:pk>/', BillingView.as_view(),name = "bill"),
    path('PriceGuide/<int:pk>/<int:year>-<int:month>-<int:day>/',GuideView.as_view(),name='guide'),

    path('month/<int:pk>/<int:year>/<int:month>/', views.ReserveCalendar.as_view(), name='month'),
    path('reserve_calender', ReserveCalendar.as_view(), name = 'reserve_calender'),
    path('reserve_calender/<int:pk>/', ReserveCalendar.as_view(), name = 'reserve_calender'),
    path('date/<int:pk>/<int:year>-<int:month>-<int:date>/', views.ReserveList.as_view(), name='date'),
]
