import allure
from pytest_bdd import scenario, when, then, parsers
from functions import *
from locators.core_locators import *
from locators.forgot_pw_locators import *


@scenario("../features/forgot_password.feature", "Forgot Password")
def test_forgot_password():
    """test use of the forgot password link on FTQ login page"""


@allure.step
@when("I click on 'Forgot password' link under Login form")
def click_forgot_pw_link(selenium, navigate_to_ftq):
    click_forgot_pass_link = by_xpath(selenium, LG_FORGOT_PASSWORD).click()
    assert "Forgot" in selenium.current_url
    wait_present(selenium, FP_RESTORE_PASSWORD_TITLE)
    wait_present(selenium, FP_INFO_TEXT)
    wait_present(selenium, FP_ENTER_USERNAME)


@allure.step
@when(parsers.parse("I type '{text}' in 'User name' field"))
def enter_username_for_forgotten_pw(selenium, text):
    enter_username_for_forgot_pw = by_xpath(selenium, FP_ENTER_USERNAME).send_keys(text)


@allure.step
@when("I click on 'Reset' button in Forgot Password form")
def click_forgot_password_reset_button(selenium):
    click_forgot_pw_reset_btn = by_xpath(selenium, FP_RESET_BUTTON).click()


@allure.step
@then(parsers.parse("I should see in forgot password form following text:\n{text}"))
def see_forgot_pw_following_text(selenium, text):
    wait_present(selenium, FP_RESET_CONFIRMATION_TEXT_WRAPPER)
    check_text = text.split("\n")
    for x in check_text:
        assert x in selenium.page_source
