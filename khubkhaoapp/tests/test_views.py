from django.contrib.auth.models import User
from social_django.compat import reverse
from django.test import TestCase

class TestViews(TestCase):
    def setUp(self):
        User.objects.create_superuser('tester', 'tester@faker.com', '123456')
        self.client.login(username='admin', password='admin')

        session = self.client.session
        session['documents_to_share_ids'] = [1]
        session.save()

    def test_authenticated(self):
        self.assertTrue(User.is_authenticated)


    def test_views_login(self):
        response = self.client.get(reverse('social:begin', kwargs={'backend': 'facebook'}))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('social:begin', kwargs={'backend': 'github'}))
        self.assertEqual(response.status_code, 404)


    
