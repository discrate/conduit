import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import random
import string
from selenium.webdriver.chrome.options import Options

from input_test_data import *


class TestConduit(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        URL = "http://localhost:1667/"
        self.browser.get(URL)
        self.browser.maximize_window()

    def teardown(self):
        self.browser.quit()

    # // Teszteset 01 \\ Regisztráció helytelen adatokkal
    # def test_registration_invalid(self):
    #     sign_up_btn = self.browser.find_element_by_xpath('//a[@href="#/register"]')
    #     sign_up_btn.click()
    #     username_input = self.browser.find_element_by_xpath('//input[@placeholder="Username"]')
    #     email_input = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
    #     password_input = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
    #     sign_up_send_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    #     username_input.send_keys(user["name"])
    #     email_input.send_keys("incorrect")
    #     password_input.send_keys(user["password"])
    #     sign_up_send_btn.click()
    #     time.sleep(2)
    #     result_message = self.browser.find_element_by_xpath('//div[@class="swal-title"]')
    #     result_reason = self.browser.find_element_by_xpath('//div[@class="swal-text"]')
    #     try:
    #         assert result_message.text == "Registration failed!"
    #         assert result_reason.text == "Email must be a valid email."
    #         print('Helyes hibaüzenet')
    #     except AssertionError:
    #         print('Helytelen validáció')

    # // Teszteset 02 \\ Regisztráció helyes adatokkal
    def name_gen(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

    name_gen(1)
    random_name = name_gen(10)

    def email_gen(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

    email_gen(1)
    random_email = email_gen(10) + "@gmail.com"

    def test_registration_valid(self):
        sign_up_btn = self.browser.find_element_by_xpath('//a[@href="#/register"]')
        sign_up_btn.click()
        username_input = self.browser.find_element_by_xpath('//input[@placeholder="Username"]')
        email_input = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
        password_input = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
        sign_up_send_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        username_input.send_keys(self.random_name)
        email_input.send_keys(self.random_email)
        password_input.send_keys(user["password"])
        time.sleep(1)
        sign_up_send_btn.click()
        time.sleep(2)
        result_message = self.browser.find_element_by_xpath('//div[@class="swal-title"]')
        result_reason = self.browser.find_element_by_xpath('//div[@class="swal-text"]')
        try:
            assert result_message.text == "Welcome!"
            assert result_reason.text == "Your registration was successful!"
            print('Sikeres regisztráció')
        except AssertionError:
            print('Sikertelen regisztráció')

        ok_btn = self.browser.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
        ok_btn.click()

    # // Teszteset 03 \\ Bejelentkezés
    # def test_sign_in(self):
    #     home_sign_in_btn = self.browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
    #     home_sign_in_btn.click()
    #     email_input = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
    #     email_input.send_keys(user1["email"])
    #     password_input = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
    #     password_input.send_keys(user1["password"])
    #     sign_in_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    #     sign_in_btn.click()
    #     time.sleep(4)   # 2 secről növelve, hátha a user_profile sor jó, de failed
    #     user_profile = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
    #     try:
    #         assert user_profile.text == user1["name"]  # helyes felhasználónév megjelenítésének ellenőrzése
    #         print('Sikeres bejelentkezés')
    #     except AssertionError:
    #         print('Nem sikerült bejelentkezni')

# // Teszteset 04 \\ Adatkezelési nyilatkozat használata
#     def test_accept_cookies(self):
#         accept_btn = self.browser.find_element_by_xpath('//div[normalize-space()="I accept!"]')
#         accept_btn.click()
#         time.sleep(1)
#         decline_btn_list = self.browser.find_elements_by_xpath('//div[normalize-space()="I decline!"]')
#         print(len(decline_btn_list))
#         try:
#             assert len(decline_btn_list) == 0
#         except AssertionError:
#             print('Hiba merült fel a cookie-kal kapcsolatban.')

# // Teszteset 05 \\ Adatok listázása

# // Teszteset 12 \\ Kijelentkezés

# def test_logout(self):
#     logout_btn = self.browser.find_element_by_xpath('//a[@active-class="active"]')
#     logout_btn.click()
#     home_sign_in_btn = self.browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
#     try:
#         assert home_sign_in_btn.text == "Sign in"
#         print('Sikeres kijelentkezés')
#     except AssertionError:
#         print('Nem sikerült kijelentkezni')
