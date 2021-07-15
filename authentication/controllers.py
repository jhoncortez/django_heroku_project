from django.apps import apps
Cliente = apps.get_model('clients', 'Cliente')

def get_client_by_idfiscal(id_fiscal):
    try:
        client = Cliente.objects.get(ID_fiscal=id_fiscal)
    except Cliente.DoesNotExist:
        context = {
            'error':True,
            'message_error': "Client doesn't exist. please Sign Up"
        }
    else :
        context = {
            'error':False,
            'client': client
        }
    return context 