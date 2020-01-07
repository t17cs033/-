from django.urls import path
from Reservation.views import LoginView,SelectView,Select,BillingTestView, BillingTest, ReservationTestView,ReservationTest

appname = 'Reservation'
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('select',SelectView.as_view(),name ='select'),
    path('select/<int:pk>',Select.as_view(),name='sel'),
    path('billing',BillingTestView.as_view(),name ='billing'),
    path('billing/<int:pk>',BillingTest.as_view(),name='t_b'),
    path('reservation',ReservationTestView.as_view(),name='reservation'),
    path('reservation/<int:pk>',ReservationTest.as_view(),name='reser'),
]