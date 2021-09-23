import allure
from pytest_bdd import scenario, when, then, parsers
from functions import *
from locators.inspection_page_locators import *
from selenium.webdriver.common.action_chains import ActionChains


@scenario("../features/signature.feature", "Signature")
def test_signature():
    """test the user can add signature to a checkpoint on an inspection"""


@allure.step
@when(parsers.parse("I click on camera button in '{checkpoint}' checkpoint on inspection page"))
def click_camera_icon(selenium, checkpoint):
    camera = by_xpath(selenium, INSP_CHECKPOINT(selenium, checkpoint) + CP_CAMERA)
    scroll_into_view(selenium, camera)
    click_camera = camera.click()


@allure.step
@when("I select 'Signature' option in camera dropdown on inspection page")
def select_signature_icon(selenium):
    click_signature = by_xpath(selenium, CP_SIGNATURE).click()


@allure.step
@then("I should see drawing board")
def signature_box_pops_up(selenium):
    verify_canvas = wait_clickable(selenium, CP_SIGNATURE_CANVAS)


@allure.step
@when("I draw signature on drawing board")
def draw_signature(selenium):
    canvas = by_xpath(selenium, CP_SIGNATURE_CANVAS)
    draw = ActionChains(selenium).click_and_hold(canvas)\
        .move_by_offset(100, 100).release().perform()


@allure.step
@when("I click on 'Save' button on drawing board")
def click_save_signature(selenium):
    save_signature = by_xpath(selenium, CP_SIGNATURE_SAVE).click()


@allure.step
@then(parsers.parse("I should see attached file to '{checkpoint}' checkpoint on inspection page"))
def see_signature_attached(selenium, checkpoint):
    wait_clickable(selenium, (INSP_CHECKPOINT(selenium, checkpoint) + CP_ATTACHMENT))
