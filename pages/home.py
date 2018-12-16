from pages.webapp import webapp
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class home():
    instance = None

    page_url = 'https://www.indeed.com'
    li_header_item = 'icl-DesktopGlobalHeader-item'
    link_text_signin = 'Sign in'
    navigation_menu = 'icl-DesktopGlobalHeader-toggleDropdown'

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = home()

        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()





#Function
    def click_signin_button(self):
        element = self.driver.find_element_by_link_text(self.link_text_signin)
        if not element:
            assert False, "Signin button Not Found."
        else:
            element.click()

    def verify_status_signedin(self, data):
        element = self.driver.find_element_by_class_name(self.navigation_menu)
        assert data in element.text, "User doesn't logged in."


    def verify_is_current_page(self):
        # Check current page
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.url_contains(self.page_url))
        except Exception as inst:
            assert self.driver.current_url in self.page_url, 'Wrong Page.'




home = home.get_instance()