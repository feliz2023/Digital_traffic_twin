from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-success/', views.contact_success, name='contact_success'),
]
