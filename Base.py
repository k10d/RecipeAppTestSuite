from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, element):
        wait = WebDriverWait(self, 5)
        wait.until(lambda self: self.driver.find_element(*element))
        return self.driver.find_element(*element)
        
    def is_element_present(self, element):
        present = self.get_element(element)
        return present

    def enter_text(self, field, text):
        field_element = self.get_element(field)
        field_element.send_keys(text)
        
    def clear_text(self, element):
        element = self.get_element(element)
        element.clear()

    def get_text(self, word):
        word_element = self.get_element(word)
        return word_element.get_attribute('value')

    def click_button(self, btn):
        button_element =  self.get_element(btn)
        button_element.click()




