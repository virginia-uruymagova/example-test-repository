from functions import *

# --- Inspection Page Locators (INSP) ---

INSP_HEADER = "//*[@data-bind='text:TaskTextSupplier']"
INSP_SAVE_BUTTON = "//span[contains(text(), 'Save')]/../../button"
INSP_ID = "//*[@data-bind='text:DataCollRecordID' and text() != '']"
INSP_SYNCED_TEXT = "//*[contains(text(), 'Synced to server')]"
INSP_SYNCED_ICON = "//*[@class='green checkmark icon']"

# --- Checkpoint Element Locators ---
CP_CAMERA = "//*[@class='large camera icon']"
CP_SIGNATURE = "//*[@data-bind='click: startSignature']"
CP_SIGNATURE_CANVAS = "//*[@class='upper-canvas cm-edit__canvas']"
CP_SIGNATURE_SAVE = "//*[@title='Save']"
CP_ATTACHMENT = "/../../..//img"
CP_CA_NOTE = "//summernote[contains(@params, 'Corrective Action')]/./div"
CP_CA_NOTE_EDIT = "//div[@class='note-editable']/p"
CP_R4R = "//div[contains(@data-bind, 'ReadyForReview')]/label"
CP_RP_DROPDOWN = "//div[@class='ui floating dropdown']/div/input"

CP_DUE_DATE_PICKER = "//i[@class='calendar icon']/../input"
CP_DATE_PICK_NEXT_MONTH = "//*[contains(@class, 'pika-single')] and not[contains(@class, 'is-hidden')]//button[@class='pika-next']"
CP_DATE_PICK_FIRST_DAY = "//*[contains(@class, 'pika-single')] and not[contains(@class, 'is-hidden')]//td[@data-day='1']/button"

# --- Pop Up Dialogs ---
POP_CP_STATUS_CONFIRM = "//div[@class='ui modal transition visible active']/div/div[@class='ui ok primary button']"


# --- Dynamic Locators ---

def INSP_CHECKPOINT(selenium, checkpoint):  # what is better way to store parameterized locators?
    all_checkpoints = by_xpath_multiple(selenium, "//*[contains(@data-bind, 'text: CheckpointText')]")
    index = [txt.text for txt in all_checkpoints].index(checkpoint) + 1
    checkpoint_xpath = f"//div[contains(@data-bind, 'checkpoints.visible')]/div[{index}]"
    return checkpoint_xpath


def CP_RP_DROPDOWN_SELECTION(selenium, checkpoint, text):
    rp_dropdown = by_xpath(selenium, INSP_CHECKPOINT(selenium, checkpoint) + CP_RP_DROPDOWN)
    scroll_into_view2(selenium, rp_dropdown)
    click_rp_dropdown = rp_dropdown.click()
    all_rps_in_list = by_xpath_multiple(selenium, "//div[@class='menu transition visible']/div/div")
    index = [txt.text for txt in all_rps_in_list].index(text) + 1
    dropdown_xpath = f"//div[@class='menu transition visible']/div/div[{index}]"
    return dropdown_xpath


def CHECKPOINT_STATUS():
    checkpoint_status_dict = {
        "FTQ": "//div[@class='ui special ftq checkbox']/input",
        "OPN": "//div[@class='ui special ca checkbox']/input",
        "QC": "//div[@class='ui special stq checkbox']/input"
    }
    return checkpoint_status_dict

#
# def INSP_CHECKPOINTS(selenium, text):
#     all_checkpoints = by_xpath_multiple(selenium, "//*[contains(@data-bind, 'text: CheckpointText')]")
#     checkpoint_names_list = [txt.text for txt in all_checkpoints]
#     checkpoint_name_has = text
#     indices = [i+1 for i in range(len(checkpoint_names_list)) if checkpoint_name_has in checkpoint_names_list[i]]
#     checkpoint_xpaths = [x for x in indices if f"//div[contains(@data-bind, 'checkpoints.visible')]/div[{indices}]"]
#     print(checkpoint_xpaths)
#     return checkpoint_xpaths
