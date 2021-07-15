from django.apps import apps
Cliente = apps.get_model('clients', 'Cliente')
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from collections import namedtuple 


def save_client_invoices(f,id_fiscal):
    if f.is_valid():
        c = get_all_client_data(id_fiscal)
        f.cleaned_data['ID_fiscal']=c.ID_fiscal
        #Invoice = namedtuple("c.factura_set.create", f.cleaned_data.keys())
        #print (Invoice(**f.cleaned_data))
        print(f.cleaned_data)
        c.factura_set.create(**f.cleaned_data)
        
        context = {
            'error': False,
            'id_fiscal': c.ID_fiscal,
            'client': c
        }
    else :
        context = {
            'error': True,
            'message_error': 'Validation error - plese try again'
        }
    return context

def get_all_client_data(id_fiscal):
    try:
        client = Cliente.objects.get(ID_fiscal=id_fiscal)
    except Cliente.DoesNotExist:
        raise Http404("Client does not exist")
    return client 
