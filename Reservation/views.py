from django.shortcuts import render
from django.http import HttpResponse
from Reservation.models import Reserve,Member
from django.views.generic.base import TemplateView
from Reservation.forms import MemberIdForm, MemberForm,LoginningUser
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import generic
from . import Calender
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Billing
from Reservation.models import MeetingRoom, Facility
from django.urls.base import reverse_lazy
from . import forms

class LoginView(TemplateView):
    template_name = 'Reservation/login.html'
    model = Member


    def post(self, request, *args, **kwargs):
        cmpId = self.request.POST.get('cmpId')
        member =get_object_or_404(Member, pk=cmpId)
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
        context['form_id'] = MemberIdForm()
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
    
def index(request):
    return HttpResponse("Hello, world. ")

class BillingBase(ListView):
    model = Billing
    template_name = "Reservation/BillBase.html"
    
class BillingView(DetailView):
    model = Billing
    template_name = "Reservation/Billing.html"
    
    
    
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
    
class ReserveDelete(DeleteView):
    model = Reserve
    success_url = reverse_lazy('reserve_list')
   
class ReserveList(ListView):
    queryset = Reserve.objects.filter(cmpId = 1)
    model = Reserve
    
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

