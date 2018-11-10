from django.test import TestCase
from khubkhaoapp.models import Category, EthnicFood, Food


class CategoryModelTest(TestCase):

    def test_string_representation(self):
        '''Test Charfield of Category models(String:Type name) '''
        category = Category(type_name='Rice')
        self.assertEqual(str(category),category.type_name)

class EthnicFoodModelTest(TestCase):

    def test_string_representation(self):
        '''Test Charfield of Ethnic models(String:Country name) '''
        ethnic_food = EthnicFood(ethnic_food_name='ThaiFood')
        self.assertEqual(str(ethnic_food),ethnic_food.ethnic_food_name)

class FoodModelTest(TestCase):

    def test_string_of_food_name_representation(self):
        '''Test Charfield of Food models(String:Food name) '''
        name = Food(food_name='Jok')
        self.assertEqual(str(name),name.food_name)

    def test_string_of_image_location_representation(self):
        '''Test Charfield of Food models(String:URL) '''
        text = Food(image_location='/home/test')
        self.assertEqual(Food.get_image_location(text),text.image_location)

    def test_intenger_of_average_price_representation(self):
        '''Test DecimalField of Food models(Integer:average price of food) '''
        baht = Food(average_price=10)
        self.assertEqual(Food.get_average_price(baht),baht.average_price)

    def test_intenger_of_original_rate_representation(self):
        '''Test DecimalField of Food models(Integer:default rate) '''
        number = Food(original_rate=10)
        self.assertEqual(Food.get_original_rate(number),number.original_rate)

    def test_intenger_of_user_rate_representation(self):
        '''Test DecimalField of Food models(Integer:user rate) '''
        number = Food(user_rate=10)
        self.assertEqual(Food.get_user_rate(number),number.user_rate)

    def test_objects_of_ethnic_food_name_representation(self):
        '''Test ForeignKey of Food models(Objects:Ethnic Food) '''
        ethnic_food = EthnicFood(ethnic_food_name='JapanFood')
        text = Food(ethnic_food_name=ethnic_food)
        self.assertEqual(Food.get_ethnic_food_name(text),text.ethnic_food_name)

    def test_ManyToMany_of_category_representation(self):
        '''Test ManyToManyField of Food models(Check Food can be relete on field of Category) '''
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
        '''Test call able pk of database'''
        category = Category.objects.get(pk=5)
        self.assertEqual(str(category),'Healthy food')

    def test_pk_ethnic_representation(self):
        '''Test call able pk of database'''
        ethnic = EthnicFood.objects.get(pk=101)
        self.assertEqual(str(ethnic),'Chinese food')

    def test_pk_food_all_componet_representation(self):
        '''Test call able pk of database and check food contain correct parameter'''
        food = Food.objects.get(pk=1001)
        self.assertEqual(str(food),'Bak Kut Teh')
        self.assertEqual(food.get_image_location(),'http://drive.google.com/uc?export=view&id=1vWtl_ugPgkcZnEgVm7NcPGV-5EUl9kJw')
        self.assertEqual(food.get_average_price(),6.5)
        self.assertEqual(food.get_original_rate(),80)
        self.assertEqual(food.get_ethnic_food_name(),EthnicFood.objects.get(pk=101))
        self.assertEqual(list(food.get_category().all()),[Category.objects.get(pk=5),Category.objects.get(pk=7),Category.objects.get(pk=8)])