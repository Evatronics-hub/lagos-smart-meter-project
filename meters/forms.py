from django import forms
from .models import Meter

class MeterChangeForm(forms.ModelForm):
    balance = forms.DecimalField(decimal_places=2, max_digits=100)

    class Meta:
        model = Meter
        fields = ('user', 'billing_type')