import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utils.readProperties import ReadConfig
from Utils.customLogger import LogGen
from Utils import ExcelUtils
import time

class Test_002_DDT_Login():

    baseUrl = ReadConfig.get_application_URL()
    path = "./TestData/LoginData.xlsx"
    logger = LogGen.log_gen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("**********Test_002_DDT_Login*********")
        self.logger.info("**********test_login_ddt*************")
        self.logger.info("**********Verifying the Login DDT test*********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.row = ExcelUtils.get_row_count(self.path,"data")
        print("No of rows in an excel",self.row)
        lst_status = []

        for r in range(2,self.row+1):
            self.user = ExcelUtils.read_data(self.path,"data",r,1)
            self.pwd = ExcelUtils.read_data(self.path, "data", r, 2)
            self.exp = ExcelUtils.read_data(self.path, "data", r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.pwd)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("*****Passed*****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("******Failed********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Fail":
                    self.logger.info("****Passed******")
                    lst_status.append("Pass")
                elif self.exp=="Pass":
                    self.logger.info("*****Failed******")
                    lst_status.append("Fail")
        if "Fail" not in lst_status:
            self.logger.info("*********Login DDT test Passed**********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********Login DDT test Failed************")
            self.driver.close()
            assert False

        self.logger.info("***** End of Login DDT test*********")
        self.logger.info("*******Completed DDT Login TC_002**********")

