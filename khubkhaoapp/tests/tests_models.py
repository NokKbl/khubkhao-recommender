from django.test import TestCase
from khubkhaoapp.models import Category, EthnicFood, Food



class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(type_name="Rice dish")
        Category.objects.create(type_name="Healthy food")
        
    def test_create_category(self):
        '''Check Category that have been setup is create'''
        self.assertEqual(2, Category.objects.count())

    def test_category_text(self):
        '''Check Category have text same as objects that have been setup'''
        self.assertTrue(Category.objects.filter(type_name="Rice dish"))

class EthnicFoodModelTest(TestCase):
    def setUp(self):
        EthnicFood.objects.create(ethnic_food_name="Thai Food")
        EthnicFood.objects.create(ethnic_food_name="Korean food")

    def test_create_ethnicFood(self):
        '''Check EthnicFood that have been setup is create'''
        self.assertEqual(2, EthnicFood.objects.count())

    def test_ethnicFood_text(self):
        '''Check EthnicFood have text same as objects that have been setup'''
        self.assertTrue(EthnicFood.objects.filter(ethnic_food_name="Thai Food"))

class FoodModelTest(TestCase):
    
    def setUp(self):
        Food.objects.create(food_name = "Baozi",
            image_location = "http://drive.google.com/uc?export=view&id=1zbH52fRGRqMGRMSnEi2BGTU4D--Gkoy5",
            average_price = 3.1,
            original_rate = 80,
            user_rate = 0,
            pk_voted = '1,6,',
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
        '''Check EthnicFood that have been setup is create'''
        self.assertEqual(2, Food.objects.count())

    def test_string_of_food_name_representation(self):
        ''' Charfield of food_name in Food models have same string that create in setup '''
        self.assertTrue(Food.objects.filter(food_name="Baozi"))

    def test_string_of_image_location_representation(self):
        ''' Charfield of image_location in Food models have same string that create in setup '''
        self.assertTrue(Food.objects.filter(image_location="http://drive.google.com/uc?export=view&id=1zbH52fRGRqMGRMSnEi2BGTU4D--Gkoy5"))

    def test_integer_of_average_price_representation(self):
        ''' DecimalField of average_price in Food models have same integer that create in setup '''
        self.assertTrue(Food.objects.filter(average_price=3.1))

    def test_integer_of_original_rate_representation(self):
        ''' DecimalField of original_rate Food models have same integer that create in setup '''
        self.assertTrue(Food.objects.filter(original_rate=80))

    def test_integer_of_user_rate_representation(self):
        ''' DecimalField of user_rate Food models have same integer that create in setup '''
        self.assertTrue(Food.objects.filter(user_rate=0))

    def test_objects_of_ethnic_food_name_representation(self):
        ''' ForeignKey of ethnic_food_name in Food models have same objects that create in setup '''
        ethnic_food = EthnicFood.objects.all().first()
        self.assertTrue(Food.objects.filter(ethnic_food_name=ethnic_food))

    def test_ManyToMany_of_category_representation(self):
        ''' ManyToMany of category in Food models is relate on field of Category '''
        category1 = Category(type_name='Rice')
        category1.save()
        category2 = Category(type_name='Healthy')
        category2.save()
        food = Food.objects.all().first()
        food.category.add(category1)
        food.category.add(category2)
        self.assertEqual(list(food.category.all()), [category1, category2])

    def test_add_user_pk_method(self):
        ''' Food name Baozi have 2 pk_vote which is 1,6 then add pk=3. So it equal to 1,6,3, '''
        food = Food.objects.all().first()
        food.add_user_pk('3')
        self.assertEqual(food.get_user_pk(),'1,6,3,')
    
    def test_add_user_count_method(self):
        ''' Food name Baozi have 3 people vote. User add one more vote to food. So it increase to 4'''
        food = Food.objects.all().first()
        food.add_user_count()
        self.assertEqual(food.get_user_count(),4)

    def test_one_user_vote(self):
        ''' Food name Baccalà Fritto have original rate 78, user rate is set to 80 so total rate is 78.4  '''
        food = Food.objects.all().last()
        food.set_user_rate(80)
        rate = food.compute_total_rate()
        self.assertEqual(rate,78.4)

    def test_many_user_vote(self):
        ''' Food name Baozi have 3 vote, origingal rate is 80, all user rate is 120. The total rate is 72  '''
        food = Food.objects.all().first()
        food.set_user_rate(120)

        rate = food.compute_total_rate()
        self.assertEqual(rate,72)
        

class FixturesTest(TestCase):
    fixtures = ['seed.json']

    def test_pk_category_representation(self):
        ''' seed can be sending data of Category  '''
        category = Category.objects.get(pk=5)
        self.assertTrue(Category.objects.filter(type_name='Healthy food'))

    def test_pk_ethnic_representation(self):
        ''' seed can be sending data of EthnicFood '''
        ethnic = EthnicFood.objects.get(pk=101)
        self.assertTrue(EthnicFood.objects.filter(ethnic_food_name='Chinese food'))

    def test_pk_food_all_componet_representation(self):
        ''' seed can be sending data of Food '''
        food = Food.objects.get(pk=1001)
        self.assertEqual(list(food.get_category().all()),[Category.objects.get(pk=5),Category.objects.get(pk=7),Category.objects.get(pk=8)])
        self.assertTrue(Food.objects.filter(food_name='Bak Kut Teh'))
        self.assertTrue(Food.objects.filter(image_location='http://drive.google.com/uc?export=view&id=1vWtl_ugPgkcZnEgVm7NcPGV-5EUl9kJw'))
        self.assertTrue(Food.objects.filter(average_price='6.5'))
        self.assertTrue(Food.objects.filter(original_rate='80'))