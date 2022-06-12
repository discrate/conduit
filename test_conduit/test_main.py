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
from functions import *


class TestConduit(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.implicitly_wait(10)
        URL = "http://localhost:1667/"
        self.browser.get(URL)
        self.browser.maximize_window()

    def teardown(self):
        self.browser.quit()

    # // Teszteset 01 \\ Regisztráció helytelen adatokkal (helytelen email címmel)
    def test_registration_invalid(self):
        registration_invalid(self.browser, user["name"], user["email"], user["password"])
        time.sleep(2)
        result_message = self.browser.find_element_by_xpath('//div[@class="swal-title"]')
        result_reason = self.browser.find_element_by_xpath('//div[@class="swal-text"]')
        assert result_message.text == "Registration failed!"
        assert result_reason.text == "Email must be a valid email."


        # // Teszteset 01 \\ Regisztráció helytelen adatokkal (helytelen email címmel)

    # def test_registration_invalid(self):
    #     sign_up_btn = self.browser.find_element_by_xpath('//a[@href="#/register"]')
    #     sign_up_btn.click()
    #     username_input = self.browser.find_element_by_xpath('//input[@placeholder="Username"]')
    #     email_input = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
    #     password_input = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
    #     sign_up_send_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    #     username_input.send_keys(user["name"])
    #     email_input.send_keys("szgteszt1_gmail.com")  # helytelen email formátum szándékos megadása
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

    # // Teszteset 02 \\ Regisztráció helyes adatokkal (létrehozott random felhasználónévvel és email címmel)
    # def name_gen(y):
    #     return ''.join(random.choice(string.ascii_letters) for x in range(y))
    #
    # name_gen(1)
    # random_name = name_gen(10)
    #
    # def email_gen(y):
    #     return ''.join(random.choice(string.ascii_letters) for x in range(y))
    #
    # email_gen(1)
    # random_email = email_gen(10) + "@gmail.com"
    #
    # def test_registration_valid(self):
    #     sign_up_btn = self.browser.find_element_by_xpath('//a[@href="#/register"]')
    #     sign_up_btn.click()
    #     username_input = self.browser.find_element_by_xpath('//input[@placeholder="Username"]')
    #     email_input = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
    #     password_input = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
    #     sign_up_send_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    #     username_input.send_keys(self.random_name)
    #     email_input.send_keys(self.random_email)
    #     password_input.send_keys(user["password"])
    #     time.sleep(1)
    #     sign_up_send_btn.click()
    #     time.sleep(2)
    #     result_message = self.browser.find_element_by_xpath('//div[@class="swal-title"]')
    #     result_reason = self.browser.find_element_by_xpath('//div[@class="swal-text"]')
    #     try:
    #         assert result_message.text == "Welcome!"
    #         assert result_reason.text == "Your registration was successful!"
    #         print('Sikeres regisztráció')
    #     except AssertionError:
    #         print('Sikertelen regisztráció')
    #
    #     ok_btn = self.browser.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
    #     ok_btn.click()
    #
    # # // Teszteset 12 \\ Kijelentkezés (felhasználó kijelentkeztetése)
    # def test_logout(self):
    #     TestConduit.test_sign_in(self)
    #     logout_btn = self.browser.find_element_by_xpath('//a[@active-class="active"]')
    #     logout_btn.click()
    #     home_sign_in_btn = self.browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
    #     try:
    #         assert home_sign_in_btn.text == "Sign in"
    #         print('Sikeres kijelentkezés')
    #     except AssertionError:
    #         print('Nem sikerült kijelentkezni')
    #
    # # // Teszteset 03 \\ Bejelentkezés (felhasználó bejelentkezése helyes email cím és jelszó megadásával)
    # def test_sign_in(self):
    #     home_sign_in_btn = self.browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
    #     home_sign_in_btn.click()
    #     email_input = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
    #     email_input.send_keys(self.random_email)
    #     password_input = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
    #     password_input.send_keys(user1["password"])
    #     sign_in_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    #     sign_in_btn.click()
    #     time.sleep(2)
    #     # user_profile = self.browser.find_element_by_xpath('//a[@href="#/@szgteszt1/" and @class="nav-link"]')
    #     user_profile = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
    #     time.sleep(2)
    #     try:
    #         assert user_profile.text == self.random_name  # user1["name"] helyes felhasználónév megjelenítésének ellenőrzése
    #         print('Sikeres bejelentkezés')
    #     except AssertionError:
    #         print('Nem sikerült bejelentkezni')
    #
    # # // Teszteset 04 \\ Adatkezelési nyilatkozat használata (cookiek elfogadása)
    # def test_accept_cookies(self):
    #     accept_btn = self.browser.find_element_by_xpath('//div[normalize-space()="I accept!"]')
    #     accept_btn.click()
    #     time.sleep(1)
    #     decline_btn_list = self.browser.find_elements_by_xpath('//div[normalize-space()="I decline!"]')
    #     print(len(decline_btn_list))
    #     try:
    #         assert len(decline_btn_list) == 0
    #     except AssertionError:
    #         print('Hiba merült fel a cookie-kal kapcsolatban.')
    #
    # # // Teszteset 05 \\ Adatok listázása ("Popular tag"-ek listázása)
    # def test_popular_tag_list(self):
    #     popular_tags = self.browser.find_elements_by_xpath('//a[@class="tag-pill tag-default"]')
    #     list_of_tags = []
    #     for i, j in enumerate(popular_tags):
    #         list_of_tags.append(f'{i + 1}. elem: {j.text}')
    #     print(f'Popular Tags: {list_of_tags}')
    #     try:
    #         assert len(list_of_tags) == len(popular_tags)
    #         print(f'Helyes lista, elemek száma: {len(list_of_tags)}')
    #     except AssertionError:
    #         print('Helytelen lista')
    #
    # # // Teszteset 06 \\ Több oldalas lista bejárása (főoldal alján levő navigációs sáv bejárása)
    # def test_page_navigation(self):
    #     TestConduit.test_sign_in(self)
    #     index_page_list = self.browser.find_elements_by_xpath('//a[@class="page-link"]')
    #     for i in range(len(index_page_list)):
    #         page_button = index_page_list[i]
    #         page_button.click()
    #     time.sleep(1)
    #     try:
    #         assert index_page_list[-1].text == f'{len(index_page_list)}'
    #         print('Számozás rendben')
    #     except AssertionError:
    #         print('Számozás nincs rendben')
    #
    # # // Teszteset 07 \\ Új adatbevitel (új cikk létrehozása)
    # def test_adding_new_input(self):
    #     TestConduit.test_sign_in(self)
    #     new_article_btn = self.browser.find_element_by_xpath('//a[@href="#/editor"]')
    #     new_article_btn.click()
    #     time.sleep(2)
    #     article_title = self.browser.find_element_by_xpath('//input[@placeholder ="Article Title"]')
    #     article_title.send_keys(article['title'])
    #     article_about = self.browser.find_element_by_xpath('//input[contains(@placeholder, "this article about?")]')
    #     article_about.send_keys(article['about'])
    #     article_body = self.browser.find_element_by_xpath('//textarea[@placeholder ="Write your article (in markdown)"]')
    #     article_body.send_keys(article['body'])
    #     article_tag = self.browser.find_element_by_xpath('//input[@placeholder ="Enter tags"]')
    #     article_tag.send_keys(article['tag'])
    #     publish_article_btn = self.browser.find_element_by_xpath('//button[@type="submit"]')
    #     publish_article_btn.click()
    #     time.sleep(2)
    #     created_body = self.browser.find_element_by_xpath('//p')
    #     try:
    #         assert created_body.text == article['body']
    #         print('Helyesen létrehozva')
    #     except AssertionError:
    #         print('Helytelen cikk')
    #
    # # // Teszteset 09 \\ Meglevő adat módosítás (profilkép cseréje input file-ból)
    # def test_change_profile_pic(self):
    #     TestConduit.test_sign_in(self)
    #     settings_btn = self.browser.find_element_by_xpath('//a[@href="#/settings"]')
    #     settings_btn.click()
    #     image_path = self.browser.find_element_by_xpath('//input[@placeholder="URL of profile picture"]')
    #     image_path.clear()
    #     image_path.send_keys(profile_pic['Rick1'])
    #     update_settings_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    #     update_settings_btn.click()
    #     ok_btn = self.browser.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
    #     ok_btn.click()
    #     user_profile = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
    #     user_profile.click()
    #     time.sleep(2)
    #     # img_source= WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,
    #     # '//img[@class="user-img"]'))).get_attribute("src")
    #     img_source = self.browser.find_element_by_xpath('//img[@class="user-img"]').get_attribute("src")
    #     print(img_source)
    #     assert img_source == profile_pic['Rick1']
    #
    # # // Teszteset 10 \\ Adat vagy adatok törlése (komment hozzáadása, majd eltávolítása)
    # def test_delete_data(self):
    #     TestConduit.test_sign_in(self)
    #     first_article = self.browser.find_elements_by_xpath('//h1')[1]
    #     first_article.click()
    #     comment_box = WebDriverWait(self.browser, 5).until(
    #         EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))
    #     comments_list_before = self.browser.find_elements_by_xpath('//div[@class="card"]')
    #     comment_box.send_keys(comment["comment1"])
    #     post_comment_btn = self.browser.find_element_by_xpath('//button[text()="Post Comment"]')
    #     post_comment_btn.click()
    #     delete_btn = self.browser.find_element_by_xpath('//i[@class="ion-trash-a"]')
    #     delete_btn.click()
    #     time.sleep(1)
    #     comments_list_after = self.browser.find_elements_by_xpath('//div[@class="card"]')
    #     assert len(comments_list_after) == len(comments_list_before)
