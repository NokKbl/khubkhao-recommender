from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse


class ViewPageTest(TestCase):
    
    def setUp(self):
        '''
        Setup list of possible valid status.
        '''
        self.status = list()
        self.status.append(200)
        self.status.append(301)


    def test_home_page_status_code(self):
        '''
        Test that the webpage URL is exist.
        '''
        response = self.client.get('/')
        self.assertIn(response.status_code, self.status)


    def test_view_uses_correct_template(self):
        '''
        Test that the webpage exist and used correct template.
        '''
        response = self.client.get(reverse('khubkhaoapp:index'))
        self.assertIn(response.status_code, self.status)
        self.assertTemplateUsed(response, 'khubkhaoapp/index.html')


    def test_result_page_status_code(self):
        '''
        Test that the result page URL is exist.
        '''
        response = self.client.get('/result')
        self.assertIn(response.status_code, self.status)


    def test_khubkhao_page_status_code(self):
        '''
        Test that the homepage URL is exist.
        '''
        response = self.client.get('/khubkhao')
        self.assertIn(response.status_code, self.status)


    def test_login_page_status_code(self):
        '''
        Test that the login page URL is exist.
        '''
        response = self.client.get('/login')
        self.assertIn(response.status_code, self.status)


    def test_logout_page_status_code(self):
        '''
        Test that the logout page URL is exist.
        '''
        response = self.client.get('/logout')
        self.assertIn(response.status_code, self.status)
