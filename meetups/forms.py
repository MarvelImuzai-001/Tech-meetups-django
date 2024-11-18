from django import forms
from .models import Participant
class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Enter your email:")
    