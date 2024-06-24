import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as Ec


class loginpage:                         # It is a class,under it has methods and methods under functions.

    text_UserName_XPATH = (By.XPATH,"//input[@placeholder='Username']")           # These are objects of XPATH.
    text_Password_XPATH = (By.XPATH,"//input[@placeholder='Password']")           # Which is called functions(Object)
    Click_Login_Button_XPATH = (By.XPATH,"//button[normalize-space()='Login']")
    Credential_Error_XPATH = (By.XPATH,"//div[@class='oxd-alert-content oxd-alert-content--error']")
    Click_Menu_Button_XPATH = (By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    Click_LogOut_Button_XPATH = (By.XPATH,"//a[normalize-space()='Logout']")


    def __init__(self,driver):    # It is a constructor to redirect method and function in testcases using veriable.
        self.driver = driver

    def Enter_Username(self,Username):             # These are method,under it has used functions objects.
        self.driver.find_element(*loginpage.text_UserName_XPATH).send_keys(Username)

    def Enter_Password(self,Password):
        self.driver.find_element(*loginpage.text_Password_XPATH).send_keys(Password)

    def Click_LoginButton(self):
        self.driver.find_element(*loginpage.Click_Login_Button_XPATH).click()

    def Displayed_Credential_Error(self):
        self.driver.find_element(*loginpage.Credential_Error_XPATH).is_displayed()

    def Click_MenuButton(self):
        self.driver.find_element(*loginpage.Click_Menu_Button_XPATH).click()

    def Click_LogOutButton(self):
        self.driver.find_element(*loginpage.Click_LogOut_Button_XPATH).click()

    def Login_Status(self):
        try:
            self.driver.find_element(*loginpage.Click_Menu_Button_XPATH)
            return True
        except Ec:
            return False




