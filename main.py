from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import auth
import trade
from evaluation import Evaluator


def main():
    user = auth.MobileAuth('steam_account.json')
    browser = webdriver.Chrome(ChromeDriverManager().install())
    auth.cookie_auth(browser)
    if not auth.check_auth(browser):
        auth.steam_auth(browser, user)


    #items: list = trade.get_filtered_items(browser, 2.5, 5)
    #trade.set_filter(browser, 2.5, 5)
    #evaluator = Evaluator('evaluation_sums.json')
    #items = sorted(items, key=evaluator.get_score)
    #print([(item['name'], item['price'], evaluator.get_score(item)) for item in items])

    #sleep(1000)
    #text = input()
    #print(text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
