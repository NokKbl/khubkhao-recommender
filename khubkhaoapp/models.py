from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,blank=False,default='xxx')
    def __str__(self):
        return self.name

# class Vegetable(models.Model):
#     name = models.CharField(max_length=80)
#     def __str__(self):
#         return self.name

class Food(models.Model):
    food_name = models.CharField(max_length=20,blank=False,unique=True,verbose_name='Name')
    # vegetable = models.OneToOneField(
    #     Vegetable,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
    pollovegetarian      = models.BooleanField(blank=True,default=False)
    pescovegetarian      = models.BooleanField(blank=True,default=False)
    lacto_ovo_vegetarian = models.BooleanField(blank=True,default=False,verbose_name='Lacto_Ovo_Vegetarian')
    lacto_vegetarian     = models.BooleanField(blank=True,default=False,verbose_name='Lacto_Vegetarian')
    vegan                = models.BooleanField(blank=True,default=False)
    average_price        = models.PositiveIntegerField(blank=True,default=0)
    picture_location     = models.CharField(max_length=100,blank=True)
    # category             = models.ManyToManyField(Category,verbose_name='catty',help_text=('Please select the users that will be clear of this space'))
    def __str__(self):
        return self.food_name

    def get_veggie_type(self):
        check_veggie_type = [self.pollovegetarian,self.pescovegetarian,self.lacto_ovo_vegetarian,self.lacto_vegetarian,self.vegan]
        return check_veggie_type

    def get_pollovegetarian(self):
        return self.pollovegetarian

    def get_pescovegetarian(self):
        return self.pescovegetarian
    
    def get_lacto_ovo_vegetarian(self):
        return self.lacto_ovo_vegetarian
    
    def get_lacto_vegetarian(self):
        return self.lacto_vegetarian
    
    def get_vegan(self):
        return self.vegan
    
    def get_average_price(self):
        return self.average_price

    def get_picture_location(self):
        return self.picture_location

class Veggie:
    def __init__(self, veggie_name):
        self.veggie_name = veggie_name

    def get_veggie_name(self):
        return self.veggie_name