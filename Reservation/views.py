from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Reserve
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Reservation.models import Reserve
from django.urls.base import reverse
from django.contrib import messages
from .forms import ReserveForm
import datetime

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")

class MRShowView(ListView):
    model = Reserve
    template_name = 'Reservation/mr_show.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')     
        return context

class BigMRReservationView(CreateView):
    model = Reserve
    form_class = ReserveForm
    template_name = 'Reservation/mr_big_reservation.html'    

    def get_form(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        cmpId = self.kwargs.get('pk')
        form = super(BigMRReservationView, self).get_form()
        form.initial['mrName'] = '大会議室'
        form.initial['number'] = cmpId
        form.initial['cmpId'] = cmpId
        form.initial['date'] = date       
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')     
        return context    
   
    def get_success_url(self):
        return reverse('Reservation:mrshow', kwargs={'pk':self.kwargs.get('pk'), 'year':self.kwargs.get('year'), 'month':self.kwargs.get('month'), 'day':self.kwargs.get('day')})

    
class MiddleMRReservationView(CreateView):
    model = Reserve
    form_class = ReserveForm
    template_name = 'Reservation/mr_middle_reservation.html' 
    
    def get_form(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        cmpId = self.kwargs.get('pk')
        form = super(MiddleMRReservationView, self).get_form()
        form.initial['mrName'] = '中会議室'
        form.initial['number'] = cmpId
        form.initial['cmpId'] = cmpId
        form.initial['date'] = date       
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')     
        return context    
   
    def get_success_url(self):
        return reverse('Reservation:mrshow', kwargs={'pk':self.kwargs.get('pk'), 'year':self.kwargs.get('year'), 'month':self.kwargs.get('month'), 'day':self.kwargs.get('day')})
               
class SmallMRReservationView(CreateView):
    model = Reserve
    form_class = ReserveForm
    template_name = 'Reservation/mr_small_reservation.html'    

    def get_form(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        cmpId = self.kwargs.get('pk')
        form = super(SmallMRReservationView, self).get_form()
        form.initial['mrName'] = '小会議室'
        form.initial['number'] = cmpId
        form.initial['cmpId'] = cmpId
        form.initial['date'] = date       
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')     
        return context    
   
    def get_success_url(self):
        return reverse('Reservation:mrshow', kwargs={'pk':self.kwargs.get('pk'), 'year':self.kwargs.get('year'), 'month':self.kwargs.get('month'), 'day':self.kwargs.get('day')})

    
class ACornerReservationView(CreateView):
    model = Reserve
    form_class = ReserveForm
    template_name = 'Reservation/corner_a_reservation.html'    

    def get_form(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        cmpId = self.kwargs.get('pk')
        form = super(ACornerReservationView, self).get_form()
        form.initial['mrName'] = 'コーナーA'
        form.initial['number'] = cmpId
        form.initial['cmpId'] = cmpId
        form.initial['date'] = date       
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')     
        return context    
   
    def get_success_url(self):
        return reverse('Reservation:mrshow', kwargs={'pk':self.kwargs.get('pk'), 'year':self.kwargs.get('year'), 'month':self.kwargs.get('month'), 'day':self.kwargs.get('day')})

    
class BCornerReservationView(CreateView):
    model = Reserve
    form_class = ReserveForm
    template_name = 'Reservation/corner_b_reservation.html'    

    def get_form(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        cmpId = self.kwargs.get('pk')
        form = super(BCornerReservationView, self).get_form()
        form.initial['mrName'] = 'コーナーB'
        form.initial['number'] = cmpId
        form.initial['cmpId'] = cmpId
        form.initial['date'] = date       
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')     
        return context    
   
    def get_success_url(self):
        return reverse('Reservation:mrshow', kwargs={'pk':self.kwargs.get('pk'), 'year':self.kwargs.get('year'), 'month':self.kwargs.get('month'), 'day':self.kwargs.get('day')})

    
class ReserveList(ListView):
    model = Reserve
    
class ReserveDetal(DetailView):    
    model = Reserve
