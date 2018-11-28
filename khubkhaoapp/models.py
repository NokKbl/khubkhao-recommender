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
        help_text='Must be 0-100', 
    )

    total_rate = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2,
        verbose_name='Total Rate',
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
        help_text='Must be 0-100', 
    )

    user_rate = models.DecimalField(
        default=0,
        max_digits=9,
        decimal_places=2,
        verbose_name='User Rate',
        blank=True,
        null=True,
        validators=[MinValueValidator(0)],
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

    pk_voted = models.TextField(
        verbose_name='Primary key of user',
        blank=True,
    )

    check_vote = models.BooleanField(
        default=True
    )
    

    def __str__(self):
        return self.food_name


    def get_average_price(self):
        return self.average_price


    def get_image_location(self):
        return self.image_location
    

    def add_user_count(self):
        self.user_count = float(self.user_count)+1


    def add_user_pk(self,primary_key):
        self.pk_voted = self.pk_voted + str(primary_key) + ","


    def get_user_pk(self):
        return self.pk_voted


    def set_user_rate(self,value):
        self.user_rate = float(self.user_rate)+value


    def set_total_rate(self):
        float_original = float(self.original_rate)*0.8
        self.total_rate = float_original
        float_user = float(self.user_rate)*0.2
        count = float(self.user_count)
        if(count != 0):
            float_user = float_user/count
        compute_rate = float("{0:.2f}".format(float_user+float_original))
        self.total_rate = compute_rate
        return self.total_rate


    def get_total_rate(self):
        return self.total_rate


    def get_original_rate(self):
        return self.original_rate


    def get_user_rate(self):
        return self.user_rate


    def get_user_count(self):
        return self.user_count
    

    def get_ethnic_food_name(self):
        return self.ethnic_food_name


    def get_category(self):
        return self.category


    def set_check_false(self):
        self.check_vote = False
    

    def set_check_true(self):
        self.check_vote = True
    

    def get_check_vote(self):
        return self.check_vote


    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"
        ordering = ['-original_rate']
