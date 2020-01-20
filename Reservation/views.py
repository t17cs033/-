from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Reserve
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Reservation.models import Reserve
from django.urls.base import reverse_lazy, reverse
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")

class MRShowView(ListView):
    model = Reserve
    template_name = 'Reservation/mr_show.html'


class BigMRReservationView(CreateView):
    model = Reserve
    fields = ('number', 'cmpId', 'date', 'mrName', 'start_time', 'end_time')
    template_name = 'Reservation/mr_big_reservation.html'    
    success_url = reverse_lazy('mrshow')

    def get_form(self):
        form = super(BigMRReservationView, self).get_form()
        form.fields['number'].label = '予約番号'
        form.fields['cmpId'].label = '企業ID'
        form.fields['date'].label = '日付'
        form.fields['mrName'].label = '会議室名'
        form.fields['start_time'].label = '開始時間'
        form.fields['end_time'].label = '終了時間'
        form.initial['mrName'] = '大会議室'
        return form
    
class MiddleMRReservationView(CreateView):
    model = Reserve
    fields = ('number', 'mrName', 'start_time', 'end_time')
    template_name = 'Reservation/mr_middle_reservation.html'    
    
    def get_form(self):
        form = super(MiddleMRReservationView, self).get_form()
        form.initial['mrName'] = '中会議室'
        form.initial['number'] = {'cmpId'}
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['cmpId'] = get_object_or_404(Reserve, pk=self.kwargs['pk'])
        context['pk'] = self.kwargs.get('pk')
        return context
    
    def form_valid(self, form):
        cmpId = self.kwargs.get('cmpId')
        date = self.kwargs.get('date')
        mrName = self.kwargs.get('mrName')
        start_time = self.kwargs.get('start_time')
        end_time = self.kwargs.get('end_time')
        if Reserve.objects.filter(date=date, mrName=mrName, start_time=start_time, end_time=end_time):
            messages.error(self.request, 'すでに予約が入っています')
        else:
            reserve = form.save(commit=False)
            reserve.cmpId = cmpId
            reserve.date = date
            reserve.save()        
        return redirect('mrbig:mrshow', pk=cmpId.pk, date=date)
               
class SmallMRReservationView(CreateView):
    model = Reserve
    fields = ('number', 'cmpId', 'date', 'mrName', 'start_time', 'end_time')
    template_name = 'Reservation/mr_small_reservation.html'    
    success_url = reverse_lazy('mrshow')

    def get_form(self):
        form = super(SmallMRReservationView, self).get_form()
        form.fields['number'].label = '予約番号'
        form.fields['cmpId'].label = '企業ID'
        form.fields['date'].label = '日付'
        form.fields['mrName'].label = '会議室名'
        form.fields['start_time'].label = '開始時間'
        form.fields['end_time'].label = '終了時間'
        form.initial['mrName'] = '小会議室'
        return form
    
class ACornerReservationView(CreateView):
    model = Reserve
    fields = ('number', 'cmpId', 'date', 'mrName', 'start_time', 'end_time')
    template_name = 'Reservation/corner_a_reservation.html'    
    success_url = reverse_lazy('mrshow')

    def get_form(self):
        form = super(ACornerReservationView, self).get_form()
        form.fields['number'].label = '予約番号'
        form.fields['cmpId'].label = '企業ID'
        form.fields['date'].label = '日付'
        form.fields['mrName'].label = '会議室名'
        form.fields['start_time'].label = '開始時間'
        form.fields['end_time'].label = '終了時間'
        form.initial['mrName'] = 'コーナーA'
        return form
    
class BCornerReservationView(CreateView):
    model = Reserve
    fields = ('number', 'cmpId', 'date', 'mrName', 'start_time', 'end_time')
    template_name = 'Reservation/corner_b_reservation.html'    
    success_url = reverse_lazy('mrshow')

    def get_form(self):
        form = super(BCornerReservationView, self).get_form()
        form.fields['number'].label = '予約番号'
        form.fields['cmpId'].label = '企業ID'
        form.fields['date'].label = '日付'
        form.fields['mrName'].label = '会議室名'
        form.fields['start_time'].label = '開始時間'
        form.fields['end_time'].label = '終了時間'
        form.initial['mrName'] = 'コーナーB'
        return form
    
class ReserveList(ListView):
    model = Reserve
    
class ReserveDetal(DetailView):    
    model = Reserve
