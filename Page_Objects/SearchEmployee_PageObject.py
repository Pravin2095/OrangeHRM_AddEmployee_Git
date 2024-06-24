from selenium.webdriver.common.by import By

class SearchEmployee:

    Search_Employee_Button_XPATH = (By.XPATH,"//a[normalize-space()='Employee List']")
    Employee_Name_Box_XPATH = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
    Search_Button_XPATH = (By.XPATH,"//button[normalize-space()='Search']")
    List_Employee_Bar_XPATH = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]")
    Employee_Status_XPATH = (By.XPATH,"//div[@class='orangehrm-edit-employee-name']")


    def __init__(self,driver):
        self.driver = driver


    def Click_Search_Employee(self):
        self.driver.find_element(*SearchEmployee.Search_Employee_Button_XPATH).click()

    def Click_Employee_Name(self,Employee_Name):
        self.driver.find_element(*SearchEmployee.Employee_Name_Box_XPATH).send_keys(Employee_Name)

    def Click_Search_Button(self):
        self.driver.find_element(*SearchEmployee.Search_Button_XPATH).click()

    def Click_List_Bar(self):
        self.driver.find_element(*SearchEmployee.List_Employee_Bar_XPATH).click()

    def Click_Employee_Status(self):
        try:
            self.driver.find_element(*SearchEmployee.Employee_Status_XPATH)
            return True
        except:
            return False



