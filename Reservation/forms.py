from django import forms
from .models import MeetingRoom

class MeetingRoom(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        fields = ['mrName', 'avail', 'charge']
