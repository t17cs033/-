from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import MeetingRoom, Reserve
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Reservation.models import Reserve
from .forms import ReserveForm, ReserveTime, ReserveCmpIDForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")

class MRShowView(TemplateView):
    model = Reserve
    template_name = 'Reservation/mr_show.html'
        
class BigMRReservationView(CreateView):
    model = Reserve
    fields = ('cmpId', 'date', 'mrName')
    template_name = 'Reservation/mr_big_reservation.html'
    success_url = 'mrshow/'
  
    def post(self, request, *args, **kwargs):
        cmpId = self.request.POST.get('cmpId')
        start_time = self.request.POST.get('reserve_stime')
        end_time = self.request.POST.get('reserve_etime')
        
        reserve = get_object_or_404(Reserve, pk=cmpId)
        reserve.stime = start_time
        reserve.etime = end_time
        reserve.save()
        return HttpResponseRedirect(reverse('mrshow'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReserveForm()
        context['form_time'] = ReserveTime()
        return context
        
    
class BigMRReservationUpdateView(UpdateView):
    model = Reserve
    fields = ('cmpId', 'date', 'mrName')
    template_name = 'Reservation/mr_big_reservation.html'
    success_url = 'mrshow/'
    
    def post(self, request, *args, **kwargs):
        cmp_Id = self.request.POST.get('cmpId')
        res_date = self.request.POST.get('date')
        mr_Name = self.request.POST.get('mrName')
        start_time = self.request.POST.get('reserve_stime')
        end_time = self.request.POST.get('reserve_etime')
        
        reserve = get_object_or_404(Reserve, pk=cmp_Id)
        reserve.cmpId = cmp_Id
        reserve.date = res_date
        reserve.mrName = mr_Name
        reserve.stime = start_time
        reserve.etime = end_time
        reserve.save()
        return HttpResponseRedirect(reverse('mrshow'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReserveForm()
        context['form_time'] = ReserveTime()
        return context
    
class MiddleMRReservationView(CreateView):
    model = Reserve
    fields = ('cmpId', 'date', 'mrName', 'start_time', 'end_time')
    template_name = 'Reservation/mr_middle_reservation.html'    
    success_url = 'mrshow/'
    
    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['initial'] = {'mrName': "中会議室"}
        return form_kwargs
    
class SmallMRReservationView(CreateView):
    model = MeetingRoom
    template_name = 'Reservation/mr_small_reservation.html'
    
class ACornerReservationView(CreateView):
    model = MeetingRoom
    template_name = 'Reservation/corner_a_reservation.html'
    
class BCornerReservationView(CreateView):
    model = MeetingRoom
    template_name = 'Reservation/corner_b_reservation.html'
    
class ReserveList(ListView):
    model = Reserve
    
class ReserveDetal(DetailView):    
    model = Reserve
