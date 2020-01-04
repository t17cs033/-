from django.urls import path
from .views import LoginView,SelectView,Select
from Reservation.views import BillingTestView, BillingTest

appname = 'Reservation'
urlpatterns = [
    path('login',LoginView.as_view(),name='login'),
    path('select',SelectView.as_view(),name ='select'),
    path('select/<int:pk>',Select.as_view(),name='sel'),
    path('billing',BillingTestView.as_view(),name ='billing'),
    path('billing/<int:pk>',BillingTest.as_view(),name='t_b'),
]