from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

class IndexPageTest(TestCase):

    def test_home_page_status_code(self):
        ''' Check url is exits '''
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        ''' Check index.html is a template of url('/') '''
        response = self.client.get(reverse('khubkhaoapp:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'khubkhaoapp/index.html')