from django import forms
from Site.models import Calendar
from django.forms import ModelForm

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class MeetingTypeForm(ModelForm):
    class Meta:
        model = Calendar
        fields = ['Meeting_date', 'Meeting_type']
        widgets = {
            'Meeting_date': DateTimeInput(),
        }