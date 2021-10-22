from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class HomePage:
    title_xpath= "//h2[normalize-space()='Welcome to Shoe Store!']"

    def __init__(self, driver):
        self.driver = driver

    def titleDisplayed(self):
        self.driver.find_element_by_xpath(self.title_xpath).is_displayed()