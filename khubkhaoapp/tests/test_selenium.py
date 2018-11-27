from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from unittest import TestCase

class UntitledTestCase(TestCase):
    
    def setUp(self):
        '''setup chromedriver to run headless and login to website'''
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(30)
        
        self.driver.get("https://khubkhao-rec.herokuapp.com/")
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=concat('Don', \"'\", 't have an account? Sign Up!')])[1]/following::button[2]").click()
        self.driver.find_element_by_id("username_or_email").clear()
        self.driver.find_element_by_id("username_or_email").send_keys("devtester018@gmail.com")
        self.driver.find_element_by_id("password").click()
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("DevTester2018")
        self.driver.find_element_by_id("allow").click()
    
    def test_only_ethnic_check(self):
        ''' Result of food after select ethnic is in database 
            this test is select ethnic:Chinese food.
        '''
        food_all = list()
        driver = self.driver
        driver.get("https://khubkhao-rec.herokuapp.com/khubkhao/")  
        driver.find_element_by_id("ethnic1").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Side dish'])[1]/following::input[1]").click()
        
        elements = driver.find_elements_by_id('Food_name')
        for element in elements:
            food_all.append(element.get_attribute('innerHTML'))
        self.assertIn("Beef Chow Fun",food_all)
        driver.close()

    def test_only_category_check(self):
        ''' Result of food after select category is in database 
            this test is select category:Rice dish.
        '''
        food_all = list()
        driver = self.driver
        driver.get("https://khubkhao-rec.herokuapp.com/khubkhao/") 
        driver.find_element_by_id("category1").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Side dish'])[1]/following::input[1]").click()
        
        elements = driver.find_elements_by_id('Food_name')
        for element in elements:
            food_all.append(element.get_attribute('innerHTML'))
        self.assertIn("Arancini (Rice Ball)",food_all)
        
        driver.close()

    def test_ethnic_and_category_check(self):
        ''' Result of food after select ethnic and category is in database
            this test is select ethnic:Chinese food and category:Noodles dish.
        '''
        food_all = list()
        driver = self.driver
        driver.get("https://khubkhao-rec.herokuapp.com/khubkhao/")  
        driver.find_element_by_id("ethnic1").click()
        driver.find_element_by_id("category2").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Side dish'])[1]/following::input[1]").click()
        
        elements = driver.find_elements_by_id('Food_name')
        for element in elements:
            food_all.append(element.get_attribute('innerHTML'))
        self.assertIn("Beef Chow Fun",food_all)
        
        driver.close()

    def test_ethnic_and_multiple_category_check(self):
        ''' Result of food after select ethnic and multiple category is in database
            this test is select ethnic:Chinese food and category:Healthy food, Vegetarian food, Side dish.
        '''
        food_all = list()
        driver = self.driver
        driver.get("https://khubkhao-rec.herokuapp.com/khubkhao/")  
        driver.find_element_by_id("ethnic1").click()
        driver.find_element_by_id("category5").click()
        driver.find_element_by_id("category6").click()
        driver.find_element_by_id("category8").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Side dish'])[1]/following::input[1]").click()
        
        elements = driver.find_elements_by_id('Food_name')
        for element in elements:
            food_all.append(element.get_attribute('innerHTML'))
        self.assertIn("Baozi",food_all)
        
        driver.close()
