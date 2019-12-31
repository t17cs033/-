from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Billing
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")



class BillingBase(ListView):
    model = Billing
    template_name = "Reservation/BillBase.html"
    
class BillingView(DetailView):
    model = Billing
    template_name = "Reservation/Billing.html"
