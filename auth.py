from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from steam_totp import generate_twofactor_code_for_time
import json


class MobileAuth:
    def __init__(self, path, password):
        self.password = password
        with open(path, "r") as read_file:
            data = json.load(read_file)
            self.username = data["account_name"]
            self.secret = data["shared_secret"]


def check_auth(browser: WebDriver):
    authorized = False

    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'TradeBalance_balance__2Hxq3')))
        authorized = True
    except:
        authorized = False

    return authorized


def cookie_auth(browser: WebDriver):
    try:
        browser.get('https://cs.money/')
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)
            for cookie in cookies:
                browser.add_cookie({'name': cookie['name'], 'value': cookie['value']})
        browser.get('https://cs.money/')
    finally:
        return False


def steam_auth(browser, user: MobileAuth):
    try:
        browser.find_element(By.CLASS_NAME, 'styles_login_button__ujo8x').click()
        browser.find_element(By.ID, 'steamAccountName').send_keys(user.username)
        browser.find_element(By.ID, 'steamPassword').send_keys(user.password)
    finally:
        browser.find_element(By.ID, 'imageLogin').click()

    if not check_auth(browser):
        try:
            code = get_steam_code(user.secret)
            code_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'twofactorcode_entry')))
            code_input.send_keys(code)
            button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[type=submit].auth_button')))
            button.click()
        finally:
            if check_auth(browser):
                print('saving cookies')
                cookies = browser.get_cookies()
                with open('cookies.json', 'w') as file:
                    json.dump(cookies, file)


def get_steam_code(secret):
    return generate_twofactor_code_for_time(shared_secret=secret)
