from django.contrib import admin
from .models import Food,Category,EthnicFood


class FoodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['food_name']}),
        ('Details',         {'fields': ['image_location','average_price','original_rate']}),
        ('Ethnic Food',     {'fields': ['ethnic_food_name']}),
        ('Category',        {'fields': ['category']}),
    ]


admin.site.register(Food, FoodAdmin)
admin.site.register(Category)
admin.site.register(EthnicFood)
