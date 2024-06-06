from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('clientForm/', views.clientForm, name='clientForm'),
    path('menu/', views.menu, name='menu'),
    # path('clients/', views.clients, name='clients'),
    path('clients/', views.ClientListView.as_view(), name='clients'),
]
