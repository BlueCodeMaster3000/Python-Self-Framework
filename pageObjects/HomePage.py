import pytest
from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(@href,'shop')]")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    loveIceCream = (By.ID, 'exampleCheck1')
    employment = (By.CSS_SELECTOR, "#inlineRadio1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    outcomeAlert = (By.CLASS_NAME, 'alert-success')

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def checkIceCream(self):
        return self.driver.find_element(*HomePage.loveIceCream)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def checkEmployment(self):
        return self.driver.find_element(*HomePage.employment)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getOutcomeAlert(self):
        return self.driver.find_element(*HomePage.outcomeAlert)


