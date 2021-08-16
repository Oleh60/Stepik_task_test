import pytest
from selenium import webdriver
import time
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"




def test_button_language(browser):
    browser.get(link)
    button = browser.find_element_by_xpath('//button[contains(@class,"btn-lg")]')
    # time.sleep(30)
    assert len(button.text), "Button not found"

