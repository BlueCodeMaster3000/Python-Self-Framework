from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkoutButton = (By.XPATH, "//button[@class='btn btn-success']")
    countrySearchBar = (By.XPATH, "//input[@id='country']")
    searchedCountry = (By.LINK_TEXT, "Poland")
    checkboxTerms = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    resultText = (By.CLASS_NAME, 'alert-success')

    def checkOutItems(self):
        return self.driver.find_element(*ConfirmPage.checkoutButton)

    def searchCountry(self):
        return self.driver.find_element(*ConfirmPage.countrySearchBar)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.searchedCountry)

    def getCheckboxTerms(self):
        return self.driver.find_element(*ConfirmPage.checkboxTerms)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getResultInfo(self):
        return self.driver.find_element(*ConfirmPage.resultText)
