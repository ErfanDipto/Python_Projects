from selenium import webdriver
import time


webdriver_path = "Z:/Python Projects/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(webdriver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

money = 0

while True:
    # cookies = driver.find_element_by_id("cookie").click()
    # money = int(driver.find_element_by_id("money").text)

    # cursor_click = driver.find_element_by_xpath('//*[@id="buyCursor"]').click()
    # grandma_click = driver.find_element_by_xpath('//*[@id="buyGrandma"]').click()
    # factory_click = driver.find_element_by_xpath('//*[@id="buyFactory"]').click()
    # mine_click = driver.find_element_by_xpath('//*[@id="buyMine"]').click()
    # shipment_click = driver.find_element_by_xpath('//*[@id="buyShipment"]').click()
    # alchemy_lab_click = driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]').click()
    # portal_click = driver.find_element_by_xpath('//*[@id="buyPortal"]').click()
    click = True

    close_time = time.time() + 5*60

    while click:
        cookies = driver.find_element_by_id("cookie").click()
        money = int(driver.find_element_by_id("money").text.replace(",", ""))
        if time.time() >= close_time:
            click = False

    # cursor_click
    if 15 <= money < 100:
        driver.find_element_by_xpath('//*[@id="buyCursor"]').click()
    elif 100 <= money < 500:
        driver.find_element_by_xpath('//*[@id="buyGrandma"]').click()
    elif 500 <= money < 2000:
        driver.find_element_by_xpath('//*[@id="buyFactory"]').click()
    elif 2000 <= money < 7000:
        driver.find_element_by_xpath('//*[@id="buyMine"]').click()
    elif 7000 <= money < 50000:
        driver.find_element_by_xpath('//*[@id="buyShipment"]').click()
    elif 50000 <= money < 100000:
        driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]').click()
    elif 100000 <= money < 123456789:
        driver.find_element_by_xpath('//*[@id="buyPortal"]').click()
    elif money >= 123456789:
        driver.find_element_by_xpath('//*[@id="buyTime machine"]').click()


    # print(store_list)
    # print(money)
