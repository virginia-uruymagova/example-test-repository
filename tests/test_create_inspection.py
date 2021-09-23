import time
import allure
from pytest_bdd import scenario, when, then, parsers
from functions import *
from locators.selection_process_locators import *
from locators.inspection_page_locators import *


@scenario("../features/create_inspection.feature", "Create Inspection")
def test_create_inspection():
    """test simple steps to create an inspection"""


@allure.step
@when(parsers.parse("I select '{checklist}' checklist on create inspection page"))
def select_checklist(selenium, checklist):
    select_specific_checklist = by_xpath(selenium, (SPECIFIC_SELECTION(selenium, checklist))).click()


@allure.step
@when(parsers.parse("I select 'V1' vendor on create inspection page"))
def select_checklist(selenium):
    select_rp = by_xpath(selenium, SP_SELECT_GENERAL_RP).click()


@allure.step
@then("inspection is created successfully")
def inspection_created_successfully(selenium):
    check_inspection_created_successfully = wait_clickable(selenium, INSP_HEADER)
    assert selenium.title == "Inspection"




