import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.homePage import HomePage
import Pages.navbarValidation
from Utilities.customLogger import LogGen
from Utilities.readproperty import ReadConfig
import time


baseURL = ReadConfig.getURL()
myLogger = LogGen.loggen()

class navBar:
    navbar_xpath= "//a[normalize-space()='All Shoes']"

    def __init__(self, driver):
        self.driver = driver

    def clickonAllShoes(self):
        self.driver.find_element_by_xpath(self.navbar_xpath).click()
