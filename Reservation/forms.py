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
