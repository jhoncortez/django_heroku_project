from django.forms import ModelForm
from .models import Factura
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class InvoiceAddForm(ModelForm):
    class Meta:
        model = Factura
        exclude = ('ID_fiscal', 'fecha_factura','estado_factura', 'cliente')
        
    def clean_id_fiscal(self):
        data = self.cleaned_data['ID_fiscal']

        # Check if a date is not in the past.
        if not data:
            self.show_error('This field cant be empty')

        # Remember to always return the cleaned data.
        return data
    def clean(self):
        cleaned_data = super(InvoiceAddForm, self).clean() # call the parent clean method
        return cleaned_data

    def show_error(message):
        raise ValidationError(_(message))


# class ClientsEditForm(ModelForm):
#     class Meta:
#         model = Cliente
#         exclude = ('activo', 'fecha_creacion', 'ID_fiscal','fecha_inactivo')
#         #fields = ['ID_fiscal', 'nombres', 'apellidos']
        

#     #def clean_id_fiscal(self):
#         #data = self.cleaned_data['ID_fiscal']

#         # Check if a date is not in the past.
#         #if not data:
#             #self.show_error('This field cant be empty')

#         # Remember to always return the cleaned data.
#         #return data
#     def show_error(message):
#         raise ValidationError(_(message))
