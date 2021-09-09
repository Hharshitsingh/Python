from selenium import webdriver
import time
edge_diver = r""
driver = webdriver.Edge(edge_diver)

driver.get("https://github.com/Hharshitsingh")
for i in range(1,10):
    time.sleep(0.5)
    driver.refresh()
driver.quit()
