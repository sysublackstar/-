import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


target_item = '茅台'

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
browser.find_element(By.LINK_TEXT, "亲，请登录").click()
print(f"请尽快扫码登录")
time.sleep(10)
browser.get("https://cart.taobao.com/cart.htm")
time.sleep(4)

while datetime.now().hour != 12:
    time.sleep(0.001)
    # 等待12点开始抢购

cart_items = browser.find_elements(By.CSS_SELECTOR, 'ul.item-content')
for item in cart_items:
    item_name = item.find_element(By.CSS_SELECTOR, 'div.item-basic-info').text
    if target_item in item_name:
        item.find_element(By.CSS_SELECTOR, 'div.cart-checkbox').click()
        print(f'{target_item}已被选中')
        break

browser.find_element(By.LINK_TEXT, "结 算").click()


while True:
    if browser.find_element(By.LINK_TEXT, '提交订单').click():
        print(f"抢购成功，请尽快付款")
        break
    time.sleep(0.001)
