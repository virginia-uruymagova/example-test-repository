from datetime import date
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.core_locators import *


# --- Functions ---

# wait 20 seconds for page load


def wait_page_title_exact(selenium, title):
    try:
        WebDriverWait(selenium, 20).until(
            EC.title_is(title)
        )
    except:
        pytest.fail(f"{title} does not match page title")


# wait 20 seconds until element present
def wait_present(selenium, locator):
    try:
        WebDriverWait(selenium, 20).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
    except:
        pytest.fail(f"Element to wait {locator} is not found")


# wait 20 seconds until element present and then clickable
def wait_clickable(selenium, locator):
    try:
        WebDriverWait(selenium, 20).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        WebDriverWait(selenium, 20).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )
    except:
        pytest.fail(f"Element to wait {locator} is not found")


# wait 20 seconds until element disappears
def wait_invisible(selenium, locator):
    try:
        WebDriverWait(selenium, 20).until(
            EC.invisibility_of_element_located((By.XPATH, locator))
        )
    except:
        pytest.fail(f"Element to wait {locator} is not found")


# scroll element into view
def scroll_into_view(selenium, locator):
    try:
        selenium.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", locator)
    except:
        pytest.fail(f"Element {locator} is not found")


def scroll_into_view2(selenium, locator):
    try:
        scroll_to_element = locator.location_once_scrolled_into_view
        scroll_element_to_center = selenium.execute_script("window.scrollBy(0, -150)", "")
    except:
        pytest.fail(f"Element {locator} is not found")


# turn text into callable url
def text_to_credential(text):
    credentials_text = text.replace(" ", "_").upper()
    return credentials_text


#return data table as list
def table_return_list(table_name):
    check_fields = table_name.split("\n")
    remove_border = [x.strip(" |") for x in check_fields]
    return remove_border[1:]


#return data table as dict
def table_return_dict(table_name):
    check_fields = table_name.split("\n")
    remove_border = [x.strip(" | ") for x in check_fields]
    turn_into_dict = {x.replace(" | ", "' : '") for x in remove_border}
    return turn_into_dict

# --- Find Element Shortcuts ---

def by_xpath(selenium, locator):
    elem = selenium.find_element(By.XPATH, locator)
    return elem


def by_xpath_multiple(selenium, locator):
    elem = selenium.find_elements(By.XPATH, locator)
    return elem


def by_contains_text(selenium, text):
    dynamic_text = f"//*[contains(text(), '{text}')]"
    by_xpath(selenium, dynamic_text)


def by_id(selenium, locator):
    elem = selenium.find_element(By.ID, locator)
    return elem


def by_class(selenium, locator):
    elem = selenium.find_element(By.CLASS_NAME, locator)
    return elem

