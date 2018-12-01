from django.test import TestCase
from khubkhaoapp.models import Category, EthnicFood, Food


class CategoryModelTest(TestCase):

    def setUp(self):
        """
        Setup by create Category objects.
        """
        Category.objects.create(type_name="Rice dish")
        Category.objects.create(type_name="Healthy food")

    def test_create_category(self):
        """
        Test that the Category objects which have been setup is created.
        """
        self.assertEqual(2, Category.objects.count())

    def test_category_text(self):
        """
        Test that the Category objects have correct detail.
        """
        self.assertTrue(Category.objects.filter(type_name="Rice dish"))


class EthnicFoodModelTest(TestCase):

    def setUp(self):
        """
        Setup by create EthnicFood objects.
        """
        EthnicFood.objects.create(ethnic_food_name="Thai Food")
        EthnicFood.objects.create(ethnic_food_name="Korean food")

    def test_create_ethnicFood(self):
        """
        Test that the EthnicFood objects which have been setup is created.
        """
        self.assertEqual(2, EthnicFood.objects.count())

    def test_ethnicFood_text(self):
        """
        Test that the EthnicFood objects have correct detail.
        """
        self.assertTrue(EthnicFood.objects.filter(ethnic_food_name="Thai Food"))


class FoodModelTest(TestCase):
    
    def setUp(self):
        """
        Setup by create Food objects.
        """
        Food.objects.create(food_name = "Baozi",
            image_location = "http://drive.google.com/uc?export=view&id=1zbH52fRGRqMGRMSnEi2BGTU4D--Gkoy5",
            average_price = 3.1,
            original_rate = 80,
            user_rate = 0,
            pk_voted = '1,6,7,',
            user_count = 3,
            ethnic_food_name = EthnicFood.objects.create(ethnic_food_name="Thai Food"),
            )

        Food.objects.create(food_name = "Baccalà Fritto",
            image_location = "http://drive.google.com/uc?export=view&id=1PE5CjdMzCwx-FMHEjNRunXBqhRfo34dS",
            average_price = 22.84,
            original_rate = 78,
            user_rate = 0,
            ethnic_food_name = EthnicFood.objects.create(ethnic_food_name="Korean food"),
            )


    def test_create_food(self):
        """
        Test that the Food objects which have been setup is created.
        """
        self.assertEqual(2, Food.objects.count())

    def test_string_of_food_name_representation(self):
        """
        Test that a Food object contains correct value of food_name.
        """
        self.assertTrue(Food.objects.filter(food_name="Baozi"))

    def test_string_of_image_location_representation(self):
        """
        Test that a Food object contains correct value of image_location.
        """
        self.assertTrue(Food.objects.filter(image_location="http://drive.google.com/uc?export=view&id=1zbH52fRGRqMGRMSnEi2BGTU4D--Gkoy5"))

    def test_value_of_average_price_representation(self):
        """
        Test that a Food object contains correct value of average_price.
        """
        self.assertTrue(Food.objects.filter(average_price=3.1))

    def test_value_of_original_rate_representation(self):
        """
        Test that a Food object contains correct value of original_rate.
        """
        self.assertTrue(Food.objects.filter(original_rate=80))

    def test_value_of_user_rate_representation(self):
        """
        Test that a Food object contains correct value of user_rate.
        """
        self.assertTrue(Food.objects.filter(user_rate=0))

    def test_objects_of_ethnic_food_name_representation(self):
        """
        Test that a Food object contains correct value of ForeignKey for ethnic_food_name.
        """
        ethnic_food = EthnicFood.objects.all().first()
        self.assertTrue(Food.objects.filter(ethnic_food_name=ethnic_food))

    def test_ManyToMany_of_category_representation(self):
        """
        Test that ManyToMany of category in Food models show all categories which have been created.
        """
        category1 = Category(type_name='Rice')
        category1.save()
        category2 = Category(type_name='Healthy')
        category2.save()
        food = Food.objects.all().first()
        food.category.add(category1)
        food.category.add(category2)
        self.assertEqual(list(food.category.all()), [category1, category2])

    def test_add_user_pk_method(self):
        """
        Test that Food object contains correct primary key of users.
        In this test, Food name Baozi have 3 pk_vote which are 1,6,7.
        If add primary key with value of 3, it'll be equal to 1,6,7,3,.
        """
        food = Food.objects.all().first()
        food.add_user_pk('3')
        self.assertEqual(food.get_user_pk(),'1,6,7,3,')

    def test_add_user_count_method(self):
        """
        Test that the amounnt of voted user is correct.
        In this test, Food name Baozi have 3 people vote.
        If user added one more vote to the food, it'll increase the value to be 4.
        """
        food = Food.objects.all().first()
        food.add_user_count()
        self.assertEqual(food.get_user_count(),4)

    def test_one_user_vote(self):
        """
        Test that the computed rate is correct.
        In this test, Food name Baccalà Fritto have original rate 78.
        If user rate is 80, then the total rate of this food is 78.4.
        """
        food = Food.objects.all().last()
        food.set_user_rate(80)
        rate = food.set_total_rate()
        self.assertEqual(rate,78.4)

    def test_multiple_users_vote(self):
        """
        Test that the computed rate from multiple users is correct.
        In this test, Food name Baozi has 3 user votes and origingal rate is 80.
        If total for users rate is 120, then the total rate after computed will be 72.
        """
        food = Food.objects.all().first()
        food.set_user_rate(120)

        rate = food.set_total_rate()
        self.assertEqual(rate,72)


class FixturesTest(TestCase):
    fixtures = ['seed.json']

    def test_pk_category_representation(self):
        """
        Test that seed can send the correct data of Category object.
        """
        category = Category.objects.get(pk=5)
        self.assertTrue(Category.objects.filter(type_name='Healthy food'))

    def test_pk_ethnic_representation(self):
        """
        Test that seed can send the correct data of EthnicFood object.
        """
        ethnic = EthnicFood.objects.get(pk=101)
        self.assertTrue(EthnicFood.objects.filter(ethnic_food_name='Chinese food'))

    def test_pk_food_all_componet_representation(self):
        """
        Test that seed can send the correct data of Food object.
        """
        food = Food.objects.get(pk=1001)
        self.assertEqual(list(food.get_category().all()),[Category.objects.get(pk=5),Category.objects.get(pk=7),Category.objects.get(pk=8)])
        self.assertTrue(Food.objects.filter(food_name='Bak Kut Teh'))
        self.assertTrue(Food.objects.filter(image_location='http://drive.google.com/uc?export=view&id=1vWtl_ugPgkcZnEgVm7NcPGV-5EUl9kJw'))
        self.assertTrue(Food.objects.filter(average_price='6.5'))
        self.assertTrue(Food.objects.filter(original_rate='80'))
