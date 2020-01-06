from django.shortcuts import render
from .models import Member
from django.views.generic.base import TemplateView
from Reservation.forms import MemberIdForm, MemberForm
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.http.response import HttpResponseRedirect
from audioop import reverse
from django.views.generic.edit import UpdateView

# Create your views here.

class LoginView(TemplateView):
    template_name = 'Reservation/login.html'
    model = Member

    def post(self, request, *args, **kwargs):
        cmpId = self.request.POST.get('cmpId')
        member = Member.objects.get(pk = cmpId)
        context = super().get_context_data(**kwargs)
        context['form_id'] = MemberIdForm()
        context['member'] = member
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_id'] = MemberIdForm()
        return context


class SelectView(TemplateView):
    model = Member
    template_name = 'Reservation/select.html'

    def post(self,request,*args,**kwargs):
        cmpId =self.request.POST.get('cmpId')
        context = super().get_context_data(**kwargs)
        context['member'] = MemberForm()
        return self.render_to_response(context)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form_id'] = MemberIdForm(initial ={'cmpId':self.kwargs.get('pk')})
        context['form'] = MemberForm()
        return context

class Select(UpdateView):
    model = Member
    template_name = 'Reservation/select.html'
    fields = ('cmpId','cmpName','address','tel','section','name','mail','pay')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_id']=MemberIdForm(initial ={'cmpId':self.kwargs.get('pk')})
        return context

class BillingTestView(TemplateView):
    model = Member
    template_name = 'Reservation/test_billing.html'

    def post(self,request,*args,**kwargs):
        cmpId =self.request.POST.get('cmpId')
        context = super().get_context_data(**kwargs)
        context['member'] = MemberForm()
        return self.render_to_response(context)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form_id'] = MemberIdForm(initial ={'cmpId':self.kwargs.get('pk')})
        context['form'] = MemberForm()
        return context

class BillingTest(UpdateView):
    model = Member
    template_name = 'Reservation/test_billing.html'
    fields = ('cmpId','cmpName','address','tel','section','name','mail','pay')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_id']=MemberIdForm(initial ={'cmpId':self.kwargs.get('pk')})
        return context

class ReservationTestView(TemplateView):
    model = Member
    template_name = 'Reservation/test_reservation.html'

    def post(self,request,*args,**kwargs):
        cmpId =self.request.POST.get('cmpId')
        context = super().get_context_data(**kwargs)
        context['member'] = MemberForm()
        return self.render_to_response(context)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form_id'] = MemberIdForm(initial ={'cmpId':self.kwargs.get('pk')})
        context['form'] = MemberForm()
        return context

class ReservationTest(UpdateView):
    model = Member
    template_name = 'Reservation/test_reservation.html'
    fields = ('cmpId','cmpName','address','tel','section','name','mail','pay')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_id']=MemberIdForm(initial ={'cmpId':self.kwargs.get('pk')})
        return context