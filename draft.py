import random
import string


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


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


random_char(1)
email_gen = random_char(10) + "@gmail.com"




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

