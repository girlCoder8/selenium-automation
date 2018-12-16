from pages.webapp import webapp
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class signin():
    instance = None

    page_url = 'https://secure.indeed.com/account/login'
    email_inputfield = 'signin_email'
    pwd_inputfield = 'signin_password'
    button_css_signin = 'icl-Button--primary'

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = signin()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()


    def input_account(self, data):
        element = self.driver.find_element_by_id(self.email_inputfield)
        if not element:
            assert False, "Account Input Field Not Found."
            webapp.save_screenshot('input_account')
        else:
            element.send_keys(data)


    def input_password(self, data):
        element = self.driver.find_element_by_id(self.pwd_inputfield)
        if not element:
            assert False, "Password Input Field Not Found."
            webapp.save_screenshot('input_password')
        else:
            element.send_keys(data)

    def click_signin_button(self):
        element = self.driver.find_element_by_class_name(self.button_css_signin)
        if not element:
            assert False, "Signin button Not Found."
            webapp.save_screenshot('click_signin_button')
        else:
            element.click()


    def verify_is_current_page(self):
        # Check current page
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.url_contains(self.page_url))
        except Exception as inst:
            assert self.driver.current_url in self.page_url, 'Wrong Page.'

signin = signin.get_instance()