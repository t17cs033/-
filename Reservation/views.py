from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Reservation.models import Reserve

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")

class ReserveList(ListView):
    model = Reserve
    
class ReserveDetal(DetailView):
    
    model = Reserve