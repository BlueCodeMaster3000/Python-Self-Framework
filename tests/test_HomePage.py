import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

    def test_formSubmission(self, getData):
        log = self.getLogger()

        homePage = HomePage(self.driver)
        log.info(f"First name is {getData['firstname']}")
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys("Poggolini")

        homePage.checkIceCream().click()

        self.selectOptionByText(homePage.getGender(), getData["gender"])

        homePage.checkEmployment().click()

        homePage.getSubmit().click()
        outcome = homePage.getOutcomeAlert().text
        print(outcome)
        assert "Success" in outcome
        self.driver.refresh()



