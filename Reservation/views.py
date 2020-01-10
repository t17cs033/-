from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Reservation.models import Reserve
from django.views.generic.edit import DeleteView
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.template.context_processors import request
from django.shortcuts import render
from . import forms

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
    
def fcl(request):
    form = forms.FclForm(request.POST)
    if form.is_valid():
        message = "成功しました"
    else:
        message = "失敗しました"
    d = {
        'form' : form,
        }
    return render(request, 'Reservation/fcl_add.html', d)
        
        

    
    