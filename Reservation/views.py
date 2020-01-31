from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserve,Member
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Reservation.models import Reserve
from django.urls.base import reverse,reverse_lazy
from django.contrib import messages
from .forms import ReserveForm
import datetime
from django.views.generic.base import TemplateView
from Reservation.forms import MemberIdForm, MemberForm,LoginningUser
from django.views.generic.edit import UpdateView,DeleteView
from django.views import generic
from . import Calender
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Billing
from Reservation.models import MeetingRoom, Facility
from Reservation import forms
from django.db.models import Max, Sum
from token import STAR

class LoginView(TemplateView):
    template_name = 'Reservation/login.html'
    model = Member


    def post(self, request, *args, **kwargs):
        cmpId = self.request.POST.get('cmpId')
        #member = Member.objects.get(pk = cmpId)
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

class MRShowView(ListView):  #会議室一覧
    model = Reserve
    template_name = 'Reservation/mr_show.html'
    
    def get_context_data(self, **kwargs):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['pk'] = pk
        context['year'] = year
        context['month'] = month
        context['day'] = day
        context['date'] = date
        if Reserve.objects.filter(cmpId=pk, date=date).exists():
            total = Reserve.objects.filter(cmpId=pk, date=date).aggregate(Sum('charge'))
            context['total'] = int(total['charge__sum'])
            white = Reserve.objects.filter(cmpId=pk, date=date).aggregate(Sum('whiteboard'))
            context['whiteboard'] = int(white['whiteboard__sum'])
            pro = Reserve.objects.filter(cmpId=pk, date=date).aggregate(Sum('projector'))
            context['projector'] = int(pro['projector__sum'])
        else:
            context['total'] = 0 
            context['whiteboard'] = 0
            context['projector'] = 0          
        if Reserve.objects.filter(date=date).exists():
            w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
            w_sto = 10 - int(w_sum['whiteboard__sum'])
            p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
            p_sto = 5 - int(p_sum['projector__sum'])
            context['w_stock'] = w_sto
            context['p_stock'] = p_sto
        else:
            context['w_stock'] = 10
            context['p_stock'] = 5    
        return context

class BigMRReservationView(CreateView):  #大会議室
    model = Reserve
    form_class = ReserveForm
    template_name = 'Reservation/mr_big_reservation.html'    

    def get_form(self):
        form = super(BigMRReservationView, self).get_form()
        form.initial['mrName'] = '大会議室'
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        if Reserve.objects.filter(date=date).exists():        
            w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
            p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
            if int(w_sum['whiteboard__sum']) == 10:
                messages.info(self.request, '在庫切れ：ホワイトボード')
            if int(p_sum['projector__sum']) == 5:
                messages.info(self.request, '在庫切れ：プロジェクター')
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(cmpId=self.kwargs.get('pk'))
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')     
        return context 
    
    def form_valid(self, form):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        pk = self.kwargs.get('pk')
        mrName = self.request.POST.get('mrName')
        start_time = self.request.POST.get('start_time')
        end_time = self.request.POST.get('end_time')
        whiteboard = self.request.POST.get('whiteboard')
        projector = self.request.POST.get('projector')
        w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
        p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
        etime = datetime.datetime.strptime(end_time, '%H:%M:%S') 
        stime = datetime.datetime.strptime(start_time, '%H:%M:%S')
        time = etime-stime
        if etime < stime:
            messages.error(self.request, '時間を正しく設定してください')
            return super(BigMRReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date,mrName=mrName,start_time__lte=start_time,end_time__gt=start_time).exists():
            messages.error(self.request, 'すでに予約が入っています')
            return super(BigMRReservationView, self).form_invalid(form)  
        if start_time == '12:00:00':
            messages.error(self.request, '12時〜13時は使用できません')
            return super(BigMRReservationView, self).form_invalid(form)  
        if end_time == '13:00:00':
            messages.error(self.request, '12時〜13時は使用できません')
            return super(BigMRReservationView, self).form_invalid(form)
        if start_time < '12:00:00' and end_time > '13:00:00' and start_time != '9:00:00' and end_time != '16:00:00':
            messages.error(self.request, '12時〜13時は使用できません')
            return super(BigMRReservationView, self).form_invalid(form) 
        if int(projector) > 1:
            messages.error(self.request, 'プロジェクターは1日に1台しか借りることができません')
            return super(BigMRReservationView, self).form_invalid(form) 
        if Reserve.objects.filter(cmpId=pk, date=date, projector='1').exists() and int(projector) == 1:
            messages.error(self.request, 'プロジェクターをすでに1台借りています')
            return super(BigMRReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date).exists() and int(w_sum['whiteboard__sum'])+int(whiteboard) > 10:
            messages.error(self.request, 'ホワイトボードの在庫がありません')
            return super(BigMRReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date).exists() and int(p_sum['projector__sum'])+int(projector) > 5:
            messages.error(self.request, 'プロジェクターの在庫がありません')
            return super(BigMRReservationView, self).form_invalid(form)                       
        else:
            r_c = 0
            f_p = 2000 * int(projector)
            f_w = 1000 * int(whiteboard)
            reserve = form.save(commit=False)
            reserve.start_time = start_time 
            reserve.end_time = end_time
            if str(time) == '1:00:00':
                r_c=2000
            if str(time) == '2:00:00':
                r_c=4000
            if str(time) == '3:00:00':
                r_c=5000
            if str(time) == '7:00:00':
                r_c=9000 
            reserve.charge = r_c + f_p + f_w
            reserve.number = pk
            reserve.cmpId = pk
            reserve.date = date
            reserve.save()    
        return redirect('mrshow', pk=self.kwargs.get('pk'), year=self.kwargs.get('year'), month=self.kwargs.get('month'), day=self.kwargs.get('day'))   
   
    def get_success_url(self):
        return reverse('mrshow', kwargs={'pk':self.kwargs.get('pk'), 'year':self.kwargs.get('year'), 'month':self.kwargs.get('month'), 'day':self.kwargs.get('day')})

    
