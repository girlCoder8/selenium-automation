from behave import given, when, then
from pages.webapp import webapp
from pages.signin import signin
from pages.home import home


@given(u'I navigate to Indeed site')
def step_impl_load_website(context):
    webapp.load_website()


@when(u'I navigate to Signin Page')
def step_impl_goto_page(context):
    home.click_signin_button()


@then(u'I fill in account "{account}" and "{password}" to signin')
def step_impl_verify_component(context, account, password):
    signin.verify_is_current_page()
    signin.input_account(account)
    signin.input_password(password)
    signin.click_signin_button()

@then(u'I can see "{user}" on Indeed portal')
def step_impl_verify_signin_status(context, user):
    home.verify_is_current_page()
    home.verify_status_signedin(user)

