from django.contrib import admin

from .models import  Color, Logo, RestaurantMealImage, RestaurantMeal, RestaurantMealSize, Restaurant, Gradient, ColorStep

# # Register your models here.


from .forms import ColorForm

...

class ColorAdmin(admin.ModelAdmin):
    form = ColorForm
    model = Color
    # filter_horizontal = ('pk',)
    list_display = [
            'color',
        ]   
    fieldsets = (
        (None, {
            'fields': ['color']
            }),
        )
    
admin.site.register(Color, ColorAdmin)

####
class ColorStepInline(admin.TabularInline):
    model = ColorStep


class GradientInline(admin.ModelAdmin):
    inlines = [ 
                ColorStepInline,
              ]


admin.site.register(Gradient, GradientInline)

####


class LogoInline(admin.TabularInline):
    model = Logo


class RestaurantInline(admin.ModelAdmin):
    inlines = [ 
                LogoInline,
              ]


admin.site.register(Restaurant, RestaurantInline)

####

class RestaurantMealSizeInline(admin.StackedInline):
    model = RestaurantMealSize


class RestaurantMealImageInline(admin.StackedInline):
    model = RestaurantMealImage


@admin.register(RestaurantMeal)
class RestaurantMealAdmin(admin.ModelAdmin):
    inlines = [
        RestaurantMealImageInline,
        RestaurantMealSizeInline,
    ]
    
