from django import forms
from .models import MeetingRoom, Reserve
import datetime as dt

SHOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(9,16)]
EHOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(10,17)]
 
class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['number', 'cmpId', 'date', 'mrName', 'start_time', 'end_time']
        widgets = {'start_time': forms.Select(choices=SHOUR_CHOICES), 'end_time': forms.Select(choices=EHOUR_CHOICES)}
                