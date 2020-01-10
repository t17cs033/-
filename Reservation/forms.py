from django import forms
from .models import Member

class MemberIdForm(forms.Form):
    cmpId = forms.IntegerField(label='ID')

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['cmpId','cmpName','address','tel','section','name','mail','pay']