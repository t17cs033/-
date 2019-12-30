from django.urls import path
from .views import LoginView,SelectView,Select

app_name = 'Reservation'
urlpatterns = [
    path('login',LoginView.as_view(),name='login'),
    path('select',SelectView.as_view(),name ='select'),
    path('<int:pk>/select',Select.as_view(),name='sel'),
]