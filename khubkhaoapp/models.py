from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class EthnicFood(models.Model):
    """
    EthnicFood class represents ethnic of food.

    Attributes:
        models.Model(Model): source of information. It contains the essential fields and behaviors of the data.
    """
    ethnic_food_name = models.CharField(
        max_length=20,
        verbose_name='Ethnic food',
        unique=True,
        blank=False,
        help_text='Enter an ethnic food'
    )


    def __str__(self):
        """
        Override to print a readable string presentation of ethnic food.

        Returns:
            str: ethnic of food.
        """
        return self.ethnic_food_name

    class Meta:
        verbose_name = "Ethnic food"
        verbose_name_plural = "Ethnic foods"


class Category(models.Model):
    """
    Category class represents food's category.

    Attributes:
        models.Model(Model): source of information. It contains the essential fields and behaviors of the data.
    """
    type_name = models.CharField(
        max_length=20,
        verbose_name='Category name',
        unique=True,
        blank=False,
        help_text='Enter Category name'
    )


    def __str__(self):
        """
        Override to print a readable string presentation of food's category.

        Returns:
            str: category's name.
        """
        return self.type_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Food(models.Model):
    """
    Food class represents informations and details of food.

    Food class represents name, image url, average price, rate, category, and ethnic of food.
    This class also compute rate of food from user rate and rate in database by itself.

    Attributes:
        models.Model (Model): source of information. It contains the essential fields and behaviors of the data.
    """
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
        """
        Override to print a readable string presentation of food name.

        Returns:
            str: food name.
        """
        return self.food_name

    def get_average_price(self):
        """
        Get average price of food.

        Returns:
            Decimal: average price of food.
        """
        return self.average_price

    def get_image_location(self):
        """
        Get image url of food.

        Returns:
            str: image url of food.
        """
        return self.image_location

    def add_user_count(self):
        """
        Count the number of user who voted on each food and update into the database.
        """
        self.user_count = float(self.user_count)+1

    def add_user_pk(self, primary_key):
        """
        Add user's primary key that voted on each food into the database.

        Args:
            primary_key (str): user's primary key.
        """
        self.pk_voted = self.pk_voted + str(primary_key) + ","

    def get_user_pk(self):
        """
        Get all primary keys of users which have been voted on each food.

        Returns:
            str: all primary keys of users which have been voted on each food.
        """
        return self.pk_voted

    def set_user_rate(self, value):
        """
        Add rate from user into database.

        Args:
            value (int): rate from user which can be [20, 40, 60, 80, 100].
        """
        self.user_rate = float(self.user_rate)+value

    def set_total_rate(self):
        """
        Set total rate of food which computes from rate in the database and rate from user by 80:20 percent respectively.

        Returns:
            Decimal: total rate of food(0-100) which computes from rate in the database and rate from user.
        """
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
        """
        Get food's rate which computes from rate in the database and rate from user.

        Returns:
            Decimal: food's rate(0-100) from rate in the database and rate from user.
        """
        return self.total_rate

    def get_original_rate(self):
        """
        Get food's rate from the database.

        Returns:
            Decimal: food's rate(0-100) from the database.
        """
        return self.original_rate

    def get_user_rate(self):
        """
        Get food's rate from users.

        Returns:
            Decimal: food's rate from users.
        """
        return self.user_rate

    def get_user_count(self):
        """
        Get number of users that voted on the food.

        Returns:
            int: number of users that voted on the food.
        """
        return self.user_count

    def get_ethnic_food_name(self):
        """
        Get all ethnic foods.

        Returns:
            EthnicFood: all ethnic foods.
        """
        return self.ethnic_food_name

    def get_category(self):
        """
        Get all categories of food.

        Returns:
            ManyRelatedManager: categories of food.
        """
        return self.category

    def set_check_false(self):
        """
        Set voteable's status for each food to be False (cannot vote).
        """
        self.check_vote = False

    def set_check_true(self):
        """
        Set voteable's status for each food to be True (can vote).
        """
        self.check_vote = True

    def get_check_vote(self):
        """
        Get voteable's status for each food.

        Returns:
            bool: True if voteable and False if otherwise.
        """
        return self.check_vote

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"
