from selenium import webdriver
from selenium.webdriver.common.keys import Keys


edge_driver = r""
driver = webdriver.Edge(executable_path=edge_driver)
url = "https://en.wikipedia.org/wiki/Main_Page"
url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)
# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(event_count.text)
# article_count.click()
# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()
# serch = driver.find_element_by_name("search")
# serch.send_keys("Python")

# serch.send_keys(Keys.ENTER)

fnam = driver.find_element_by_name("fName")
fnam.send_keys("HASRSHIT")

lnam = driver.find_element_by_name("lName")
lnam.send_keys("SINGH")

emai = driver.find_element_by_name("email")
emai.send_keys("harshitsingh@gmail.com")

# submit = driver.find_element_by_link_text("Sign Up")
submit = driver.find_element_by_class_name("btn-primary")

submit.send_keys(Keys.ENTER)





# driver.close()