class MiddleMRReservationView(CreateView):  #中会議室
    model = Reserve
    form_class = ReserveForm
    template_name = 'Reservation/mr_middle_reservation.html' 
    
    def get_form(self):
        form = super(MiddleMRReservationView, self).get_form()
        form.initial['mrName'] = '中会議室'
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        if Reserve.objects.filter(date=date).exists():        
            w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
            p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
            if int(w_sum['whiteboard__sum']) == 10:
                messages.info(self.request, '在庫切れ：ホワイトボード')
            if int(p_sum['projector__sum']) == 5:
                messages.info(self.request, '在庫切れ：プロジェクター')
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(cmpId=self.kwargs.get('pk'))
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')
        context['start_time'] = self.request.POST.get('start_time')
        context['end_time'] = self.request.POST.get('end_time')
        return context

    def form_valid(self, form):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        pk = self.kwargs.get('pk')
        mrName = self.request.POST.get('mrName')
        whiteboard = self.request.POST.get('whiteboard')
        projector = self.request.POST.get('projector')
        start_time = self.request.POST.get('start_time')
        end_time = self.request.POST.get('end_time')
        w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
        p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
        etime = datetime.datetime.strptime(end_time, '%H:%M:%S') 
        stime = datetime.datetime.strptime(start_time, '%H:%M:%S')
        time = etime-stime
        if etime < stime:
            messages.error(self.request, '時間を正しく設定してください')
            return super(MiddleMRReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date,mrName=mrName,start_time__lte=start_time,end_time__gt=start_time).exists():
            messages.error(self.request, 'すでに予約が入っています')
            return super(MiddleMRReservationView, self).form_invalid(form)  
        if start_time == '12:00:00':
            messages.error(self.request, '12時〜13時は使用できません')
            return super(MiddleMRReservationView, self).form_invalid(form)  
        if end_time == '13:00:00':
            messages.error(self.request, '12時〜13時は使用できません')
            return super(MiddleMRReservationView, self).form_invalid(form)
        if start_time < '12:00:00' and end_time > '13:00:00' and start_time != '9:00:00' and end_time != '16:00:00':
            messages.error(self.request, '12時〜13時は使用できません')
            return super(MiddleMRReservationView, self).form_invalid(form)
        if int(projector) > 1:
            messages.error(self.request, 'プロジェクターは1日に1台しか借りることができません')
            return super(MiddleMRReservationView, self).form_invalid(form) 
        if Reserve.objects.filter(cmpId=pk, date=date, projector='1').exists() and int(projector) == 1:
            messages.error(self.request, 'プロジェクターをすでに1台借りています')
            return super(MiddleMRReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date).exists() and int(w_sum['whiteboard__sum'])+int(whiteboard) > 10:
            messages.error(self.request, 'ホワイトボードの在庫がありません')
            return super(MiddleMRReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date).exists() and int(p_sum['projector__sum'])+int(projector) > 5:
            messages.error(self.request, 'プロジェクターの在庫がありません')
            return super(MiddleMRReservationView, self).form_invalid(form)                                                                        
        else:   
            r_c = 0
            f_p = 2000 * int(projector)
            f_w = 1000 * int(whiteboard)  
            reserve = form.save(commit=False)
            reserve.start_time = start_time 
            reserve.end_time = end_time            
            if str(time) == '1:00:00':
                r_c=1500 
            if str(time) == '2:00:00':
                r_c=3000
            if str(time) == '3:00:00':
                r_c=4000
            if str(time) == '7:00:00':
                r_c=7500
            reserve.charge = r_c + f_p + f_w
            reserve.number = pk
            reserve.cmpId = pk
            reserve.date = date
            reserve.save()
        return redirect('mrshow', pk=self.kwargs.get('pk'), year=self.kwargs.get('year'), month=self.kwargs.get('month'), day=self.kwargs.get('day'))
    
    def form_invalid(self, form):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        mrName = self.request.POST.get('mrName')
        start_time = self.request.POST.get('start_time')
        end_time = self.request.POST.get('end_time')
        etime = datetime.datetime.strptime(end_time, '%H:%M:%S') 
        stime = datetime.datetime.strptime(start_time, '%H:%M:%S')
        if Reserve.objects.filter(date=date,mrName=mrName,start_time=start_time).exists():
            messages.error(self.request, 'すでに予約が入っています')
        if etime < stime:
            messages.error(self.request, '時間を正しく設定してください')                
        return super(MiddleMRReservationView, self).form_invalid(form)
   
    def get_success_url(self):
        return reverse('mrshow', kwargs={'pk':self.kwargs.get('pk'), 'year':self.kwargs.get('year'), 'month':self.kwargs.get('month'), 'day':self.kwargs.get('day')})
               
