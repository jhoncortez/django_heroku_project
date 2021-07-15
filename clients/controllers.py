from .models import Cliente
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from .forms import ClientsAddForm

def save_client(f):
    try:
        #client = Cliente.objects.get(ID_fiscal=form.cleaned_data["ID_fiscal"])
        client = Cliente.objects.get(ID_fiscal=f.clean_id_fiscal())
    except Cliente.DoesNotExist:
        # obj = Cliente()
        # obj.ID_fiscal = form.clean_id_fiscal()
        # obj.nombres = form.cleaned_data["nombres"]
        # obj.apellidos = form.cleaned_data["apellidos"]
        # obj.save()
        created_user = f.save()
        context = {
            'error': False,
            'id_fiscal': created_user.ID_fiscal
        }
        return context
    else:
        return {'error':True, 'message_error': "Already exist a client with id_fiscal %s." % f.clean_id_fiscal()}

def update_client(f):
    if f.is_valid():
        updated_client = f.save()
        context = {
            'error': False,
            'id_fiscal': updated_client.ID_fiscal
        }
    else :
        context = {
            'error': True,
            'message_error': 'Validation error - plese try again'
        }
    return context

def get_client_by_idfiscal(id_fiscal):
    try:
        client = Cliente.objects.get(ID_fiscal=id_fiscal)
    except Cliente.DoesNotExist:
        raise Http404("Client does not exist")
    return client 

def get_client_by_pk(pk):
    try:
        client = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        raise Http404("Client does not exist")
    return client 