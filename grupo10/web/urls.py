from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name="web/registration/login.html"), name="login"),
    path('accounts/logout/', views.user_logout, name='logout'),
    
    path('clientForm/', views.clientForm, name='clientForm'),
    path('productForm/', views.productForm, name='productForm'),
    path('orderForm/', views.orderForm, name='orderForm'),

    path('menu/', views.menu, name='menu'),
    path('clients/', views.ClientListView.as_view(), name='clients'),
]
