import time
import allure
from pytest_bdd import scenario, when, then, parsers
from functions import *
from locators.selection_process_locators import *
from locators.inspection_page_locators import *

DATA = dict(observation=str, corrective_active_note=str)

@pytest.fixture
def data_scope():
    JSON_DATA = {"RESPONSIBLE_PARTY_LOC":"(//div[@class='ui input right icon fluid'])[1]",
            "DUE_DATA_LOC":"//section/div[1]/div[1]/div/div[7]/div/input"}
    return JSON_DATA


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




