from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'Products', views.ProductViewSet, basename='product')

urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
]
