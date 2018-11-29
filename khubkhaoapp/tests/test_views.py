from django.contrib.auth.models import User
from social_django.compat import reverse
from django.test import TestCase, Client


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
        Test IndexView is Post request. So rate_star is exits. 
        '''
        c = Client()
        data = {'rate_star' : 'ONE'}
        response = c.post('/khubkhao/',data)
        self.assertEqual(response.status_code,200)


    def test_post_resutl(self):
        '''
        Test IndexResultView is Post request. So category_name and ethnic_name are exits. 
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
