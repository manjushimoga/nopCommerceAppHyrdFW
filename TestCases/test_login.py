import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utils.readProperties import ReadConfig
from Utils.customLogger import LogGen

class Test_001_Login():

    baseUrl = ReadConfig.get_application_URL()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_HomePageTitle(self,setup):
        print(self.logger,'&&&&&&&')
        self.logger.info("**********Test_001_Login**********")
        self.logger.info("*************Verifying Home Page Title***************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("******Home page title test is passed*********")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("******Home page title test is Failed*********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**********test_login*********")
        self.logger.info("**********Verifying the Login*********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title= self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("**********Login is succusfull- passed*********")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("**********Login is not succusful-Failed *********")
            assert False