class SmallMRReservationView(CreateView):  #小会議室
    model = Reserve
    form_class = ReserveForm
    template_name = 'Reservation/mr_small_reservation.html'    

    def get_form(self):
        form = super(SmallMRReservationView, self).get_form()
        form.initial['mrName'] = '小会議室'
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        if Reserve.objects.filter(date=date).exists():        
            w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
            p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
            if int(w_sum['whiteboard__sum']) == 10:
                messages.info(self.request, '在庫切れ：ホワイトボード')
            if int(p_sum['projector__sum']) == 5:
                messages.info(self.request, '在庫切れ：プロジェクター')
        return form
   
    def form_valid(self, form):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        pk = self.kwargs.get('pk')
        mrName = self.request.POST.get('mrName')
        whiteboard = self.request.POST.get('whiteboard')
        projector = self.request.POST.get('projector')
        w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
        p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
        start_time = self.request.POST.get('start_time')
        end_time = self.request.POST.get('end_time')
        etime = datetime.datetime.strptime(end_time, '%H:%M:%S') 
        stime = datetime.datetime.strptime(start_time, '%H:%M:%S')
        time = etime-stime
        if etime < stime:
            messages.error(self.request, '時間を正しく設定してください')
            return super(SmallMRReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date,mrName=mrName,start_time__lte=start_time,end_time__gt=start_time).exists():
            messages.error(self.request, 'すでに予約が入っています')
            return super(SmallMRReservationView, self).form_invalid(form)  
        if start_time == '12:00:00':
            messages.error(self.request, '12時〜13時は使用できません')
            return super(SmallMRReservationView, self).form_invalid(form)
        if end_time == '13:00:00':
            messages.error(self.request, '12時〜13時は使用できません')
            return super(SmallMRReservationView, self).form_invalid(form) 
        if start_time < '12:00:00' and end_time > '13:00:00' and start_time != '9:00:00' and end_time != '16:00:00':
            messages.error(self.request, '12時〜13時は使用できません')
            return super(SmallMRReservationView, self).form_invalid(form) 
        if int(projector) > 1:
            messages.error(self.request, 'プロジェクターは1日に1台しか借りることができません')
            return super(SmallMRReservationView, self).form_invalid(form) 
        if Reserve.objects.filter(cmpId=pk, date=date, projector='1').exists() and int(projector) == 1:
            messages.error(self.request, 'プロジェクターをすでに1台借りています')
            return super(SmallMRReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date).exists() and int(w_sum['whiteboard__sum'])+int(whiteboard) > 10:
            messages.error(self.request, 'ホワイトボードの在庫がありません')
            return super(SmallMRReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date).exists() and int(p_sum['projector__sum'])+int(projector) > 5:
            messages.error(self.request, 'プロジェクターの在庫がありません')
            return super(SmallMRReservationView, self).form_invalid(form)              
        else:
            r_c = 0
            f_p = 2000 * int(projector)
            f_w = 1000 * int(whiteboard)
            reserve = form.save(commit=False)
            reserve.start_time = start_time 
            reserve.end_time = end_time 
            if str(time) == '1:00:00':
                r_c=1000 
            if str(time) == '2:00:00':
                r_c= 2000
            if str(time) == '3:00:00':
                r_c= 2500
            if str(time) == '7:00:00':
                r_c= 4000
            reserve.charge = r_c + f_p + f_w
            reserve.number = pk
            reserve.cmpId = pk
            reserve.date = date
            reserve.save()    
        return redirect('mrshow', pk=self.kwargs.get('pk'), year=self.kwargs.get('year'), month=self.kwargs.get('month'), day=self.kwargs.get('day'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(cmpId=self.kwargs.get('pk'))
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')
        return context    
   
    def get_success_url(self):
        return reverse('mrshow', kwargs={'pk':self.kwargs.get('pk'), 'year':self.kwargs.get('year'), 'month':self.kwargs.get('month'), 'day':self.kwargs.get('day')})

    
class ACornerReservationView(CreateView):  #コーナーA
    model = Reserve
    form_class = ReserveForm
    template_name = 'Reservation/corner_a_reservation.html'    

    def get_form(self):
        form = super(ACornerReservationView, self).get_form()
        form.initial['mrName'] = 'コーナーA'
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        if Reserve.objects.filter(date=date).exists():        
            w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
            p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
            if int(w_sum['whiteboard__sum']) == 10:
                messages.info(self.request, '在庫切れ：ホワイトボード')
            if int(p_sum['projector__sum']) == 5:
                messages.info(self.request, '在庫切れ：プロジェクター')    
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(cmpId=self.kwargs.get('pk'))
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')     
        return context    

    def form_valid(self, form):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        pk = self.kwargs.get('pk')
        mrName = self.request.POST.get('mrName')
        whiteboard = self.request.POST.get('whiteboard')
        projector = self.request.POST.get('projector')
        w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
        p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
        start_time = self.request.POST.get('start_time')
        end_time = self.request.POST.get('end_time')
        etime = datetime.datetime.strptime(end_time, '%H:%M:%S') 
        stime = datetime.datetime.strptime(start_time, '%H:%M:%S')
        time = etime-stime
        if etime < stime:
            messages.error(self.request, '時間を正しく設定してください')
            return super(ACornerReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date,mrName=mrName,start_time__lte=start_time,end_time__gt=start_time).exists():
            messages.error(self.request, 'すでに予約が入っています')
            return super(ACornerReservationView, self).form_invalid(form)
        if str(time) > '2:00:00' and start_time <= '12:00:00' and end_time >= '13:00:00' and (start_time != '9:00:00' or end_time != '16:00:00'):
            messages.error(self.request, '半日貸しは9:00〜12:00、13:00〜16:00です')
            messages.error(self.request, '1時間貸しは連続2時間までです')
            return super(ACornerReservationView, self).form_invalid(form)             
        if int(projector) > 1:
            messages.error(self.request, 'プロジェクターは1日に1台しか借りることができません')
            return super(ACornerReservationView, self).form_invalid(form) 
        if Reserve.objects.filter(cmpId=pk, date=date, projector='1').exists() and int(projector) == 1:
            messages.error(self.request, 'プロジェクターをすでに1台借りています')
            return super(ACornerReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date).exists() and int(w_sum['whiteboard__sum'])+int(whiteboard) > 10:
            messages.error(self.request, 'ホワイトボードの在庫がありません')
            return super(ACornerReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date).exists() and int(p_sum['projector__sum'])+int(projector) > 5:
            messages.error(self.request, 'プロジェクターの在庫がありません')
            return super(ACornerReservationView, self).form_invalid(form)  
        else:
            r_c = 0
            f_p = 2000 * int(projector)
            f_w = 1000 * int(whiteboard)
            reserve = form.save(commit=False)
            reserve.start_time = start_time 
            reserve.end_time = end_time
            if str(time) == '1:00:00':
                r_c= 500 
            if str(time) == '2:00:00':
                r_c = 1000
            if str(time) == '3:00:00':
                r_c = 1500
            if str(time) == '7:00:00':
                r_c = 2500 
            reserve.charge = r_c + f_p + f_w
            reserve.number = pk
            reserve.cmpId = pk
            reserve.date = date
            reserve.save()    
        return redirect('mrshow', pk=self.kwargs.get('pk'), year=self.kwargs.get('year'), month=self.kwargs.get('month'), day=self.kwargs.get('day'))
   
    def get_success_url(self):
        return reverse('mrshow', kwargs={'pk':self.kwargs.get('pk'), 'year':self.kwargs.get('year'), 'month':self.kwargs.get('month'), 'day':self.kwargs.get('day')})

    
class BCornerReservationView(CreateView):  #コーナーB
    model = Reserve
    form_class = ReserveForm
    template_name = 'Reservation/corner_b_reservation.html'    

    def get_form(self):
        form = super(BCornerReservationView, self).get_form()
        form.initial['mrName'] = 'コーナーB'
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        if Reserve.objects.filter(date=date).exists():        
            w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
            p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
            if int(w_sum['whiteboard__sum']) == 10:
                messages.info(self.request, '在庫切れ：ホワイトボード')
            if int(p_sum['projector__sum']) == 5:
                messages.info(self.request, '在庫切れ：プロジェクター')   
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member'] = Member.objects.get(cmpId=self.kwargs.get('pk'))
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['pk'] = self.kwargs.get('pk')     
        return context    

    def form_valid(self, form):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        date = datetime.date(year=year, month=month, day=day)
        pk = self.kwargs.get('pk')
        mrName = self.request.POST.get('mrName')
        whiteboard = self.request.POST.get('whiteboard')
        projector = self.request.POST.get('projector')
        w_sum = Reserve.objects.filter(date=date).aggregate(Sum('whiteboard'))
        p_sum = Reserve.objects.filter(date=date).aggregate(Sum('projector'))
        start_time = self.request.POST.get('start_time')
        end_time = self.request.POST.get('end_time')
        etime = datetime.datetime.strptime(end_time, '%H:%M:%S') 
        stime = datetime.datetime.strptime(start_time, '%H:%M:%S')
        time = etime-stime
        if etime < stime:
            messages.error(self.request, '時間を正しく設定してください')
            return super(BCornerReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date,mrName=mrName,start_time__lte=start_time,end_time__gt=start_time).exists():
            messages.error(self.request, 'すでに予約が入っています')
            return super(BCornerReservationView, self).form_invalid(form)
        if str(time) > '2:00:00' and start_time <= '12:00:00' and end_time >= '13:00:00' and (start_time != '9:00:00' or end_time != '16:00:00'):
            messages.error(self.request, '半日貸しは9:00〜12:00、13:00〜16:00です')
            messages.error(self.request, '1時間貸しは連続2時間までです')
            return super(BCornerReservationView, self).form_invalid(form)   
        if int(projector) > 1:
            messages.error(self.request, 'プロジェクターは1日に1台しか借りることができません')
            return super(BCornerReservationView, self).form_invalid(form) 
        if Reserve.objects.filter(cmpId=pk, date=date, projector='1').exists() and int(projector) == 1:
            messages.error(self.request, 'プロジェクターをすでに1台借りています')
            return super(BCornerReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date).exists() and int(w_sum['whiteboard__sum'])+int(whiteboard) > 10:
            messages.error(self.request, 'ホワイトボードの在庫がありません')
            return super(BCornerReservationView, self).form_invalid(form)
        if Reserve.objects.filter(date=date).exists() and int(p_sum['projector__sum'])+int(projector) > 5:
            messages.error(self.request, 'プロジェクターの在庫がありません')
            return super(BCornerReservationView, self).form_invalid(form) 
        else:
            r_c = 0
            f_p = 2000 * int(projector)
            f_w = 1000 * int(whiteboard)
            reserve = form.save(commit=False)
            reserve.start_time = start_time 
            reserve.end_time = end_time
            if str(time) == '1:00:00':
                r_c = 500 
            if str(time) == '2:00:00':
                r_c = 1000
            if str(time) == '3:00:00':
                r_c = 1500
            if str(time) == '7:00:00':
                r_c = 2500 
            reserve.charge = r_c + f_p + f_w
            reserve.number = pk
            reserve.cmpId = pk
            reserve.date = date
            reserve.save()    
        return redirect('mrshow', pk=self.kwargs.get('pk'), year=self.kwargs.get('year'), month=self.kwargs.get('month'), day=self.kwargs.get('day'))
   
    def get_success_url(self):
        return reverse('mrshow', kwargs={'pk':self.kwargs.get('pk'), 'year':self.kwargs.get('year'), 'month':self.kwargs.get('month'), 'day':self.kwargs.get('day')})

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