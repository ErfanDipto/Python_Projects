from selenium import webdriver

chrome_driver_path = "Z:/Python Projects/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
target = driver.get(url="https://www.python.org/")
price = driver.find_element_by_name(name="q")
# print(price.get_attribute("placeholder"))
# print(driver.find_element_by_css_selector(".documentation-widget a").get_property("href"))
event_list_driver = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
event_list_both = [event.text for event in event_list_driver]


event_dict = {}
count = 0
in_dict = {}

for event in event_list_both:
    in_dict["time"] = event.split("\n")[0]
    in_dict["name"] = event.split("\n")[1]
    event_dict[count] = in_dict
    count += 1

print(event_dict)
# driver.close()
driver.quit()
