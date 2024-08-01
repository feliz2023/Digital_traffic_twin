from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Home/', views.Home, name='Home'),
    path('About/', views.About, name='About'),
    path('project_plan/', views.project_plan, name="project_plan"),
    path('data_tech/', views.data_tech, name="data_tech"),
    path('update/', views.update, name="update"),
    path('contact/', views.contact, name="contact"),
    path('contact-success/', views.contact_success, name='contact_success'),
]
