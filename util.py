from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser
import datetime

def wait_for_element_to_be_clickable(driver, element, by):
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((by, element))
    )

def loop_calendar(calendar_element):
    print()