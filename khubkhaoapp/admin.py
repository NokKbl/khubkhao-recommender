# from django.contrib import admin
# from .models import Category,Food

# # Register your models here.
# # admin.site.register(Food)
# admin.site.register(Category)
# # admin.site.register(Vegetable)

# class FoodAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['food_name','average_price']}),
#         ('Vegetable Type', {'fields': ['pollovegetarian','pescovegetarian','lacto_ovo_vegetarian','lacto_vegetarian','vegan']}),
#         ('Picture Location',{'fields':['picture_location']})
#     ]
# admin.site.register(Food,FoodAdmin)

from django.contrib import admin

from .models import Category, Food,Veggie,Item,Ingredient

class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1

class ItemInline(admin.StackedInline):
    model = Item
    extra = 1

class VeggieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['veggie_name']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ItemInline]

class FoodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['food_name']}),
    ]
    inlines = [CategoryInline]
    # list_display = ('food_name', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # search_fields = ['question_text']

admin.site.register(Food, FoodAdmin)
admin.site.register(Veggie,VeggieAdmin)
admin.site.register(Ingredient)