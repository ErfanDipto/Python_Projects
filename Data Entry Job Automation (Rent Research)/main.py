from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time


webdriver_path = "Z:/Python Projects/chromedriver_win32/chromedriver.exe"
zillow_addr = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagin" \
              "ation%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-1" \
              "22.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.70334372401613" \
              "6%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%2" \
              "2%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C" \
              "%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cm" \
              "sn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%2" \
              "2%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B" \
              "%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%2" \
              "2%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22" \
              "mapZoom%22%3A11%7D"

form_addr = "https://docs.google.com/forms/d/e/1FAIpQLSfGMBhgJalBPdpxKVPZ0zMbJ77FyJx6c7-JbPF7ejZmFDCe" \
            "xQ/viewform?usp=sf_link"

add_addr = "https://www.zillow.com"

header_params = {"Accept-Language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-GB;q=0.6",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                               "Chrome/89.0.4389.72 Safari/537.36"}

response = requests.get(url=zillow_addr, headers=header_params)
# print(response)
# print(response.text)
response_html = response.text

soup = BeautifulSoup(response_html, "html.parser")
# print(soup.text)
# print(soup.select_one(".list-card-info a")
link_addr_soup = soup.select(".list-card-info a")
link_addr_list_unsup = [ele.get("href") for ele in link_addr_soup]
link_addr_list = []

for ele in link_addr_list_unsup:
    if "zillow" not in ele:
        ele = f"{add_addr}{ele}"
    else:
        pass
    link_addr_list.append(ele)

print(link_addr_list)


addr_soup = soup.select(".list-card-addr")
addr_list = [ele.text for ele in addr_soup]
# addr_list = [f"{add_addr}{ele}" for ele in addr_list_unsup if "zillow" not in ele]
# addr_list = []
print(addr_list)


price_soup = soup.select(".list-card-price")
price_list = [ele.text for ele in price_soup]
print(price_list)

for i in range(0, len(price_list)):
    driver = webdriver.Chrome(webdriver_path)
    driver.get(form_addr)
    time.sleep(5)
    addr_in_form = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]'
                                                '/div/div[1]/div/div[1]/input')
    price_in_form = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                 '/div/div[1]/div/div[1]/input')

    link_in_form = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
                                                '/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')

    addr_in_form.send_keys(addr_list[i])
    price_in_form.send_keys(price_list[i])
    link_in_form.send_keys(link_addr_list[i])
    submit_button.click()
    time.sleep(5)
    driver.quit()
    time.sleep(5)
