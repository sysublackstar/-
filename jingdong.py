import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


target_item = '茅台'

browser = webdriver.Chrome()
browser.get("https://www.jd.com/")
browser.find_element(By.LINK_TEXT, "你好，请登录").click()
print(f"请尽快扫码登录")
time.sleep(10)
browser.get("https://cart.jd.com/cart_index")
time.sleep(4)

while datetime.now().hour != 12:
    time.sleep(0.001)
    # 等待12点开始抢购

cart_items = browser.find_elements(By.CSS_SELECTOR, 'div.item-item')
for item in cart_items:
    item_name = item.find_element(By.CSS_SELECTOR, 'div.p-name').text
    if target_item in item_name:
        item.find_element(By.CSS_SELECTOR, 'div.cart-checkbox').click()
        print(f'{target_item}已被选中')
        break

browser.find_element(By.LINK_TEXT, "去结算").click()


while True:
    if browser.find_element(By.CSS_SELECTOR, 'button.checkout-submit').click():
        print(f"抢购成功，请尽快付款")
        break
    time.sleep(0.001)
