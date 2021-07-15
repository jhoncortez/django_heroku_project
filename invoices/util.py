from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def verify_login(request):
    
    if not request.session.has_key('logged_client'):
        return {'logged_in':False,'id_fiscal': '', 'nombres': ''}
    return {'logged_in':request.session['logged_client'],'id_fiscal': request.session['logged_client_idfiscal'], 'nombres': request.session['logged_client_nombres']} 
        
     