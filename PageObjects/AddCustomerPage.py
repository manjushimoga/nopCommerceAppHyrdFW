from selenium.webdriver.support.ui import Select
import time

class AddCustomer:
    # Add Customer Page
    lnk_customer_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnk_customer_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btn_AddNew_xpath = "//a[@class='btn bg-blue']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_FirstName_xpath = "//input[@id='FirstName']"
    txt_LastName_xpath = "//input[@id='LastName']"
    rdbtn_malegender_id = "Gender_Male"
    rdbtn_femalegender_id = "Gender_Female"
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_Company_xpath = "//input[@id='Company']"
    txt_custRoles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    lstItem_Administrators_xpath = "//li[text()='Administrators']"
    lstItem_ForumModerators_xpath = "//li[text()='Forum Moderators']"
    lstItem_Guests_xpath = "//li[text()='Guests']"
    lstItem_Registered_xpath = "//li[text()='Registered']"
    lstItem_Vendors_xpath = "//li[text()='Vendors']"
    drp_mgrVendor_xpath = "//*[@id='VendorId']"
    txtarea_AdmContent_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def click_customer_menu(self):
        self.driver.find_element_by_xpath(self.lnk_customer_menu_xpath).click()

    def click_customer_menu_item(self):
        self.driver.find_element_by_xpath(self.lnk_customer_menuitem_xpath).click()

    def click_on_addNew(self):
        self.driver.find_element_by_xpath(self.btn_AddNew_xpath).click()

    def set_Email(self,email):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email)

    def set_Password(self,pwd):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(pwd)

    def set_First_name(self,fstName):
        self.driver.find_element_by_xpath(self.txt_FirstName_xpath).send_keys(fstName)

    def set_LastName(self,LName):
        self.driver.find_element_by_xpath(self.txt_LastName_xpath).send_keys(LName)

    def set_company_name(self,compName):
        self.driver.find_element_by_xpath(self.txt_Company_xpath).send_keys(compName)

    def set_customer_roles(self,role):
        self.driver.find_element_by_xpath(self.txt_custRoles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstItem_Registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstItem_Administrators_xpath)
        elif role == "Guests":

            # Here user can be registered (or) Guests, only one
            time.sleep(2)
            self.driver.find_element_by_xpath("//span[@aria-label='delete']").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstItem_Guests_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstItem_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstItem_Guests_xpath)

        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def set_mgrOfVendor(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drp_mgrVendor_xpath))
        drp.select_by_visible_text(value)

    def set_Gender(self,gender):
        if gender == "male":
            self.driver.find_element_by_id(self.rdbtn_malegender_id).click()
        elif gender == "female":
            self.driver.find_element_by_id(self.rdbtn_femalegender_id).click()
        else:
            self.driver.find_element_by_id(self.rdbtn_malegender_id).click()

    def set_dob(self,dob):
        self.driver.find_element_by_xpath(self.txt_dob_xpath).send_keys(dob)

    def set_AdminContent(self,content):
        self.driver.find_element_by_xpath(self.txtarea_AdmContent_xpath).send_keys(content)

    def click_save(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()




