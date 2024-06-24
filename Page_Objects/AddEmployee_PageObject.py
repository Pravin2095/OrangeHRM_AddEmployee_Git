import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as Ec


class AddEmployee:
    Click_PIM_Button_XPATH = (By.XPATH, "//span[normalize-space()='PIM']")
    Click_AddEmp_Button_XPATH = (By.XPATH, "//a[normalize-space()='Add Employee']")
    text_First_Name_XPATH = (By.XPATH, "//input[@placeholder='First Name']")
    text_Middle_Name_XPATH = (By.XPATH, "//input[@placeholder='Middle Name']")
    text_Last_Name_XPATH = (By.XPATH, "//input[@placeholder='Last Name']")
    text_EmpID_XPATH = (By.XPATH,
                            "//div[@class='oxd-input-group oxd-input-field-bottom-space']"
                            "//div//input[@class='oxd-input oxd-input--active']")
    Click_Save_Button_XPATH = (By.XPATH, "//button[normalize-space()='Save']")
    Click_Personal_Details_XPATH = (By.XPATH, "//a[normalize-space()='Personal Details']")

    def __init__(self, driver):
        self.driver = driver

    def Click_PIM(self):
        self.driver.find_element(*AddEmployee.Click_PIM_Button_XPATH).click()

    def Click_AddEmp(self):
        self.driver.find_element(*AddEmployee.Click_AddEmp_Button_XPATH).click()
        # time.sleep(2)

    def Enter_FirstName(self, Firstname):
        self.driver.find_element(*AddEmployee.text_First_Name_XPATH).send_keys(Firstname)

    def Enter_MiddleName(self, Middlename):
        self.driver.find_element(*AddEmployee.text_Middle_Name_XPATH).send_keys(Middlename)

    def Enter_LastName(self, Lastname):
        self.driver.find_element(*AddEmployee.text_Last_Name_XPATH).send_keys(Lastname)

    # def Enter_EmpID_BackSpace01(self, text_EmpID_XPATH):
    #     Length = len(text_EmpID_XPATH)
    #     for :
    #         self.driver.find_element(*AddEmployee.text_EmpID_XPATH).send_keys(Keys.BACK_SPACE)

    def Enter_EmpID(self, ID):
        self.driver.find_element(*AddEmployee.text_EmpID_XPATH).send_keys(ID)

    def Click_SaveButton(self):
        self.driver.find_element(*AddEmployee.Click_Save_Button_XPATH).click()

    def Add_Employee_Status(self):
        try:
            self.driver.find_element(*AddEmployee.Click_Personal_Details_XPATH)
            return True
        except Ec:
            return False
