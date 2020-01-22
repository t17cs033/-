from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Reserve
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Reservation.models import Reserve, Member
from django.urls.base import reverse_lazy, reverse
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .forms import ReserveTime
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
    fields = ('number', 'cmpId', 'date', 'mrName', 'start_time', 'end_time')
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
    fields = ('number', 'cmpId', 'date', 'mrName', 'start_time', 'end_time')
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

'''
    def form_valid(self, form, request, *args, **kwargs):
        cmpId = self.kwargs.get('pk')
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        start_time = self.request.POST.get('start_time')
        end_time = self.request.POST.get('end_time')
        time = end_time - start_time
        if Reserve.objects.filter(date=date, start_time=start_time, end_time=end_time).exists():
            messages.error(self.request, 'すでに予約が入っています')
        else:
            reserve = form.save(commit=False)
            reserve.cmpId = cmpId
            reserve.date = date
            reserve.start_time = start_time
            reserve.end_time = end_time 
            if time == '7':
                reserve.charge = '1500'
            if time == '8':
                reserve.charge = '3000'
            if time == '9':
                reserve.charge = '4000'
            if time == '13':
                reserve.charge = '7500'
            reserve.save()        
        return redirect('mrbig:mrshow', pk=cmpId, year=year, month=month, day=day)
'''
               
class SmallMRReservationView(CreateView):
    model = Reserve
    fields = ('number', 'cmpId', 'date', 'mrName', 'start_time', 'end_time')
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
    fields = ('number', 'cmpId', 'date', 'mrName', 'start_time', 'end_time')
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
    fields = ('number', 'cmpId', 'date', 'mrName', 'start_time', 'end_time')
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
