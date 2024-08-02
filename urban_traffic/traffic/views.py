from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm
from .models import trafficData

def index(request):
    traffic_data = trafficData.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                'gobaeanony@gmail.com',  # Your email address (from email)
                ['khushi.22scse1012412@galgotiasuniversity.edu.in'],  # Recipient email address (to email)
            )
            
            return HttpResponseRedirect(reverse('contact_success'))
    else:
        form = ContactForm()

    return render(request, 'traffic/index.html', {'traffic_data': traffic_data, 'form': form})


def Home(request):
    return render(request, 'traffic/home.html')


def About(request):
    return render(request, 'traffic/About.html')


def project_plan(request):
    return render(request, 'traffic/project_plan.html')


def data_tech(request):
    return render(request, 'traffic/data_tech.html')


def update(request):
    return render(request, 'traffic/update.html')


def contact(request):
    return render(request, 'traffic/contact.html')


def contact_success(request):
    return render(request, 'traffic/contact_success.html')
