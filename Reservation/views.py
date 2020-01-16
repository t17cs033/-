from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Billing
from django.views.generic.list import ListView
from Reservation.models import MeetingRoom, Facility
from Reservation.models import Reserve

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")
class BillingBase(ListView):
    model = Billing
    template_name = "Reservation/BillBase.html"
    
class BillingView(DetailView):
    model = Billing
    template_name = "Reservation/Billing.html"
    
class GuideView(ListView):
    model = MeetingRoom
    template_name = "Reservation/Guide.html"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                'fcl_list' : Facility.objects.order_by('fclName'),
                'extra' : Facility.objects.all(),
            }
        )
        return ctx
    
class ReserveList(ListView):
    model = Reserve
    
class ReserveDetal(DetailView):
    
    model = Reserve
