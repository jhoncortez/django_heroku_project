from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

#for class based views
from django.views import View
from .forms import ClientsAddForm, ClientsEditForm

from . import controllers, util

# class ClientValidation:
#     logged_user = {}
#     id_fiscal = ''
#     def __init__(self, req, idf):
#         self.request = req
#         self.id_fiscal = idf
#         self.logged_user = util.verify_login(req)

#     def validate_logged_client(self, reverse, HttpResponseRedirect):
#         if self.logged_user['logged_in'] is False:
#             return HttpResponseRedirect(reverse('authentication:login'))

#     def validate_permissions_client(self, render):
#         if self.logged_user['id_fiscal'] != self.id_fiscal:
#             return render(self.request, 'clients/no-permissions.html', {'title': 'Not permisions:', 'client_id_fiscal': self.logged_user['id_fiscal'], 'logged_user': self.logged_user})


class ClientProfileView(View):
    template_name = 'clients/profile.html'
    template_no_permisions = 'clients/no-permissions.html'

    def get(self, request, *args, **kwargs):
        
        logged_user = util.verify_login(request)
        if logged_user['logged_in'] is False:
            return HttpResponseRedirect(reverse('authentication:login'))
        if logged_user['id_fiscal'] != kwargs['slug']:
            return render(request, self.template_no_permisions, {'title': 'Not permisions:', 'client_id_fiscal': logged_user['id_fiscal'], 'logged_user': logged_user})
        # valid = ClientValidation(request, kwargs['slug'])
        # valid.validate_logged_client(reverse, HttpResponseRedirect)
        # valid.validate_permissions_client(render)

        client = controllers.get_client_by_idfiscal(kwargs['slug'])
        return render(request, self.template_name, {'client': client, 'title': 'Profile:', 'client_id_fiscal': client.ID_fiscal, 'logged_user': logged_user})

class ClientCreateView(View): 
    form_class = ClientsAddForm
    template_name = 'clients/create.html'
    created_template_name = 'clients/profile-created.html'

    def get(self, request, *args, **kwargs):
        logged_user = util.verify_login(request)
        if logged_user['logged_in'] :
            return HttpResponseRedirect(reverse('clients:profile', args=[logged_user['id_fiscal']]))

        form = self.form_class()
        return render(request, self.template_name, {'form': form, "title": 'Signup as client'})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # create the client 
            created_client = controllers.save_client(form)
            if created_client['error'] == False:
                return render(request, self.created_template_name, {'title': 'Account created waiting for activation', 'client_id_fiscal': created_client['id_fiscal']})
            else:
                return render(request, self.template_name, {"error": created_client['error'], "message_error": created_client['message_error'], "form": form, 'title': 'Error creating client'})
        else: 
            # If the form is invalid, re-render the page with existing information.
            return render(request, self.template_name, {"title": "Error - Invalid form data", "form": form})

def index(request):
    return HttpResponseRedirect(reverse("authentication:login"))

# def profile(request, id_fiscal):
#     client = controllers.get_client_by_idfiscal(id_fiscal)
#     return render(request, 'clients/profile.html', {'client': client, 'title': 'Profie:', 'client_id_fiscal': client.ID_fiscal})

# def create(request):
#     # Check if method is POST
#     if request.method == "POST":

#         # Take in the data the user submitted and save it as form
#         form = ClientsAddForm(request.POST)

#         # Check if form data is valid (server-side)
#         if form.is_valid():
#             # create the client 
#             created_client = controllers.save_client(form)
#             if created_client['error'] == False:
#                 return render(request, 'clients/profile-created.html', {'title': 'Account created waiting for activation', 'client_id_fiscal': created_client['id_fiscal']})
#             else:
#                 raise forms.ValidationError(
#                     created_client['message_error'],
#                 )
#         else: 
#             # If the form is invalid, re-render the page with existing information.
#             return render(request, "clients/create.html", {"title": "Error - Invalid form data", "form": form})

#     return render(request, "clients/create.html", {
#         "form": ClientsAddForm(),
#         "title": 'Signup as client'
#     })

# def edit(request):
#     return HttpResponse("Edit client page!")

class ClientEditProfileView(View):
    form_class = ClientsEditForm
    template_name = 'clients/edit.html'
    template_no_permisions = 'clients/no-permissions.html'

    def get(self, request, *args, **kwargs):
        logged_user = util.verify_login(request)
        if logged_user['logged_in'] is False:
            return HttpResponseRedirect(reverse('authentication:login'))
        if logged_user['id_fiscal'] != kwargs['slug']:
            return render(request, self.template_no_permisions, {'title': 'Not permisions:', 'client_id_fiscal': logged_user['id_fiscal'], 'logged_user': logged_user})
        
        
        client = controllers.get_client_by_idfiscal(kwargs['slug'])
        form = self.form_class(instance=client)
        return render(request, self.template_name, {'form': form, "title": 'Edit profile', 'client_id_fiscal': client.ID_fiscal, 'logged_user': logged_user})

    def post(self, request, *args, **kwargs):
        logged_user = util.verify_login(request)
        if logged_user['logged_in'] is False:
            return HttpResponseRedirect(reverse('authentication:login'))

        client = controllers.get_client_by_idfiscal(kwargs['slug'])
        form = self.form_class(request.POST, instance=client)
        created_client = controllers.update_client(form)

        if created_client['error']:
            return render(request, self.template_name, {"error": created_client['error'], "message_error": created_client['error'], "form": form, 'title': 'Error updating client','client_id_fiscal': client.ID_fiscal, 'logged_user': logged_user})
        else: 
            #return HttpResponse(created_client['id_fiscal'])
            return HttpResponseRedirect(reverse('clients:profile', args=[created_client['id_fiscal']]))

