from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Reservation.models import Reserve,Member
from django.views import generic
from . import Calender
from django.http.response import HttpResponseRedirect
from Reservation.forms import LoginningUser
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")

class ReserveList(ListView):
    model = Reserve
    
class ReserveDetal(DetailView):
    
    model = Reserve
    
class ReserveCalendar(Calender.MonthCalendarMixin, generic.ListView):
    """月間カレンダーを表示するビュー"""
    template_name = 'Reservation/reserve_calender.html'
    model = Reserve
    

    def post(self, request, *args, **kwargs):
        cmpId = self.request.POST.get('cmpId')
        member = get_object_or_404(Reserve, pk=cmpId)
        date = self.request.POST.get('date')
        number = self.request.POST.get('number')
        member.save()
        return HttpResponseRedirect(reverse('reserve_list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
       #$ cmpId = Reserve.objects.get(id = self.kwargs['pk'])
        context['pk'] = self.kwargs.get('pk')#html内でpkとして使える
        context.update(calendar_context)
        return context
    
   
