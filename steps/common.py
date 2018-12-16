from behave import given, when, then
from pages.webapp import webapp

@then(u'Close Browser')
def step_impl_close_browser(context):
    webapp.close_browser()