from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.



app_name= "Burgar_King"


context= {
    "app_name": app_name
}


def splash(req):
    context["page_name"]= "home"
    return render(req, f"Splash/index.html", context= context)


@login_required
def intro(req):
    context["page_name"]= "home"
    return render(req, f"Foodee/index.html", context= context)


@login_required
def home(req):
    context["page_name"]= "home"
    return render(req, f"{app_name}/index.html", context= context)


@login_required
def blog(req):
    context["page_name"]= "blog"
    return render(req, f"{app_name}/blog.html", context= context)


@login_required
def about(req):
    context["page_name"]= "about"
    return render(req, f"{app_name}/about.html", context= context)


@login_required
def contact(req):
    context["page_name"]= "contact"
    return render(req, f"{app_name}/contact.html", context= context)


@login_required
def menu(req):
    context["page_name"]= "menu"
    return render(req, f"{app_name}/menu.html", context= context)


@login_required
def booking(req):
    context["page_name"]= "booking"
    return render(req, f"{app_name}/booking.html", context= context)


@login_required
def single(req):
    context["page_name"]= "single"
    return render(req, f"{app_name}/single.html", context= context)


@login_required
def team(req):
    context["page_name"]= "team"
    return render(req, f"{app_name}/team.html", context= context)


@login_required
def feature(req):
    context["page_name"]= "feature"
    return render(req, f"{app_name}/feature.html", context= context)

@login_required
def restauranty(req):
    return render(req, "Restauranty/index.html")

@login_required
def food_hut(req):
    return render(req, "Food_Hut/index.html")

@login_required
def components(req):
    return render(req, "Food_Hut/components.html")