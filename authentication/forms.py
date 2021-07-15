from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AuthenticationLoginForm(forms.Form):
    ID_fiscal = forms.CharField(label="ID Fiscal")
         
    def clean_id_fiscal(self):
        if self.is_valid():
            data = self.cleaned_data['ID_fiscal']

        # Check if a date is not in the past.
        if not data:
            self.show_error('field ID_fiscal cant be empty')

        # Remember to always return the cleaned data.
        return data

    def show_error(message):
        raise ValidationError(_(message)) 
    