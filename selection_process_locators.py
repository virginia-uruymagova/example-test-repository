# --- Selection Process Page Locators (SP) ---

from functions import by_xpath_multiple

SP_EMERGENCY_DICT = "//*[@class='refresh link icon']"
SP_DICT_LOADING_MODAL_OPEN = "//div[@class='ui modal transition visible active']"
SP_DICT_LOADING_MODAL_SUCCESS = "//*[@data-percent='100']"
SP_DICT_LOADING_MODAL_CLOSED = "//div[@class='ui modal transition hidden']"


SP_SELECT_GENERAL_PUNCH_CHECKLIST = "//div[contains(text(),'General-Punch List Deficiency (CT147)')]"
SP_SELECT_GENERAL_RP = "//div[contains(text(),'FTQ Automation Group')]"


# --- Dynamic Locators ---


def SPECIFIC_SELECTION(selenium, text):
    all_selections = by_xpath_multiple(selenium, "//div[@class='item-text']")
    titles_list = [txt.text for txt in all_selections]
    selection_name = text
    index = [i+1 for i in range(len(titles_list)) if selection_name in titles_list[i]]
    specific_selection_xpath = f"//ul[@class='cl-menu-ul']/li{index}/div/a"
    return specific_selection_xpath

#
# def SPECIFIC_CHECKLIST(selenium, text):
#     all_checklists = by_xpath_multiple(selenium, "//div[@class='item-text']")
#     checklist_titles_list = [txt.text for txt in all_checklists]
#     checklist_name = text
#     indices = [i+1 for i in range(len(checklist_titles_list)) if checklist_name in checklist_titles_list[i]]
#     specific_checklist_xpath = f"//ul[@class='cl-menu-ul']/li{[indices[0]]}/div/a"
#     return specific_checklist_xpath
