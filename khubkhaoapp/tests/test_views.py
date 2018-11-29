from django.contrib.auth.models import User
from social_django.compat import reverse
from django.test import TestCase, Client
from khubkhaoapp.models import Food, Category, EthnicFood
from khubkhaoapp import views




class TestViews(TestCase):


    def setUp(self):
        '''
        Create a fake user.
        '''
        User.objects.create_superuser('tester', 'tester@faker.com', '123456')
        self.client.login(username='admin', password='admin')


    def test_user_login(self):
        '''
        Test that User have been login to webpage.
        In this method, return True if user was logged in.
        '''
        self.assertTrue(User.is_authenticated)


    def test_authentication_backends(self):
        '''
        Test that socail-auth-app-django contain authentication backends in setting.py.
        In this method, response is equal 302 if authentication is contain in setting else equal 404.
        '''
        response = self.client.get(reverse('social:begin', kwargs={'backend': 'facebook'}))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('social:begin', kwargs={'backend': 'github'}))
        self.assertEqual(response.status_code, 404)


    def test_post_index(self):
        '''
        Test that Post request in IndexView. So rate_star is exist. 
        '''
        c = Client()
        data = {'rate_star' : 'ONE'}
        response = c.post('/khubkhao/',data)
        self.assertEqual(response.status_code,200)


    def test_post_resutl(self):
        '''
        Test that Post request in IndexResultView. So category_name and ethnic_name are exist. 
        '''
        c = Client()
        data = {'category_name' : 4}
        response = c.post('/result/',data)
        self.assertEqual(response.status_code,200)

        data = {'ethnic_name' : 101}
        response = c.post('/result/',data)
        self.assertEqual(response.status_code,200)

        data = {'category_name' : 4,'ethnic_name' : 101}
        response = c.post('/result/',data)
        self.assertEqual(response.status_code,200)

    def test_sort_food(self):
        '''
        Test that foods are sorting correctly.
        '''
        food_correct = '[<Food: Albóndigas>, <Food: Jok>, <Food: Bak Kut Teh>, <Food: Broccolini Gomaa>]'

        Food.objects.create(food_name = "Bak Kut Teh",#68
            original_rate = 80,
            user_rate = 20,
            ethnic_food_name = EthnicFood.objects.create(ethnic_food_name="Chinese Food"),
            )
        
        Food.objects.create(food_name = "Albóndigas",#72
            original_rate = 65,
            user_rate = 100,
            ethnic_food_name = EthnicFood.objects.create(ethnic_food_name="Mexican food"),
            )

        Food.objects.create(food_name = "Jok",#70.4
            original_rate = 78,
            user_rate = 40,
            ethnic_food_name = EthnicFood.objects.create(ethnic_food_name="Thai food"),
            )
        
        Food.objects.create(food_name = "Broccolini Gomaa",#60
            original_rate = 70,
            user_rate = 20,
            ethnic_food_name = EthnicFood.objects.create(ethnic_food_name="Japanese food"),
            )

        food_list = Food.objects.all()
        self.assertNotEqual(str(list(food_list)),food_correct)
        
        food_list_sorted = views.sort_food(food_list)
        self.assertEqual(str(food_list_sorted),food_correct)
        