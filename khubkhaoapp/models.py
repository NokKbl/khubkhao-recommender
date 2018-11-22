from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class EthnicFood(models.Model):
    ethnic_food_name = models.CharField(
        max_length=20,
        verbose_name='Ethnic food',
        unique=True,
        blank=False,
        help_text='Enter ethnic food name'
    )

    def __str__(self):
        return self.ethnic_food_name

    class Meta:
        verbose_name = "Ethnic food"
        verbose_name_plural = "Ethnic foods"


class Category(models.Model):
    type_name = models.CharField(
        max_length=20,
        verbose_name='Category name',
        unique=True,
        blank=False,
        help_text='Enter Category name'
    )

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Food(models.Model):
    food_name = models.CharField(
        max_length=40,
        verbose_name='Food name',
        unique=True,
        blank=False,
        help_text='Enter food name'
    )

    image_location = models.CharField(
        max_length=100,
        verbose_name='Image url',
        unique=True,
        null=True,
        blank=True,
        help_text='Enter url location'
    )

    average_price = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2,
        verbose_name='Average price',
        blank=True,
        null=True,
    )

    original_rate = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2,
        verbose_name='Original Rate',
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
    )

    user_rate = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2,
        verbose_name='User Rate',
        blank=True,
        null=True,
    )

    user_count = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name='User Count',
        help_text='Must be zero', 
    )

    ethnic_food_name = models.ForeignKey(
        EthnicFood,
        on_delete=models.CASCADE,
        verbose_name='Ethnic Food',
        blank=False,
    )

    category = models.ManyToManyField(
        Category,
        verbose_name='Category',
        blank=False
    )

    def __str__(self):
        return self.food_name

    def get_average_price(self):
        return self.average_price

    def get_image_location(self):
        return self.image_location

    def set_user_rate(self,value):
        self.user_rate += value

    def get_total_rate(self):
        float_original = float(self.original_rate)*0.8
        self.original_rate = float_original
        float_user = float(self.user_rate)*0.2
        total_rate = float("{0:.2f}".format(float_user+float_original))
        self.original_rate = total_rate
        return total_rate

    def get_original_rate(self):
        return self.original_rate

    def get_user_rate(self):
        return self.user_rate

    def get_user_count(self):
        return self.user_count

    # def change_user_rate(self, increase):
    #     if self.user_rate+increase > 100 :
    #         self.user_rate = 100

    #     return self.user_rate+increase

    # def get_total_rate(self):
    #     float_price = float(self.original_rate)*0.8
    #     float_user = float(self.user_rate)*0.2
    #     float_price = float("{0:.2f}".format(float_price))
    #     float_user = float("{0:.2f}".format(float_user))
    #     return float_price+float_user

    # def get_db_prep_value(self, value, connection, prepared=False):
    #     value = super().get_db_prep_value(value, connection, prepared)
    #     if value is not None:
    #         return connection.Database.Binary(value)
    #     return value

    def get_ethnic_food_name(self):
        return self.ethnic_food_name

    def get_category(self):
        return self.category

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"
        ordering = ['-original_rate']
