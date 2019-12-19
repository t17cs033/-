from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Billing

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. ")


class BillingView(TemplateView):
    model = Billing
    template_name = 'Reservation/Billing.html'
    
    def post(self,request,*arg,**kwargs):
        billing_id = self.request.POST.get('billing_id')
        billing = Billing.objects.get(pk=billing_id)
        context = super().get_context_data(**kwargs)
        context['billing'] = billing
        return self.render_to_response(context)
    