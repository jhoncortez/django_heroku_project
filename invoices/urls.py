from django.urls import path

from . import views

app_name = "invoices"

urlpatterns = [
    #path('list', views.list, name='list'),
    path('list/client/<slug:slug>/', views.ListInvoicesView.as_view(), name='list'),
    path('client/<slug:slug>/create/', views.InvoiceCreateView.as_view(), name='create'),
]