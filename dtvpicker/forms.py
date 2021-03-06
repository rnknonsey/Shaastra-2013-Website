from django import forms
from models import SubEvent
from django.forms import ModelForm

class SubEventForm(ModelForm):
    class Meta:
        model = SubEvent
        fields = ('title', 'start_date_and_time', 'end_date_and_time', 'venue', 'event', )
        widgets = {
            'event' : forms.HiddenInput(),
        }
        
class EventUnlockForm(forms.Form):
    unlock_reason = forms.CharField(max_length = 1024, help_text = 'Please give reason for unlocking.')
