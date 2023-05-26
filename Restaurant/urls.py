from django.urls import path
from .views import (
    splash,
    intro,
    home,
    blog,
    menu,
    contact,
    single,
    booking,
    about,
    team,
    feature,
    restauranty,
    food_hut,
    components,
)


app_name = "Restaurant"


urlpatterns = [
    ## Servies Web Set
    path("", splash, name="Splash"),
    path("intro/", intro, name="Intro"),
    path("home/", home, name="Home"),
    path("about/", about, name="About"),
    path("blog/", blog, name="Blog"),
    path("menu/", menu, name="Menu"),
    path("contact/", contact, name="Contact"),
    path("single/", single, name="Single"),
    path("booking/", booking, name="Booking"),
    path("team/", team, name="Team"),
    path("feature/", feature, name="Feature"),
    path("restauranty/", restauranty, name="Restauranty"),
    path("food_hut/", food_hut, name="Food_Hut"),
    path("components/", components, name="Components"),
]
