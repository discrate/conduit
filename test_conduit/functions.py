from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import string
from input_test_data import *


def registration_invalid(browser, username, email, password):
    sign_up_btn = browser.find_element_by_xpath('//a[@href="#/register"]')
    sign_up_btn.click()
    username_input = browser.find_element_by_xpath('//input[@placeholder="Username"]')
    email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    sign_up_send_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    username_input.send_keys(username)
    email_input.send_keys(email)  # helytelen email formátum szándékos megadása
    password_input.send_keys(password)
    sign_up_send_btn.click()
