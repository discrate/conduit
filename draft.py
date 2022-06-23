import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser_options = Options()
# browser_options.headless = True
browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
browser.implicitly_wait(10)
URL = "http://localhost:1667/"
browser.get(URL)


# browser.maximize_window()


# def email_gen():
#     userx = {
#         "counter": 992,
#         "name": "szgtest",
#         "domain": "gmail.com",
#         "password": "Tesztelek1"
#     }
#     email = f'{userx["name"]}{userx["counter"]}@{userx["domain"]}'
#     userx['counter'] += 1
#     print(userx["counter"])
#     return email


# def random_char(y):
#     return ''.join(random.choice(string.ascii_letters) for x in range(y))
#
#
# random_char(1)
# email_gen = random_char(10) + "@gmail.com"


# // Teszteset 03 \\ Bejelentkezés
# def sign_in():
#     home_sign_in_btn = browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
#     # sign_in_btn = browser.find_elements_by_xpath('//a[normalize-space()="Sign in"]')[0]
#     home_sign_in_btn.click()
#     email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
#     email_input.send_keys(user1["email"])
#     password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
#     password_input.send_keys(user1["password"])
#     sign_in_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
#     sign_in_btn.click()
#     time.sleep(2)
#     user_profile = browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
#     # user_profile = browser.find_element_by_xpath('//a[@class="nav-link"][normalize-space()="szgteszt1"]')
#     try:
#         assert user_profile.text == user1["name"]  # helyes felhasználónév megjelenítésének ellenőrzése
#         print('Sikeres bejelentkezés')
#     except AssertionError:
#         print('Nem sikerült bejelentkezni')


def sign_in():
    home_sign_in_btn = browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
    home_sign_in_btn.click()
    email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    email_input.send_keys("szgteszt1@gmail.com")
    password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    password_input.send_keys("Tesztelek1")
    sign_in_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_btn.click()
    time.sleep(2)
    user_profile = browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
    assert user_profile.text == "szgteszt1"


def add_comments_from_input():
    first_article = browser.find_elements_by_xpath('//h1')[1]
    first_article.click()
    time.sleep(1)
    comment_box = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))
    with open('test_conduit/input_comments.csv', 'r', encoding='UTF-8') as input_f:
        text = csv.reader(input_f, delimiter=',')
        counter = 0
        for row in text:
            comment_box.send_keys(row[1])
            post_comment_btn = browser.find_element_by_xpath('//button[text()="Post Comment"]')
            post_comment_btn.click()
            counter += 1
            time.sleep(0.3)
    comments_list = browser.find_elements_by_xpath('//div[@class="card"]')
    assert len(comments_list) == counter


sign_in()
add_comments_from_input()
