from django import forms
from django.conf import settings


class CreateTicketForm(forms.Form):
    title = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea, max_length=250)
