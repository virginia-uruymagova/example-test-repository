import allure
from pytest_bdd import scenario, when
from functions import *
from locators.selection_process_locators import *


@scenario("../features/emergency_dictionary_refresh.feature", "Emergency Dictionary Refresh")
def test_emergency_dictionary_refresh():
    """test use of the emergency dictionary refresh button in selection process"""


@allure.step
@when("I click on emergency dictionary refresh button")
def click_emergency_dictionary_refresh_button(selenium):
    click_emergency_dict_refresh = by_xpath(selenium, SP_EMERGENCY_DICT).click()



