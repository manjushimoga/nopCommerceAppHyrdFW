import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utils.readProperties import ReadConfig
from PageObjects.AddCustomerPage import AddCustomer
from Utils.customLogger import LogGen
import string
import time
import random

class Test_003_AddCustomer():

    baseUrl = ReadConfig.get_application_URL()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()


    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("**********Test_003_addCustomer*********")
        self.logger.info("**********Creating the customer and verifying it*********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Succussfull**********")

        self.logger.info("****** Starting Adding new customer*********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.click_customer_menu()
        time.sleep(2)
        self.addcust.click_customer_menu_item()
        self.addcust.click_on_addNew()

        self.logger.info("******* Providing customer Info **********")

        self.email = random_generator() + '@gmail.com'
        self.addcust.set_Email(self.email)
        self.addcust.set_Password("test1234")
        self.addcust.set_First_name("Manjunatha")
        self.addcust.set_LastName("Charu")
        self.addcust.set_Gender("male")
        self.addcust.set_dob("01/01/1989")
        self.addcust.set_company_name("IBS")
        self.addcust.set_customer_roles("Vendors")
        self.addcust.set_mgrOfVendor("Vendor 2")
        self.addcust.set_AdminContent("This is for testing...........")
        time.sleep(2)
        self.addcust.click_save()

        self.logger.info("********** Saving customer info ************")
        self.logger.info("********* Add customer validation started ***********")

        self.msg = self.driver.find_element_by_tag_name('body').text

        print(self.msg)

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("******* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_addCustomer_scr.png")
            self.logger.error("********* Add customer Test Failed *******")
            assert True == False


        self.driver.close()
        self.logger.info("************** Ending Adding customers succusfull Test ********")



def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))


