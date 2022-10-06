import json

import requests
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def get_filtered_items(browser: WebDriver, min_price, max_price):
    prefix = 'view-source:'
    json_uri = f'https://inventories.cs.money/5.0/load_bots_inventory/730?hasRareStickers=true&hasStickers=true&hasTradeLock=true&isMarket=false&limit=60&minPrice={min_price}&maxPrice={max_price}&offset=0&order=desc&priceWithBonus=30&sort=price&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&type=5&type=6&type=3&type=4&withStack=true'
    uri = prefix + json_uri
    browser.get(uri)
    content = browser.find_element(By.CLASS_NAME, 'line-content').text
    data = json.loads(content)
    return data['items']


def set_filter(browser: WebDriver, min_price, max_price):
    url = f"https://cs.money/ru/csgo/trade/?minPrice={min_price}&maxPrice={max_price}&isMarket=false&hasRareStickers=true&hasTradeLock=true&hasStickers=true&type=Pistols&type=SMGs&type=Assault Rifles&type=Sniper Rifles"

    browser.get(url)

    #checkbox_classname = 'styles_checkbox__1oWu_'

    # cs.money items only
    #parent = browser.find_element(By.CLASS_NAME, 'CheckboxWithLabel_checkbox_with_label_container__SI11Y')
    #parent.find_element(By.CLASS_NAME, 'styles_checkbox__1oWu_').click()

    # set the price range
    #parent = browser.find_element(By.CLASS_NAME, 'FilterPrice_inputs__1atR8')
    #inputs = parent.find_elements(By.CLASS_NAME, 'styles_input__1osOB')
    #inputs[0].send_keys(str(min_price))
    #inputs[1].send_keys(str(max_price))

    #filters = browser.find_elements(By.CLASS_NAME, 'CollapseContainer_container__1_wT6')
    #for filter in filters:
    #    filter.click()

    # select weapon types
    #checks = filters[2].find_elements(By.CLASS_NAME, checkbox_classname)
    #for i in range(2, 6):
    #    checks[i].click()

    # trade locked only
    #checks = filters[4].find_elements(By.CLASS_NAME, checkbox_classname)
    #checks[1].click()

    # with stickers only
    #checks = filters[6].find_elements(By.CLASS_NAME, checkbox_classname)
    #checks[1].click()

    # only stickers that add price
    #checks = filters[14].find_elements(By.CLASS_NAME, checkbox_classname)
    #checks[1].click()