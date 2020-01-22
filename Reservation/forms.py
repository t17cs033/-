from django import forms
from .models import Member

from Reservation.models import Member,Reserve
from django.contrib.contenttypes import fields

class LoginningUser(forms.Form):
    class Meta:
        model = Reserve
        fields = ['date','number','cmpId']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class FclForm(forms.Form):
    fcl_a = forms.IntegerField(
        label = 'ホワイトボード',
        min_value = 0,
        max_value = 10,
        required = True,
        )
    
    fcl_b = forms.IntegerField(
        label = 'プロジェクタ',
        min_value = 0,
        max_value = 1,
        required = True,
        )

class MemberIdForm(forms.Form):
    cmpId = forms.IntegerField(label='ID')

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['cmpId','cmpName','address','tel','section','name','mail','pay']

