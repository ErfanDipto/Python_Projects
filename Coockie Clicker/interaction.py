from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "Z:/Python Projects/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")
# article_number = driver.find_element_by_css_selector("#articlecount a")
# print(article_number.text)
#
# search = driver.find_element_by_name(name="search")
# python_search = search.send_keys("python")
# search.send_keys(Keys.ENTER)

# englist_click = driver.find_element_by_xpath(xpath='//*[@id="articlecount"]/a[2]')

driver.find_element_by_name("fName").send_keys("First_Name")
driver.find_element_by_name("lName").send_keys("Last_Name")
driver.find_element_by_name("email").send_keys("EMAIL@ADDR.com")
driver.find_element_by_xpath('/html/body/form/button').click()

# driver.quit()
