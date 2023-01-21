from django import forms
from .models import Logger

SHIFT = (
    ('1', 'Morning'),
    ('2', 'Afternoon'),
    ('3', 'Evening'),
)

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices = SHIFT)
    time_log = forms.TimeField()

class LoggerForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'