from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

class ViewPageTest(TestCase):
    
    def setUp(self):
        self.status = list()
        self.status.append(200)
        self.status.append(301)

    def test_home_page_status_code(self):
        ''' Check url is exits '''
        response = self.client.get('/')
        self.assertIn(response.status_code, self.status)

    def test_view_uses_correct_template(self):
        ''' Check index.html is a template of url('/') '''
        response = self.client.get(reverse('khubkhaoapp:index'))
        self.assertIn(response.status_code, self.status)
        self.assertTemplateUsed(response, 'khubkhaoapp/index.html')

    def test_result_page_status_code(self):
        ''' Check url is exits '''
        response = self.client.get('/result')
        self.assertIn(response.status_code, self.status)

    def test_khubkhao_page_status_code(self):
        ''' Check url is exits '''
        response = self.client.get('/khubkhao')
        self.assertIn(response.status_code, self.status)

    def test_vote_page_status_code(self):
        ''' Check url is exits '''
        response = self.client.get('/vote')
        self.assertIn(response.status_code, self.status)

    def test_login_page_status_code(self):
        ''' Check url is exits '''
        response = self.client.get('/login')
        self.assertIn(response.status_code, self.status)

    def test_logout_page_status_code(self):
        ''' Check url is exits '''
        response = self.client.get('/logout')
        self.assertIn(response.status_code, self.status)

    
