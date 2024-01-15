#Тест логина
from playwright.sync_api import Page
import pytest
import time
import datetime
now = datetime.datetime.now()
def test_title(page: Page):
    page.goto("http://185.22.63.39/sign-in")
    page.locator('//*[@id="at-field-username_and_email"]').fill('testееadmin') #Ввод юзернейма
    page.locator('//*[@id="at-field-password"]').fill('123123123') #Ввод пароля
    time.sleep(1)
    page.locator('//*[@id="at-btn"]').click()#Клик по кнопке Sign In
    time.sleep(1)
    header_exsists = page.locator('//*[@id="header-quick-access"]/ul/li[1]/a/div/p')#Поиск хедера
    header_exsists.text_content() == 'Тест_много карточек'#Соответствие хедера при успешном логине
