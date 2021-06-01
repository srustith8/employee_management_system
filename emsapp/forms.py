from django import forms
from .models import Leave

class Leaveform(forms.ModelForm):
    class Meta:
        model = Leave
        exclude  = ('accepted',)