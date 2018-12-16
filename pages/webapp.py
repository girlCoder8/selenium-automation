from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from data.config import settings
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urlparse import urljoin
import os, datetime

class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):

        driver_path_firefox  = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/geckodriver')
        driver_path_chrome  =  os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/chromedriver')

        try:
            self.remote_webdriver_user = os.environ['BROWSERSTACK_USER']
            self.remote_webdriver_accesskey = os.environ['BROWSERSTACK_ACCESSKEY']
            self.is_remote_webdriver = os.environ['IS_REMOTE_WEBDRIVER']
        except:
            self.remote_webdriver_user = settings['remote_webdriver_user']
            self.remote_webdriver_accesskey = settings['remote_webdriver_accesskey']
            self.is_remote_webdriver = settings['remote_webdriver']

        if self.is_remote_webdriver :

            desired_cap = {
                    'os' : settings['os'],
                    'os_version' : settings['os_version'],
                    'browser' : settings['browser'],
                    'browser_version' : '',
                    'browserstack.local' : 'false',
                    'browserstack.selenium_version' : settings['browserstack_selenium_version']
            }

            if str(settings['browser']).lower() == "firefox":
                desired_cap['browser_version'] = settings['browser_version_firefox']
                self.driver = webdriver.Remote(command_executor='http://' + self.remote_webdriver_user + ':' + self.remote_webdriver_accesskey + '@hub-cloud.browserstack.com/wd/hub',desired_capabilities=desired_cap)
            elif str(settings['browser']).lower() == "chrome":
                desired_cap['browser_version'] = settings['browser_version_chrome']
                self.driver = webdriver.Remote(command_executor='http://' + settings['remote_webdriver_user'] + ':' + settings['remote_webdriver_accesskey'] + '@hub-cloud.browserstack.com/wd/hub',desired_capabilities=desired_cap)
            else:
                desired_cap['browser_version'] = settings['browser_version_firefox']
                self.driver = webdriver.Remote(command_executor='http://' + settings['remote_webdriver_user'] + ':' + settings['remote_webdriver_accesskey'] + '@hub-cloud.browserstack.com/wd/hub',desired_capabilities=desired_cap)
        else:
            if str(settings['browser']).lower() == "firefox":
                self.driver = webdriver.Firefox(executable_path = driver_path_firefox)
            elif str(settings['browser']).lower() == "chrome":
                self.driver = webdriver.Chrome(executable_path = driver_path_chrome)
            else:
                self.driver = webdriver.Firefox(executable_path = driver_path_firefox)


    def get_driver(self):
        return self.driver

    def close_browser(self):
        self.driver.close()

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(settings[page])

    def save_screenshot(self, note):
        # Simple implementation
        self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../screenshots/', datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S") + '_' + note + '.png'))

webapp = WebApp.get_instance()
