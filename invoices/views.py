from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

#for class based views
from django.views import View
from .forms import InvoiceAddForm

from . import controllers, util

# Create your views here.
class ListInvoicesView(View):
    template_name = 'invoices/list.html'
    template_no_permisions = 'invoices/no-permissions.html'

    def get(self, request, *args, **kwargs):
        
        logged_user = util.verify_login(request)
        if logged_user['logged_in'] is False:
            return HttpResponseRedirect(reverse('authentication:login'))
        if logged_user['id_fiscal'] != kwargs['slug']:
            return render(request, self.template_no_permisions, {'title': 'Not permisions:', 'client_id_fiscal': logged_user['id_fiscal'], 'logged_user': logged_user})


        client = controllers.get_all_client_data(kwargs['slug'])
        return render(request, self.template_name, {'client': client, 'title': 'Invoices', 'client_id_fiscal': client.ID_fiscal, 'logged_user': logged_user})

class InvoiceCreateView(View): 
    form_class = InvoiceAddForm
    template_name = 'invoices/create.html'
    created_template_name = 'invoices/list.html'
    template_no_permisions = 'invoices/no-permissions.html'
    slug = ''
    logged_user= {}
    

    def get(self, request, *args, **kwargs):
        self.slug = kwargs['slug']
        self.logged_user = util.verify_login(request)
        if self.logged_user['logged_in'] is False:
            return HttpResponseRedirect(reverse('authentication:login'))
        if self.logged_user['id_fiscal'] != self.slug:
            return render(request, self.template_no_permisions, {'title': 'Not permisions:', 'client_id_fiscal': self.logged_user['id_fiscal'], 'logged_user': self.logged_user})
        
        client = controllers.get_all_client_data(self.slug)
        form = self.form_class()
        return render(request, self.template_name, {'form': form, "title": 'Create Invoice', 'client_id_fiscal' : self.slug, 'client': client, 'logged_user': self.logged_user})

    def post(self, request, *args, **kwargs):
        self.slug = kwargs['slug']
        self.logged_user = util.verify_login(request)
        if self.logged_user['logged_in'] is False:
            return HttpResponseRedirect(reverse('authentication:login'))
        if self.logged_user['id_fiscal'] != self.slug:
            return render(request, self.template_no_permisions, {'title': 'Not permisions:', 'client_id_fiscal': self.logged_user['id_fiscal'], 'logged_user': self.logged_user})
        
        form = self.form_class(request.POST)
        
        # create the invoice 
        created_invoice = controllers.save_client_invoices(form, self.slug)
        
        if created_invoice['error'] == False:
                return render(request, self.created_template_name, {'title': 'Invoices List - saved!', 'client_id_fiscal': self.slug,  'client': created_invoice['client']})
        else:
            return render(request, self.template_name, {"error": created_invoice['error'], "message_error": created_invoice['message_error'], "form": form, 'title': 'Error creating invoice', 'logged_user': self.logged_user})
        

