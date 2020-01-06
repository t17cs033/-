from django.shortcuts import render
from django.http import HttpResponse
from Reservation.models import MeetingRoom
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Reservation.models import Reserve
from .forms import MeetingRoomForm, MRChargeForm
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")

class MRShowView(TemplateView):
    model = MeetingRoom
    template_name = 'Reservation/mr_show.html'
    
class BigMRReservationView(CreateView):
    model = MeetingRoom
    fields = ('mrName', 'avail', 'timeCharge', 'halfCharge', 'dayCharge')
    template_name = 'Reservation/mr_big_reservation.html'
                
class MiddleMRReservationView(CreateView):
    model = MeetingRoom
    template_name = 'Reservation/mr_middle_reservation.html'
    
class SmallMRReservationView(CreateView):
    model = MeetingRoom
    template_name = 'Reservation/mr_small_reservation.html'
    
class ACornerReservationView(CreateView):
    model = MeetingRoom
    template_name = 'Reservation/corner_a_reservation.html'
    
class BCornerReservationView(CreateView):
    model = MeetingRoom
    template_name = 'Reservation/corner_b_reservation.html'
    
class ReserveTime(CreateView):
    model = Reserve

class ReserveList(ListView):
    model = Reserve
    
class ReserveDetal(DetailView):    
    model = Reserve
