from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse , HttpResponseRedirect
from django.apps import apps
Cliente = apps.get_model('clients', 'Cliente')

#for class based views
from django.views import View

from .forms import AuthenticationLoginForm

from . import controllers

# Create your views here.
def index(request):
    if "logged_client" in request.session :
        return HttpResponseRedirect(reverse('clients:profile', args=[request.session['logged_client_idfiscal']]))
    return HttpResponseRedirect(reverse("authentication:login"))

def login(request):
    if "logged_client" in request.session :
        return HttpResponseRedirect(reverse('clients:profile', args=[request.session['logged_client_idfiscal']]))

    form = AuthenticationLoginForm()
    return render(request, 'authentication/login.html', {'title': 'Sign in:', 'form': form})
    # return HttpResponseRedirect(reverse("authentication:login"))

def signup(request):
    if "logged_client" in request.session :
        return HttpResponseRedirect(reverse('clients:profile', args=[request.session['logged_client_idfiscal']]))

    return HttpResponseRedirect(reverse("clients:create"))

def auth(request):
    if "logged_client" in request.session :
        return HttpResponseRedirect(reverse('clients:profile', args=[request.session['logged_client_idfiscal']]))

    if request.method == 'GET':
        form = AuthenticationLoginForm(request.GET)
        if not form.is_valid :
            return render(request, 'authentication/login.html', {'error': True,'title': 'Sign in - Error','form': form, 'message_error': 'Invalid form'})
        
        query = controllers.get_client_by_idfiscal(form.clean_id_fiscal())

        if not query['error']:
            request.session['logged_client'] = True
            request.session['logged_client_id'] = query['client'].id
            request.session['logged_client_idfiscal'] = query['client'].ID_fiscal
            request.session['logged_client_nombres'] = query['client'].nombres
            return HttpResponseRedirect(reverse('clients:profile', args=[query['client'].ID_fiscal]))
        else:
            return render(request, 'authentication/login.html', {'error': query['error'],'title': 'Sign in - Error','form': form, 'message_error': query['message_error']})
    return render(request, 'authentication/login.html', {'title': 'Sign in','form': AuthenticationLoginForm()})

def logout(request):
    if not request.session.has_key('logged_client'):
        return HttpResponseRedirect(reverse('authentication:login'))
    try:
        del request.session['logged_client']
        del request.session['logged_client_id']
        del request.session['logged_client_idfiscal']
        del request.session['logged_client_nombres']
    except:
        pass
    return HttpResponseRedirect(reverse('authentication:login'))
    