import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()

        log.info("Getting all the card titles")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i +1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooters()[i].click()

        confirmPage = checkOutPage.checkOutItems()

        confirmPage.checkOutItems().click()
        log.info("Entering country name")
        confirmPage.searchCountry().send_keys("Pol")
        self.verifyLinkPresence("Poland")
        confirmPage.getCountry().click()

        confirmPage.getCheckboxTerms().click()

        confirmPage.getPurchaseButton().click()

        successText = confirmPage.getResultInfo().text
        log.info(f"Text recieved from app is {successText}")
        assert "Success! Thank you!" in successText #perfectly failed and made a screenshot when changed
