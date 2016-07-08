from django import forms
from .models import Lunch


class LunchForm(forms.ModelForm):
    class Meta:
        model = Lunch
        fields = ('submitter', 'food',)
