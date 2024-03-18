
from django import forms

class RSVPForm(forms.Form):
    attending = forms.BooleanField(label='Attending', required=False)
