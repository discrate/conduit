import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from test_conduit.input_test_data import article, user1
import random
import string

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://localhost:1667/#/")
browser.maximize_window()


# // Teszteset 05 \\ Adatok listázása




# // Teszteset 07 \\ Új adatbevitel


def sign_in():
    home_sign_in_btn = browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
    home_sign_in_btn.click()
    email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    email_input.send_keys(user1["email"])
    password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    password_input.send_keys(user1["password"])
    sign_in_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_btn.click()
    time.sleep(2)
    user_profile = browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
    try:
        assert user_profile.text == user1["name"]  # helyes felhasználónév megjelenítésének ellenőrzése
        print('Sikeres bejelentkezés')
    except AssertionError:
        print('Nem sikerült bejelentkezni')


def adding_new_input():
    new_article_btn = browser.find_element_by_xpath('//a[@href="#/editor"]')
    new_article_btn.click()
    time.sleep(2)
    article_title = browser.find_element_by_xpath('//input[@placeholder ="Article Title"]')
    article_title.send_keys(article['title'])
    article_about = browser.find_element_by_xpath('//input[contains(@placeholder, "this article about?")]')
    article_about.send_keys(article['about'])
    article_body = browser.find_element_by_xpath('//textarea[@placeholder ="Write your article (in markdown)"]')
    article_body.send_keys(article['body'])
    article_tag = browser.find_element_by_xpath('//input[@placeholder ="Enter tags"]')
    article_tag.send_keys(article['tag'])
    publish_article_btn = browser.find_element_by_xpath('//button[@type="submit"]')
    publish_article_btn.click()
    time.sleep(2)
    created_body = browser.find_element_by_xpath('//p')
    try:
        assert created_body.text == article['body']
        print('Helyesen létrehozva')
    except AssertionError:
        print('Helytelen cikk')


sign_in()
adding_new_input()

# try:
#     assert result_message.text == "Registration failed!"
#     assert result_reason.text == "Email must be a valid email."
#     print('Helyes hibaüzenet')
# except AssertionError:
#     print('Helytelen validáció')


# browser.quit()
