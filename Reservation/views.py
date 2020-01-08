from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Reservation.models import Reserve
from django.template.context_processors import request
from Reservation import models
from django.http.response import HttpResponseRedirect
from audioop import reverse
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.messages.api import success
from django.urls.base import reverse_lazy
from django.db.models.query import QuerySet

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")


class ReserveDelete(DeleteView):
    model = Reserve
    success_url = reverse_lazy('reserve_list')
    
class ReserveList(ListView):
    queryset = Reserve.objects.filter(cmpId = 1)
    
class ReserveDetail(DetailView):
    model = Reserve
    


    
    