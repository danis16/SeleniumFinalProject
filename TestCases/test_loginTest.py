import unittest
from Base import InitiateDriver
from Pages import LoginPage
from Library import read_config

class TestLoginSuccess(unittest.TestCase):

    
    @classmethod
    def setUpClass(cls):
        cls.browser = InitiateDriver.StartBrowser()
        cls.login_page = LoginPage(cls.browser)        
                
        # Retrieve credentials from config file
        cls.username = read_config("Credentials", "username")
        cls.password = read_config("Credentials", "password")
    
    def test_success_login(self):
      
                self.login_page.enter_username(self.username)
                self.login_page.enter_password(self.password)
                self.login_page.click_login()
        
                # Verifikasi login berhasil
                self.assertTrue(self.login_page.is_login_successfull())
                self.login_page.logout()        
        
    @classmethod   
    def tearDownClass(cls):
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    