from django import forms
from .models import MeetingRoom, Reserve

class MeetingRoomForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        fields = ['mrName', 'avail', 'timeCharge', 'halfCharge', 'dayCharge']


class MRChargeForm(forms.Form):
    timeCharge = forms.BooleanField
    halfCharge = forms.BooleanField
    dayCharge = forms.BooleanField
"""    
class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['date', 'start_time', 'end_time', 'mrName']
        """
