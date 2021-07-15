from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path('', views.index, name='index'),
    #path('<str:id_fiscal>/profile/', views.profile, name='profile'),
    #path('create/', views.create, name='create'),
    path('create/', views.ClientCreateView.as_view(), name='create'),
    path('<slug:slug>/profile/', views.ClientProfileView.as_view(), name='profile'),
    path('<slug:slug>/profile/edit', views.ClientEditProfileView.as_view(), name='edit'),
]