from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.



app_name= "Burgar_King"


context= {
    "app_name": app_name
}


# @
def splash(req):
    context["page_name"]= "home"
    return render(req, f"Foodee/index.html", context= context)


# @login_required
def home(req):
    context["page_name"]= "home"
    return render(req, f"{app_name}/index.html", context= context)


def blog(req):
    context["page_name"]= "blog"
    return render(req, f"{app_name}/blog.html", context= context)


def about(req):
    context["page_name"]= "about"
    return render(req, f"{app_name}/about.html", context= context)


def contact(req):
    context["page_name"]= "contact"
    return render(req, f"{app_name}/contact.html", context= context)


def menu(req):
    context["page_name"]= "menu"
    return render(req, f"{app_name}/menu.html", context= context)


def booking(req):
    context["page_name"]= "booking"
    return render(req, f"{app_name}/booking.html", context= context)


def single(req):
    context["page_name"]= "single"
    return render(req, f"{app_name}/single.html", context= context)


def team(req):
    context["page_name"]= "team"
    return render(req, f"{app_name}/team.html", context= context)


def feature(req):
    context["page_name"]= "feature"
    return render(req, f"{app_name}/feature.html", context= context)

def restauranty(req):
    return render(req, "Restauranty/index.html")

def food_hut(req):
    return render(req, "Food_Hut/index.html")

def components(req):
    return render(req, "Food_Hut/components.html")