import allure
from pytest_bdd import scenario, parsers, when, then
from functions import *
from locators.inspection_page_locators import *


@scenario("../features/opn-qc_checkpoints.feature", "OPN/QC checkpoints work as expected")
def test_opn_qc_checkpoints():
    """Verify that OPN/QC checkpoints are working as expected"""


@allure.step
@when(parsers.parse("I click on 'OPN' checkbox in '{checkpoint}' checkpoint on inspection page"))
def click_checkpoint_status(selenium, checkpoint):
    checkpoint_name = by_xpath(selenium, INSP_CHECKPOINT(selenium, checkpoint))
    scroll_to_checkpoint = scroll_into_view(selenium, checkpoint_name)
    checkpoint_status_select = by_xpath(selenium, (INSP_CHECKPOINT(selenium, checkpoint)
                                                   + CHECKPOINT_STATUS()["OPN"])).click()


@allure.step
@when(parsers.parse("I fill 'Corrective Action Notes' field for '{checkpoint}' checkpoint with '{text}'"))
def fill_deficiency_checkpoint_fields_CA(selenium, checkpoint, text):
    by_xpath(selenium, INSP_CHECKPOINT(selenium, checkpoint) + CP_CA_NOTE).click()
    by_xpath(selenium, CP_CA_NOTE_EDIT).send_keys(f"{text}")


@allure.step
@when(parsers.parse("I fill 'Responsible Party' field for '{checkpoint}' checkpoint with '{text}'"))
def fill_deficiency_checkpoint_fields_RP(selenium, checkpoint, text):
    rp_to_select = text
    # center_rp_list = scroll_into_view1(selenium, INSP_CHECKPOINT(selenium, checkpoint) + CP_RP_DROPDOWN)
    dropdown_xpath = CP_RP_DROPDOWN_SELECTION(selenium, checkpoint, rp_to_select)
    correct_rp = by_xpath(selenium, dropdown_xpath)
    scroll_to_correct_rp = scroll_into_view(selenium, correct_rp)
    click_correct_rp = correct_rp.click()
    true_rp_selected = by_xpath(selenium, INSP_CHECKPOINT(selenium, checkpoint) + CP_RP_DROPDOWN).get_attribute("value")
    if true_rp_selected != "Responsible Party 2 (V1)":
        fill_deficiency_checkpoint_fields_RP(selenium, checkpoint, rp_to_select)
    else:
        pass


@allure.step
@when(parsers.parse("I click on 'FTQ' checkbox in '{checkpoint}' checkpoint on inspection page"))
def click_ftq_status(selenium, checkpoint):
    checkpoint_name = by_xpath(selenium, INSP_CHECKPOINT(selenium, checkpoint))
    scroll_to_checkpoint = scroll_into_view(selenium, checkpoint_name)
    checkpoint_status_select = by_xpath(selenium, (INSP_CHECKPOINT(selenium, checkpoint)
                                                   + CHECKPOINT_STATUS()["FTQ"])).click()
    by_xpath(selenium, POP_CP_STATUS_CONFIRM).click()


@allure.step
@then(parsers.parse("I should see changes made to fields in '{checkpoint}' checkpoint on inspection page"))
def value_still_present(selenium, checkpoint):
    true_ca_note = by_xpath(selenium, INSP_CHECKPOINT(selenium, checkpoint) + CP_CA_NOTE).text
    assert true_ca_note == "actionNote"
    true_rp_selected = by_xpath(selenium, INSP_CHECKPOINT(selenium, checkpoint) + CP_RP_DROPDOWN).get_attribute("value")
    assert true_rp_selected == "Responsible Party 2 (V1)"
