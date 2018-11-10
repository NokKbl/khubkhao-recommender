from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

class IndexPageTest(TestCase):

    def test_home_page_status_code(self):
        '''Check url can open'''
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        '''Check that index.html is a template of url('/')'''
        response = self.client.get(reverse('khubkhaoapp:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'khubkhaoapp/index.html')

    def test_home_page_returns_correct_html(self):
        '''Check template contains component in index.html'''
        response = self.client.get('/')
        self.assertContains(response, '<h1>Generated Result!</h1>')

    def test_home_page_does_not_contains_incorrect_html(self):
        '''Check template does not contains component in index.html'''
        response = self.client.get('/')
        self.assertNotContains(response, 'This should not be on the page.')

