from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import NewUserForm

# Create your views here.


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(reverse_lazy('Quran:Home'))
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="Log/signup.html", context={"form":form})


