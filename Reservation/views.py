from django.shortcuts import render
from django.http import HttpResponse
from .models import MeetingRoom, Reserve
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")

class MRShowView(TemplateView):
    model = MeetingRoom
    template_name = 'Reservation/mr_show.html'
    
class BigMRReservationView(CreateView):
    model = MeetingRoom
    fiels = ('mrName')
    template_name = 'Reservation/mr_big_reservation.html'
    
class MiddleMRReservationView(TemplateView):
    model = MeetingRoom
    template_name = 'Reservation/mr_middle_reservation.html'
    
class SmallMRReservationView(TemplateView):
    model = MeetingRoom
    template_name = 'Reservation/mr_small_reservation.html'
    
class ACornerReservationView(TemplateView):
    model = MeetingRoom
    template_name = 'Reservation/corner_a_reservation.html'
    
class BCornerReservationView(TemplateView):
    model = MeetingRoom
    template_name = 'Reservation/corner_b_reservation.html'