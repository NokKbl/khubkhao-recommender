from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from unittest import TestCase

class UntitledTestCase(TestCase):
    
    def setUp(self):
        '''setup chromedriver to run headless'''
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(30)
        
        self.food_all = list()
        self.driver.get("https://khubkhao-rec.herokuapp.com/")  
        before_elements = self.driver.find_elements_by_tag_name('h3')
        for element in before_elements:
            self.food_all.append(element.get_attribute('innerHTML'))
    
    def test_only_ethnic_check(self):
        ''' Result of food after select ethnic is in database 
            this test is select ethnic:Chinese food.
        '''
        food_all = self.food_all
        driver = self.driver
        driver.get("https://khubkhao-rec.herokuapp.com/")  
        driver.find_element_by_id("ethnic1").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Side dish'])[1]/following::input[1]").click()
        
        after_elements = driver.find_elements_by_tag_name('h3')
        for element in after_elements:
            self.assertIn(element.get_attribute('innerHTML'),food_all)
        
        self.driver.close()

    def test_only_category_check(self):
        ''' Result of food after select category is in database 
            this test is select category:Rice dish.
        '''
        food_all = self.food_all
        driver = self.driver
        driver.get("https://khubkhao-rec.herokuapp.com/") 
        driver.find_element_by_id("category1").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Side dish'])[1]/following::input[1]").click()
        
        after_elements = driver.find_elements_by_tag_name('h3')
        for element in after_elements:
            self.assertIn(element.get_attribute('innerHTML'),food_all)
        
        self.driver.close()

    def test_ethnic_and_category_check(self):
        ''' Result of food after select ethnic and category is in database
            this test is select ethnic:Chinese food and category:Noodles dish.
        '''
        food_all = self.food_all
        driver = self.driver
        driver.get("https://khubkhao-rec.herokuapp.com/")  
        driver.find_element_by_id("ethnic1").click()
        driver.find_element_by_id("category2").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Side dish'])[1]/following::input[1]").click()
        
        after_elements = driver.find_elements_by_tag_name('h3')
        for element in after_elements:
            self.assertIn(element.get_attribute('innerHTML'),food_all)
        
        self.driver.close()

    def test_ethnic_and_multiple_category_check(self):
        ''' Result of food after select ethnic and multiple category is in database
            this test is select ethnic:Chinese food and category:Healthy food, Vegetarian food, Side dish.
        '''
        food_all = self.food_all
        driver = self.driver
        driver.get("https://khubkhao-rec.herokuapp.com/")  
        driver.find_element_by_id("ethnic1").click()
        driver.find_element_by_id("category5").click()
        driver.find_element_by_id("category6").click()
        driver.find_element_by_id("category8").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Side dish'])[1]/following::input[1]").click()
        
        after_elements = driver.find_elements_by_tag_name('h3')
        for element in after_elements:
            self.assertIn(element.get_attribute('innerHTML'),food_all)
        
        self.driver.close()
