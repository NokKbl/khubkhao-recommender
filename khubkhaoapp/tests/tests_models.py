from django.test import TestCase
from django.db import IntegrityError
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
            original_rate = 84,
            user_rate = 0,
            ethnic_food_name = EthnicFood.objects.create(ethnic_food_name="Thai Food"),
            )

        Food.objects.create(food_name = "Baccalà Fritto",
            image_location = "http://drive.google.com/uc?export=view&id=1PE5CjdMzCwx-FMHEjNRunXBqhRfo34dS",
            average_price = 22.84,
            original_rate = 78,
            user_rate = 40,
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
        self.assertTrue(Food.objects.filter(original_rate=84))

    def test_integer_original_rate_negative(self):
        ''' original_rate can't be negative'''
        with self.assertRaises(IntegrityError):
            food =  Food.objects.create(original_rate = -1)

    def test_integer_original_rate_more_then_maximum(self):
        ''' original_rate can't be more then maximum(which is 100)'''
        with self.assertRaises(IntegrityError):
            food =  Food.objects.create(original_rate = 200)

    def test_integer_of_user_rate_representation(self):
        ''' DecimalField of user_rate Food models have same integer that create in setup '''
        self.assertTrue(Food.objects.filter(user_rate=40))

    def test_integer_user_rate_negative(self):
        ''' user_rate can't be negative '''
        with self.assertRaises(IntegrityError):
            food =  Food.objects.create(user_rate = -1)

    def test_objects_of_ethnic_food_name_representation(self):
        ''' ForeignKey of ethnic_food_name in Food models have same objects that create in setup '''
        ethnic_food = EthnicFood.objects.all()[:1].get()
        self.assertTrue(Food.objects.filter(ethnic_food_name=ethnic_food))

    def test_ManyToMany_of_category_representation(self):
        ''' ManyToMany of category in Food models is relate on field of Category '''
        category1 = Category(type_name='Rice')
        category1.save()
        category2 = Category(type_name='Healthy')
        category2.save()
        food = Food.objects.all()[:1].get()
        food.category.add(category1)
        food.category.add(category2)
        self.assertEqual(list(food.category.all()), [category1, category2])

class FixturesTest(TestCase):
    fixtures = ['seed.json']

    def test_pk_category_representation(self):
        ''' seed can be sending data of Category  '''
        category = Category.objects.get(pk=5)
        self.assertEqual(str(category),'Healthy food')

    def test_pk_ethnic_representation(self):
        ''' seed can be sending data of EthnicFood '''
        ethnic = EthnicFood.objects.get(pk=101)
        self.assertEqual(str(ethnic),'Chinese food')

    def test_pk_food_all_componet_representation(self):
        ''' seed can be sending data of Food '''
        food = Food.objects.get(pk=1001)
        self.assertEqual(str(food),'Bak Kut Teh')
        self.assertEqual(food.get_image_location(),'http://drive.google.com/uc?export=view&id=1vWtl_ugPgkcZnEgVm7NcPGV-5EUl9kJw')
        self.assertEqual(food.get_average_price(),6.5)
        self.assertEqual(food.get_original_rate(),80)
        self.assertEqual(food.get_ethnic_food_name(),EthnicFood.objects.get(pk=101))
        self.assertEqual(list(food.get_category().all()),[Category.objects.get(pk=5),Category.objects.get(pk=7),Category.objects.get(pk=8)])
