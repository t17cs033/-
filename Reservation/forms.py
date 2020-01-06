from django import forms
from .models import MeetingRoom, Reserve

class ReserveTime(forms.Form):
    stime = (
        (0,'9:00'),
        (1,'10:00'),
        (2,'11:00'),
        (3,'12:00'),
        (4,'13:00'),
        (5,'14:00'),
        (6,'15:00'),
        )
    
    etime = (
        (7,'10:00'),
        (8,'11:00'),
        (9,'12:00'),
        (10,'13:00'),
        (11,'14:00'),
        (12,'15:00'),
        (13,'16:00'),
        )
    
    reserve_stime = forms.ChoiceField(label='開始時間',widget=forms.Select,choices=stime)
    reserve_etime = forms.ChoiceField(label='終了時間',widget=forms.Select,choices=etime)
    
class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['cmpId', 'date', 'mrName']