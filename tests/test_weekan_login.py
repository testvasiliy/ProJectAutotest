#Тест логина
from playwright.sync_api import sync_playwright
import time
import datetime
now = datetime.datetime.now()
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    try:
        page = browser.new_page()
        delay = 10
        url = "http://185.22.63.39/sign-in"
        page.goto(url)
        page.locator('//*[@id="at-field-username_and_email"]').fill('testtadmin') #Ввод юзернейма
        page.locator('//*[@id="at-field-password"]').fill('123123123') #Ввод пароля
        time.sleep(1)
        page.locator('//*[@id="at-btn"]').click()#Клик по кнопке Sign In
        time.sleep(1)
        header_exsists = page.locator('//*[@id="header-quick-access"]/ul/li[1]/a/div/p')#Проверка по наличию заголовка, добленного у юзера в избранное. Если совпадает с указанным - значит вход выполнен успешно 
        if header_exsists.text_content() == 'Тест_много карточек':
            print('OK', 'LOGIN SUCCESSFUL', now.strftime("%d-%m-%Y %H:%M:%S"))
        else:
            print('NOT OK', 'LOGIN FAILED', now.strftime("%d-%m-%Y %H:%M:%S"))
        time.sleep(3)                                        
    except:
        print('NOT OK, SOMETHING WENT WRONG', now.strftime("%d-%m-%Y %H:%M:%S"))
    time.sleep(4)
