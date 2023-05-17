from rest_framework import routers
from Driver.ViewsSet import DriverViewSet
from Language.ViewsSet import LanguageViewSet
from Category.ViewsSet import CategoryViewSet
from Location.ViewsSet import LocationViewSet
from Notification.ViewsSet import NotificationViewSet
from Order.ViewsSet import OrderRateDriverViewSet, OrderRateRestaurantViewSet, OrderViewSet, OrderMealViewSet
from Payment.ViewsSet import CurrencyViewSet, PaymentMethodViewSet
from Restaurant.ViewsSet import (
    RestaurantViewSet,
    RestaurantMealViewSet,
    RestaurantMealSizeViewSet,
    RestaurantMealImageViewSet,
)
from User.ViewsSet import UserViewSet
from Meal.ViewsSet import MealViewSet


router = routers.DefaultRouter()

## User App
router.register('users', UserViewSet)

## Restaurant App
router.register('restaurants', RestaurantViewSet)
router.register('restaurants_meals', RestaurantMealViewSet)
router.register('restaurants_meals_sizes', RestaurantMealSizeViewSet)
router.register('restaurants_meals_images', RestaurantMealImageViewSet)

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


## Location App
router.register('locations', LocationViewSet)

