from os import times_result
from selenium.webdriver.common.by import By
from Library import get_locator, read_config
import time
from selenium.webdriver.support.ui import Select

class InventoryPage:
    
    def __init__(self, browser):
        self.browser = browser        
        self.product_sort_container_locator = get_locator("Inventory","product_sort_container")
      
    # def test_filter(self):
    #     self.browser.find_element(By.CSS_SELECTOR, self.product_sort_container).click()
    #     # select.select_by_value(filter) 
    #     time.sleep(20)
    
    def test_filter(self, value):
        """click test filter"""
        select_element = self.browser.find_element(By.XPATH, self.product_sort_container_locator)
        select = Select(select_element)
        select.select_by_value(value) 
        time.sleep(5)


 
    
    
        
   
        




   