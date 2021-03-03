from selenium import webdriver
edge_driver = r"C://Users/HARSHIT SINGH/Development/Edge_Driver/msedgedriver.exe"
driver = webdriver.Edge(executable_path=edge_driver)
url = "https://www.python.org/events/"
driver.get(url)

event_time = driver.find_elements_by_css_selector("time")
event_title = driver.find_elements_by_class_name("event-title")
event_location = driver.find_elements_by_class_name("event-location")

event_title_list = [event.text for event in event_title]
event_time_list = [event.text for event in event_time]
event_location_list = [event.text for event in event_location]


event  = {i:{
    "Event Time":event_time_list[i],
    "Event Tittle":event_title_list[i],
    "Event Location":event_location_list[i]}
    for i in range(len(event_title_list))}
print(event)
driver.close()



