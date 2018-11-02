from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse


class IndexPageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'khubkhaoapp/index.html')

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>KhubKhao Recommender</title>')

    def test_home_page_does_not_contains_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'This should not be on the page.')

    