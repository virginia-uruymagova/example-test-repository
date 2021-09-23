import os
import allure
from pytest_bdd import given, parsers, then, when
from functions import *
from locators.core_locators import *
from locators.inspection_page_locators import *
from locators.selection_process_locators import *


# ----- Test Config -----

# Getting variables from environment variables (windows)

def cred_data():

    data_dict = {
        "BASE_URL": os.environ['PROD_URL'],
        "ADMIN_USER": os.environ['FTQ_USER_admin_username'],
        "ADMIN_PASSWORD": os.environ['FTQ_USER_admin_password'],
        "CREATE_INSPECTION": os.environ['FTQ_INSP-PAGE_create_inspection'],
        "RECENT_INSPECTIONS_LISTING": os.environ['FTQ_LISTING-GRID_recent_insp'],
    }

    return data_dict


# Chrome preferences
prefs = {"download.default_directory": os.getcwd() + "/"}


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('no-sandbox')
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument('--start-maximized')  # SHOULD BE COMMENTED ALWAYS!!! ACTUAL ONLY FOR LOCAL LAUNCHES
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    return chrome_options


# Test setup and teardown
@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(60)
    yield selenium
    allure.attach(selenium.get_screenshot_as_png(),
                  name='test_evidence',
                  attachment_type=allure.attachment_type.PNG)


# ----- Fixtures -----

# Login
@pytest.fixture
@given(parsers.parse('I login as {user_type} user'))
def login_step(selenium, navigate_to_ftq, user_type):
    user_login = text_to_credential(user_type)
    username = user_login + '_USER'
    password = user_login + '_PASSWORD'
    enter_login_username = by_xpath(selenium, LG_USERNAME_FIELD).send_keys(cred_data()[username])
    enter_login_password = by_xpath(selenium, LG_PASSWORD_FIELD).send_keys(cred_data()[password])
    click_login_button = by_xpath(selenium, LG_LOGIN_BUTTON).click()
    wait_clickable(selenium, GL_TOP_MENU)


# Navigate to FTQ
@pytest.fixture
@given('I navigate to FTQ360 app')
def navigate_to_ftq(selenium):
    selenium.get(cred_data()['BASE_URL'])
    assert cred_data()['BASE_URL'] in selenium.current_url


# Navigate to dynamic page url
@pytest.fixture
@given(parsers.parse("I navigate to {page_name} page"))
def navigate_to_specific_page(selenium, page_name):
    page = text_to_credential(page_name)
    selenium.get(cred_data()['BASE_URL'] + cred_data()[page])
    assert selenium.current_url == cred_data()['BASE_URL'] + cred_data()[page]


# ----- Common Steps -----


@pytest.fixture
@then("I should see 'Loading data' modal")
def loading_modal_appears(selenium):
    modal_appears = wait_present(selenium, SP_DICT_LOADING_MODAL_OPEN)


@pytest.fixture
@then("I should wait until 'Loading data' modal will be closed")
def wait_for_modal_to_close(selenium):
    modal_loads = wait_present(selenium, SP_DICT_LOADING_MODAL_SUCCESS)
    loading_complete = wait_present(selenium, SP_DICT_LOADING_MODAL_CLOSED)


@pytest.fixture
@when("I create an inspection")
def create_inspection(selenium):
    go_to_create_insp = selenium.get(cred_data()['BASE_URL'] + cred_data()["CREATE_INSPECTION"])
    dict_loading_modal_appears = wait_present(selenium, SP_DICT_LOADING_MODAL_OPEN)
    dictionaries_load = wait_present(selenium, SP_DICT_LOADING_MODAL_SUCCESS)
    dictionary_loading_complete = wait_present(selenium, SP_DICT_LOADING_MODAL_CLOSED)
    select_checklist_general = by_xpath(selenium, SP_SELECT_GENERAL_PUNCH_CHECKLIST).click()
    select_rp = by_xpath(selenium, SP_SELECT_GENERAL_RP).click()
    check_inspection_created_successfully = wait_clickable(selenium, INSP_HEADER)
    assert selenium.title == "Inspection"
    click_save_btn = by_xpath(selenium, INSP_SAVE_BUTTON).click()
    wait_clickable(selenium, INSP_SYNCED_TEXT)


@pytest.fixture
@when(parsers.parse("I create an inspection via '{checklist}'"))
def create_specific_inspection(selenium, checklist):
    go_to_create_insp = selenium.get(cred_data()['BASE_URL'] + cred_data()["CREATE_INSPECTION"])
    dict_loading_modal_appears = wait_present(selenium, SP_DICT_LOADING_MODAL_OPEN)
    dictionaries_load = wait_present(selenium, SP_DICT_LOADING_MODAL_SUCCESS)
    dictionary_loading_complete = wait_present(selenium, SP_DICT_LOADING_MODAL_CLOSED)
    select_specific_checklist = by_xpath(selenium, (SPECIFIC_SELECTION(selenium, checklist))).click()
    select_rp = by_xpath(selenium, SP_SELECT_GENERAL_RP).click()
    check_inspection_created_successfully = wait_clickable(selenium, INSP_HEADER)
    assert selenium.title == "Inspection"
    click_save_btn = by_xpath(selenium, INSP_SAVE_BUTTON).click()
    wait_clickable(selenium, INSP_SYNCED_TEXT)


@pytest.fixture
@when("I click on 'Save' button on inspection page")
def click_save_inspection(selenium):
    click_save_btn = by_xpath(selenium, INSP_SAVE_BUTTON).click()


@pytest.fixture
@then("I wait until Inspection ID value appears on inspection page")
def inspection_id_appears(selenium):
    wait_clickable(selenium, INSP_SYNCED_TEXT)
    wait_clickable(selenium, INSP_ID)


@pytest.fixture
@then("I should see 'Synced to server' inspection status")
def synced_to_server(selenium):
    wait_clickable(selenium, INSP_SYNCED_TEXT)


@pytest.fixture
@when("I refresh page")
def refresh_browser(selenium):
    selenium.refresh()
