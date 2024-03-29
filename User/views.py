import random
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy

from .models import User, Profile
from .forms import NewUserForm
from API.TwilioMessageHandler import TwilioMessageHandler

# from Ver.TwilioMessageHandler import TwilioMessageHandler
# Create your views here.


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(reverse_lazy('Restaurant:Intro'))
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="Log/sign_up.html", context={"form":form})

# ### Twilio
# # https://www.twilio.com/blog/enable-multiple-otp-methods-django

def register(request):
    if request.method=="POST":
        if User.objects.filter(username__iexact=request.POST['username']).exists():
            return HttpResponse("User already exists")
        if User.objects.filter(email__iexact=request.POST['email']).exists():
            return HttpResponse("User already exists")
        otp=random.randint(1000,9999)
        user=User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            mobile=request.POST['mobile'],
            otp=f'{otp}'
        )
        if request.POST['methodOtp']=="methodOtpWhatsapp":
            messagehandler=TwilioMessageHandler(request.POST['mobile'],otp).send_otp_via_whatsapp()
        else:
            messagehandler=TwilioMessageHandler(request.POST['mobile'],otp).send_otp_via_message()
        return redirect(reverse_lazy('Restaurant:Intro')).set_cookie("can_otp_enter",True,max_age=600)
          
    return render(request, 'Log/sign_up.html')


def otpVerify(request,uid):
    if request.method=="POST":
        profile=Profile.objects.get(uid=uid)     
        if request.COOKIES.get('can_otp_enter')!=None:
            if(profile.otp==request.POST['otp']):
                red=redirect("home")
                red.set_cookie('verified',True)
                return red
            return HttpResponse("wrong otp")
        return HttpResponse("10 minutes passed")        
    return render(request,"Twilio/otp.html",{'id':uid})


# def home(request):
#     if request.COOKIES.get('verified') and request.COOKIES.get('verified')!=None:
#         return HttpResponse(" verified.")
#     else:
#         return HttpResponse(" Not verified.")


# verification view
def verify_email(request, pk):
    user = User.objects.get(pk=pk)
    if not user.email_verified:
        user.email_verified = True
        user.save()
    return redirect('http://localhost:8000/')  # Replace with your desired redirect URL