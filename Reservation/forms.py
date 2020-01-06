from django import forms
from .models import MeetingRoom, Reserve

class ReserveTime(forms.Form):
    time = (
        (0,'9:00〜10:00'),
        (1,'10:00〜11:00'),
        (2,'11:00〜12:00'),
        (3,'12:00〜13:00'),
        (4,'13:00〜14:00'),
        (5,'14:00〜15:00'),
        (6,'15:00〜16:00'),
        )
    
    reserve_time = forms.ChoiceField(label='time',widget=forms.Select,choices=time)
    
class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['date', 'start_time', 'end_time', 'mrName']

    
