from django.test import TestCase
from khubkhaoapp.models import Category, EthnicFood, Food


class CategoryModelTest(TestCase):

    def test_string_representation(self):
        ''' Charfield of type_name in Category models is equal to category '''
        category = Category(type_name='Rice')
        self.assertEqual(str(category),category.type_name)

class EthnicFoodModelTest(TestCase):

    def test_string_representation(self):
        ''' Charfield of ethnic_food_name in Ethnic models is equal to ethnic_food '''
        ethnic_food = EthnicFood(ethnic_food_name='ThaiFood')
        self.assertEqual(str(ethnic_food),ethnic_food.ethnic_food_name)

class FoodModelTest(TestCase):

    def test_string_of_food_name_representation(self):
        ''' Charfield of food_name in Food models is equal to name '''
        name = Food(food_name='Jok')
        self.assertEqual(str(name),name.food_name)

    def test_string_of_image_location_representation(self):
        ''' Charfield of image_location in Food models is equal to text '''
        text = Food(image_location='/home/test')
        self.assertEqual(Food.get_image_location(text),text.image_location)

    def test_intenger_of_average_price_representation(self):
        ''' DecimalField of average_price in Food models is equal to baht '''
        baht = Food(average_price=10)
        self.assertEqual(Food.get_average_price(baht),baht.average_price)

    def test_intenger_of_original_rate_representation(self):
        ''' DecimalField of original_rate Food models is equal to number '''
        number = Food(original_rate=10)
        self.assertEqual(Food.get_original_rate(number),number.original_rate)

    def test_intenger_of_user_rate_representation(self):
        ''' DecimalField of user_rate Food models is equal to number '''
        number = Food(user_rate=10)
        self.assertEqual(Food.get_user_rate(number),number.user_rate)

    def test_objects_of_ethnic_food_name_representation(self):
        ''' ForeignKey of ethnic_food_name in Food models is equal to ethnic_Food '''
        ethnic_food = EthnicFood(ethnic_food_name='JapanFood')
        text = Food(ethnic_food_name=ethnic_food)
        self.assertEqual(Food.get_ethnic_food_name(text),text.ethnic_food_name)

    def test_ManyToMany_of_category_representation(self):
        ''' ManyToMany of category in Food models is relete on field of Category '''
        category1 = Category(type_name='Rice')
        category1.save()
        category2 = Category(type_name='Healthy')
        category2.save()
        ethnic_food = EthnicFood(ethnic_food_name='ThaiFood')
        ethnic_food.save()
        food = Food(food_name='Jok',ethnic_food_name=ethnic_food)
        food.save()
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