from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser
import datetime



def main():
    is_copper = True
    if is_copper:
        copper()
    else:
        winter_park()

def copper():
    driver = webdriver.Chrome()
    driver.get("https://www.coppercolorado.com/plan-your-trip/getting-here/parking")
    calendar = wait_for_element_to_be_clickable(driver, "CalendarMonth_table", By.CLASS_NAME)
    things = ''

def winter_park():
    mountains_ids = {}
    date = datetime.datetime(2021,1,1)
    print(date.strftime("%B"))

    driver = webdriver.Chrome()
    driver.get("https://account.ikonpass.com/en/login?redirect_uri=/en/myaccount/add-reservations/")
    email_input = driver.find_element_by_id('email')
    password_input = driver.find_element_by_id('sign-in-password')
    submit_button = driver.find_element_by_class_name('submit')
    config = configparser.ConfigParser()
    config.read("config.ini")

    email_input.send_keys(config.get('SaraCredentials', 'Username'))
    password_input.send_keys(config.get('SaraCredentials', 'Password'))
    submit_button.click()

    mountains_list = wait_for_element_to_be_clickable(driver, "react-autowhatever-resort-picker", By.ID)
    mountains = mountains_list.find_elements_by_tag_name("li")

    for mountain in mountains:
        mountains_ids[mountain.text] = mountain.get_attribute("id")

    is_copper = True


    day_found = False

    while not day_found:
        winter_park_li = wait_for_element_to_be_clickable(driver,"react-autowhatever-resort-picker-section-0-item-10", By.ID)
        winter_park_li.click()

        # Use direct path
        continue_button = wait_for_element_to_be_clickable(driver,"jxPclZ", By.CLASS_NAME)
        continue_button.click()

        # Clean up this logic
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "DayPicker")))

        daypicker_days = driver.find_elements_by_class_name("DayPicker-Day")

        for day in daypicker_days:
            if day.get_attribute("aria-label") == 'Wed Jan 20 2021':
                if 'DayPicker-Day--unavailable' in day.get_attribute("class"):
                    driver.refresh()
                    time.sleep(5)
                else:
                    day.click()
                    day_found = True
                break

    print("dummy")

    #all_passholders = True

    #if all_passholders

    main_tag = wait_for_element_to_be_clickable(driver,"//main", By.XPATH)
    checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

    # Better/more specific paths for these
    save_button = wait_for_element_to_be_clickable(driver,"lkoEyq", By.CLASS_NAME)
    save_button.click()

    continue_to_confirm_button = wait_for_element_to_be_clickable(driver,"dHRKUJ", By.CLASS_NAME)
    continue_to_confirm_button.click()

    confirm_check_box = wait_for_element_to_be_clickable(driver,"input", By.CLASS_NAME)
    confirm_check_box.click()

    submit_button = wait_for_element_to_be_clickable(driver,"jxPclZ", By.CLASS_NAME)
    submit_button.click()

    things = ''

if __name__ == '__main__':
    main()

