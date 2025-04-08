import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Base import InitiateDriver

class TestLoginFailedDoNotFillPassword(unittest.TestCase):
    
    def setUp(self):
        self.browser = InitiateDriver.StartBrowser()
        
    def test_failed_login(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, "user-name").send_keys('standard_user')
        browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('')

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Verifikasi login failed dengan URL assertion
        error_message = browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
        self.assertIn('Password is required', error_message)

        print("Website logged in failed because Do not fill password")
   
    def tearDown(self):
        InitiateDriver.CloseBrowser()

class TestLoginFailedDoNotFillUsername(unittest.TestCase):
    
    def setUp(self):
        self.browser = InitiateDriver.StartBrowser()
        
    def test_failed_login(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, "user-name").send_keys('')
        browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('wrong password')

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Verifikasi login failed dengan URL assertion
        error_message = browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
        self.assertIn('Username is required', error_message)

        print("Website logged in failed because Do not fill username")

   
    def tearDown(self):
        InitiateDriver.CloseBrowser()


class TestLoginFailedDoNotFillUsernameAndPassword(unittest.TestCase):
    
    def setUp(self):
        self.browser = InitiateDriver.StartBrowser()
        
    def test_failed_login(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, "user-name").send_keys('')
        browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('')

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Verifikasi login failed dengan URL assertion
        error_message = browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
        self.assertIn('Username is required', error_message)

        print("Website logged in failed because Do not fill username and password")

   
    def tearDown(self):
        InitiateDriver.CloseBrowser()

class TestLoginFailedWrongPassword(unittest.TestCase):
    
    def setUp(self):
        self.browser = InitiateDriver.StartBrowser()
        
    def test_failed_login(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, "user-name").send_keys('standard_user')
        browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('wrong password')

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Verifikasi login failed dengan URL assertion
        error_message = browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
        self.assertIn('Username and password do not match', error_message)

        print("Website logged in failed because Wrong Password")

    def tearDown(self):
        InitiateDriver.CloseBrowser()

class TestLoginFailedWrongUsername(unittest.TestCase):
    
    def setUp(self):
        self.browser = InitiateDriver.StartBrowser()
        
    def test_failed_login(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, "user-name").send_keys('wrong username')
        browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('secret_sauce')

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Verifikasi login failed dengan URL assertion
        error_message = browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
        self.assertIn('Username and password do not match any user in this service', error_message)

        print("Website logged in failed because Wrong Username")

    def tearDown(self):
        InitiateDriver.CloseBrowser()

class TestLoginFailedWrongUsernameandWrongPassword(unittest.TestCase):
    
    def setUp(self):
        self.browser = InitiateDriver.StartBrowser()
        
    def test_failed_login(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, "user-name").send_keys('wrong username')
        browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('wrong password')

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Verifikasi login failed dengan URL assertion
        error_message = browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
        self.assertIn('Username and password do not match any user in this service', error_message)

        print("Website logged in failed because Wrong Username and Wrong Password")

    def tearDown(self):
        InitiateDriver.CloseBrowser()




if __name__ == '__main__':
    unittest.main()