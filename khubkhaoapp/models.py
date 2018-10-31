from django.db import models

class Item(models.Model):
    item_name = models.CharField(
        max_length=20,
        verbose_name='Ingredient name',
        unique=True,
        blank=False,
        help_text='Enter ingredient name'
    )
    def __str__(self):
        return self.item_name

class Veggie(models.Model):
    veggie_name = models.CharField(
        max_length=20,
        verbose_name='Veggie type',
        unique=True,
        blank=False,
        help_text='Enter veggie type',
        primary_key=True,
    )
    item_name = models.ManyToManyField(
        Item,
        verbose_name='Item name'
    )
    def __str__(self):
        return self.veggie_name

class Food(models.Model):
    food_name = models.CharField(
        max_length=20,
        verbose_name='Food name',
        unique=True,
        blank=False,
        help_text='Enter food name'
    )
    image_location = models.CharField(
        max_length=100,
        verbose_name='Image url',
        unique=True,
        blank=False,
        help_text='Enter url location'
    )
    average_price = models.PositiveIntegerField(
        default=0,
        verbose_name='Average price'
    )
    veggie = models.ManyToManyField(
        Veggie,
        verbose_name='Veggie Type',
    )

    def __str__(self):
        return self.food_name
    def get_average_price(self):
        return self.average_price
    def get_image_location(self):
        return self.image_location
    def get_veggie(self):
        return self.veggie
    def get_try(self):
        return self.call
    def get_cat(self):
        return self.cat

class Ingredient(models.Model):
    non_veg = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        verbose_name='Ingredient'
    )
    items = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Item',
    )
  
