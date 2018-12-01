from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class EthnicFood(models.Model):
    """EthnicFood class represents ethnic's name on dish food country.

    Attributes:
        models.Model(Model): source of information. It contains the essential fields and behaviors of the data you’re storing.
    """
    ethnic_food_name = models.CharField(
        max_length=20,
        verbose_name='Ethnic food',
        unique=True,
        blank=False,
        help_text='Enter ethnic food name'
    )

    def __str__(self):
        """Override to print a readable string presentation of ethnic.

        Returns:
            str: ethnic's name.
        """
        return self.ethnic_food_name

    class Meta:
        verbose_name = "Ethnic food"
        verbose_name_plural = "Ethnic foods"


class Category(models.Model):
    """Category class represents category's name on dish food type.

    Attributes:
        models.Model(Model): source of information. It contains the essential fields and behaviors of the data you’re storing.
    """
    type_name = models.CharField(
        max_length=20,
        verbose_name='Category name',
        unique=True,
        blank=False,
        help_text='Enter Category name'
    )

    def __str__(self):
        """Override to print a readable string presentation of category.

        Returns:
            str: category's name.
        """
        return self.type_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Food(models.Model):
    """Food class represents informations and details of dish food.

    Food class represents name, image url, average price, rate, category, and ethnic of dish food 
    which can compute rate of food from user and database by itself.

    Attributes:
        models.Model(Model): source of information. It contains the essential fields and behaviors of the data you’re storing.
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
        """Override to print a readable string presentation of food.

        Returns:
            str: food's name.
        """
        return self.food_name

    def get_average_price(self):
        """Get average price of dish food.

        Returns:
            Decimal: average price of dish food.
        """
        return self.average_price

    def get_image_location(self):
        """Get image url of dish food.

        Returns:
            str: image url of dish food.
        """
        return self.image_location

    def add_user_count(self):
        """
        Count the number of user who already voted any dish food to database by adding one for each user.
        """
        self.user_count = float(self.user_count)+1

    def add_user_pk(self, primary_key):
        """Add user's primary key which already voted any dish food to database.

        Args:
            primary_key (str): user's primary key.
        """
        self.pk_voted = self.pk_voted + str(primary_key) + ","

    def get_user_pk(self):
        """Get all primary keys of user which has been voted on dish food.

        Returns:
            str: all primary keys of user which has been voted on dish food.
        """
        return self.pk_voted

    def set_user_rate(self, value):
        """Add user's rate points to database.

        Args:
            value (int): user's rate points which can be [20,40,60,80,100].
        """
        self.user_rate = float(self.user_rate)+value

    def set_total_rate(self):
        """Set food's total rate points which computes from user's rate and database's rate by 80:20 percentage respectively.

        Returns:
            Decimal: food's rate points(0-100) which computes from user's rate and database's rate.
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
        """Get food's rate points which computes from user's rate and database's rate.

        Returns:
            Decimal: food's rate points(0-100) from user's rate and database's rate.
        """
        return self.total_rate

    def get_original_rate(self):
        """Get food's rate points from database.

        Returns:
            Decimal: food's rate points(0-100) from database.
        """
        return self.original_rate

    def get_user_rate(self):
        """Get food's rate points from users.

        Returns:
            Decimal: food's rate points from users which can be zero to infinity.
        """
        return self.user_rate

    def get_user_count(self):
        """Get number of users have voted on dish food.

        Returns:
            int: number of users have voted on dish food.
        """
        return self.user_count

    def get_ethnic_food_name(self):
        """Get all ethnic names in dish food.

        Returns:
            EthnicFood: all ethnic names in dish food.
        """
        return self.ethnic_food_name

    def get_category(self):
        """Get all categories in dish food.

        Returns:
            ManyRelatedManager: categories in dish food.
        """
        return self.category

    def set_check_false(self):
        """
        Set voteable's status for each dish food can't be voted.
        """
        self.check_vote = False

    def set_check_true(self):
        """
        Set voteable's status for each dish food can be voted.
        """
        self.check_vote = True

    def get_check_vote(self):
        """Get voteable's status for each dish food.

        Returns:
            bool: True if successful(voteable), False otherwise(unvoteable).
        """
        return self.check_vote

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"
