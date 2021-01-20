import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utils.readProperties import ReadConfig
from Utils.customLogger import LogGen
from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
import time

class Test_SearchCustomerByName_T005():

    baseUrl = ReadConfig.get_application_URL()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()


    @pytest.mark.regression
    def test_search_by_email(self,setup):
        self.logger.info("**********Test_SearchCustomerByName_T005*********")
        self.logger.info("**********Verifying the Login*********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*******Login is successful*********")
        self.logger.info("********Starting Search customer by Name *************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.click_customer_menu()
        time.sleep(2)
        self.addcust.click_customer_menu_item()

        self.logger.info("****** Entering the First Name **************")
        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.set_firstName("Arthur")
        self.searchCust.set_lastName("Holmes")
        self.searchCust.click_search()
        time.sleep(3)
        status = self.searchCust.search_customer_by_name("Arthur Holmes")
        assert True == status
        self.logger.info("******** Test_SearchCustomerByName_T005 Finished *********")
        self.driver.close()










