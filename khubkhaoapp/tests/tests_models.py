from django.test import TestCase
from khubkhaoapp.models import Category, EthnicFood, Food


class CategoryModelTest(TestCase):

    def test_string_representation(self):
        category = Category(type_name='Rice')
        self.assertEqual(str(category),category.type_name)

class EthnicFoodModelTest(TestCase):

    def test_string_representation(self):
        ethnic_food = EthnicFood(ethnic_food_name='ThaiFood')
        self.assertEqual(str(ethnic_food),ethnic_food.ethnic_food_name)

class FoodModelTest(TestCase):

    def test_string_of_food_name_representation(self):
        name = Food(food_name='Jok')
        self.assertEqual(str(name),name.food_name)

    def test_string_of_image_location_representation(self):
        text = Food(image_location='/home/test')
        self.assertEqual(Food.get_image_location(text),text.image_location)

    def test_intenger_of_average_price_representation(self):
        baht = Food(average_price=10)
        self.assertEqual(Food.get_average_price(baht),baht.average_price)

    def test_intenger_of_rate_representation(self):
        number = Food(original_rate=10)
        self.assertEqual(Food.get_original_rate(number),number.original_rate)

    def test_objects_of_ethnic_food_name_representation(self):
        ethnic_food = EthnicFood(ethnic_food_name='JapanFood')
        text = Food(ethnic_food_name=ethnic_food)
        self.assertEqual(Food.get_ethnic_food_name(text),text.ethnic_food_name)

    def test_ManyToMany_of_category_representation(self):
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