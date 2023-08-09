from rest_framework import routers
from API.Serializer import ChangePasswordSerializer
from Address.ViewsSet import AddressViewSet, AreaViewSet, CityViewSet, CountryViewSet, GovernorateViewSet, StreetViewSet
from Driver.ViewsSet import DriverViewSet
from Language.ViewsSet import LanguageViewSet
from Category.ViewsSet import CategoryViewSet
from Notification.ViewsSet import NotificationViewSet
from Order.ViewsSet import OrderRateDriverViewSet, OrderRateRestaurantViewSet, OrderViewSet, OrderMealViewSet
from Payment.ViewsSet import CurrencyViewSet, PaymentMethodViewSet
from Restaurant.ViewsSet import (
    ColorStepViewSet,
    ColorViewSet,
    GradientViewSet,
    HospitalityViewSet,
    LogoViewSet,
    RestaurantViewSet,
    RestaurantMealViewSet,
    RestaurantMealSizeViewSet,
    RestaurantMealImageViewSet,
    UserRestaurantViewSet,
)
from User.ViewsSet import  MyProfileViewSet, UserViewSet
from Meal.ViewsSet import MealViewSet

from .ViewsSet import  RegisterViewSet

router = routers.DefaultRouter()

## User App

router.register('register', RegisterViewSet, basename='register')
router.register('users', UserViewSet)
router.register('MyProfile', MyProfileViewSet)

## Restaurant App
router.register('restaurants', RestaurantViewSet)
router.register('user_restaurants', UserRestaurantViewSet)
router.register('restaurants_meals', RestaurantMealViewSet)
router.register('restaurants_meals_sizes', RestaurantMealSizeViewSet)
router.register('restaurants_meals_images', RestaurantMealImageViewSet)
router.register('gradients', GradientViewSet)
router.register('logos', LogoViewSet)
router.register('colors', ColorViewSet)
router.register('color_steps', ColorStepViewSet)
router.register('hospitalities', HospitalityViewSet)

## Category App
router.register('categories', CategoryViewSet)

## Order App
router.register('orders', OrderViewSet)
router.register('order_meals', OrderMealViewSet)
router.register('order_meals', OrderMealViewSet)
router.register('order_rate_drivers', OrderRateDriverViewSet)
router.register('order_rate_restaurants', OrderRateRestaurantViewSet)


## Payment App
router.register('currencies', CurrencyViewSet)
router.register('payment_methods', PaymentMethodViewSet)

## Language App
router.register('languages', LanguageViewSet)

## Meal App
router.register('Meals', MealViewSet)


## Driver App
router.register('drivers', DriverViewSet)


## Notification App
router.register('notifications', NotificationViewSet)

## Address App
router.register('address', AddressViewSet)
router.register('street', StreetViewSet)
router.register('area', AreaViewSet)
router.register('cities', CityViewSet)
router.register('governorates', GovernorateViewSet)
router.register('countries', CountryViewSet)

