


class SearchCustomer():
    # Add customer page
    txt_Email_id = "SearchEmail"
    txt_FirstName_id = 'SearchFirstName'
    txt_LastName_id = 'SearchLastName'
    btn_search_id = 'search-customers'

    tbl_searchResults_xpath = "//table[@role='grid']"
    tbl_xpath = "//table[@id='customers-grid']"
    tbl_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tbl_cols_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def set_Email(self,email):
        self.driver.find_element_by_id(self.txt_Email_id).clear()
        self.driver.find_element_by_id(self.txt_Email_id).send_keys(email)

    def set_firstName(self,fname):
        self.driver.find_element_by_id(self.txt_FirstName_id).clear()
        self.driver.find_element_by_id(self.txt_FirstName_id).send_keys(fname)

    def set_lastName(self,lname):
        self.driver.find_element_by_id(self.txt_LastName_id).clear()
        self.driver.find_element_by_id(self.txt_LastName_id).send_keys(lname)

    def click_search(self):
        self.driver.find_element_by_id(self.btn_search_id).click()

    def get_noOf_Rows(self):
        return len(self.driver.find_elements_by_xpath(self.tbl_rows_xpath))

    def get_noOf_cols(self):
        return len(self.driver.find_elements_by_xpath(self.tbl_cols_xpath))

    def search_customer_by_email(self,email):
        flag = False
        for r in range(1,self.get_noOf_Rows()+1):
            table = self.driver.find_element_by_xpath(self.tbl_xpath)
            email_id = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if email_id == email:
                flag=True
                break
        return flag

    def search_customer_by_name(self,name):
        flag = False
        for r in range(1,self.get_noOf_Rows()+1):
            table = self.driver.find_element_by_xpath(self.tbl_xpath)
            Name = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if Name == name:
                flag=True
                break
        return flag

