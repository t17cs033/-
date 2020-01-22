from django.urls import path
from . import views
from .views import BillingView, BillingBase, GuideView
from django.urls.conf import path
from Reservation.views import LoginView,SelectView,Select,ReservationTestView,ReservationTest,ReserveList, ReserveDetail,ReserveDelete,ReserveCalendar
from . import views
urlpatterns = [


    
  
    

    path('login/',LoginView.as_view(),name='login'),
    path('select',SelectView.as_view(),name ='select'),
    path('select/<int:pk>',Select.as_view(),name='sel'),
    path('reservation',ReservationTestView.as_view(),name='reservation'),
    path('reservation/<int:pk>',ReservationTest.as_view(),name='reser'),

    path('', views.index, name='index'),
    path('reserve_list', ReserveList.as_view(), name = 'reserve_list'),
    path('reserve_list/<int:pk>/', ReserveDetail.as_view(), name = 'reserve_detail'),
    path('reserve_list/<int:pk>/delete/', ReserveDelete.as_view(), name = 'delete'),
    path('fcl_add/',views.fcl, name = 'fcl'),
    
    path('Billing',BillingBase.as_view(),name='billbase'),
    path('Billing/<int:pk>/',BillingView.as_view(),name='billing'),
    path('PriceGuide',GuideView.as_view(),name='guide'),
  
    path('month/<int:pk>/<int:year>/<int:month>/', views.ReserveCalendar.as_view(), name='month'),
    path('reserve_calender', ReserveCalendar.as_view(), name = 'reserve_calender'),
    
    path('reserve_calender/<int:pk>/', ReserveCalendar.as_view(), name = 'reserve_calender'),
    path('date/<int:pk>/<int:year>-<int:month>-<int:date>/', views.ReserveList.as_view(), name='date'),
]
