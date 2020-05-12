from django.forms import ModelForm
from .models import TransportBooking
from django import forms
class DateInput(forms.DateInput):
    input_type='date'

class TransportBookingForm(ModelForm):
    class Meta:
        model=TransportBooking
        fields='__all__'
        exclude=('transport',)
        #widgets = { 'startdate': DateInput(),'transport': forms.HiddenInput() }
        widgets = { 'startdate': DateInput(),'transport': forms.HiddenInput() }