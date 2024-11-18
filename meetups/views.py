from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm
# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    context = {
        "meetups" : meetups,
        
    }
    return render(request,"index.html", context )

def meetup_details(request,meetup_slug):
 try:
    selected_meetup = Meetup.objects.get(slug=meetup_slug)
    if request.method == "GET":
        registration_form = RegistrationForm()
   
    else:
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
           user_email = registration_form.cleaned_data["email"]
           participant, _=Participant.objects.get_or_create(email=user_email)
           selected_meetup.participant.add(participant)
           return redirect("confirm-registration", meetup_slug=meetup_slug)
           
    context = {
        "meetup" : selected_meetup,
        "meetup_found" : True,
        "form":registration_form
    }     
    return render(request, "meetup-details.html", context)
           
 except Exception as e:
     context = {
       "meetup_found" : False
    }
     return render(request, "meetup-details.html", context)

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    context = {
        "organizer_email":meetup.organizers
    }
    return render(request, "registration-success.html")