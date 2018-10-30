from django.contrib import admin
from .models import Category,Food

# Register your models here.
# admin.site.register(Food)
admin.site.register(Category)
# admin.site.register(Vegetable)

class FoodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['food_name','average_price']}),
        ('Vegetable Type', {'fields': ['pollovegetarian','pescovegetarian','lacto_ovo_vegetarian','lacto_vegetarian','vegan']}),
        ('Picture Location',{'fields':['picture_location']})
    ]
admin.site.register(Food,FoodAdmin)
