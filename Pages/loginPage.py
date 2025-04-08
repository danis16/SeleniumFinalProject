from selenium.webdriver.common.by import By
from Library import get_locator, read_config
import time

class LoginPage:
    
    def __init__(self, browser):
        self.browser = browser        
        # Ambil locator dari element.cfg
        self.username_locator = get_locator("Login","username")
        self.password_locator = get_locator("Login","password")
        self.login_button_locator = get_locator("Login","login_button")        
        # Menambahkan locator untuk logout       
        self.burger_menu_locator = get_locator("Inventory","burger_menu")
        self.logout_button_locator = get_locator("Inventory","logout_button")
        
    def enter_username(self, username):
        """Clear and enter the username."""
        username_field = self.browser.find_element(By.ID, self.username_locator)
        username_field.clear()
        username_field.send_keys(username)
        
    def enter_password(self, password):
        """Clear and enter the password."""
        password_field = self.browser.find_element(By.ID,self.password_locator)
        password_field.clear()
        password_field.send_keys(password)
    
    def click_login(self):        
        """Click the login button."""
        self.browser.find_element(By.ID, self.login_button_locator).click()

    def is_login_successfull(self):
        """Verify successful login by checking the URL."""
        get_url = self.browser.current_url
        
        if '/inventory.html'in get_url:
            print("Website logged in successfully")
            return True
        else:
            print("Failed")
            return False
    
    def logout(self):
        self.browser.find_element(By.ID, self.burger_menu_locator).click()
        time.sleep(1)
        self.browser.find_element(By.ID, self.logout_button_locator).click()
        time.sleep(2) # Wait for logout to complete
        
        
        
        




   