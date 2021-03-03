from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

EDGE_DRIVER_PATH = ""
SIMILAR_ACCOUNT = ""
USERNAME = ""
PASSWORD = ""
class Insta:
    def __init__(self):
        self.driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)
        self.login()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        time.sleep(3)

        password.send_keys(Keys.ENTER)


    def find_following(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(3)

        following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following.click()
        # followers.click()
        time.sleep(3)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.follow()
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        print(all_buttons)
        print()
        for button in all_buttons:
            print(button)
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
        
    def find_followings(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{USERNAME}")
        time.sleep(3)

        following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following.click()
        time.sleep(3)
        # modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        # for i in range(10):
        #     # self.follow()
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(2)

    def unfollow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        # print(all_buttons)
        print()
        for button in all_buttons:
            print(button)
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                time.sleep(3)
                cancel_button = self.driver.find_element_by_css_selector("button[1] .aOOlW")
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
                cancel_button.click()
    
    
bot = Insta()
bot.find_following()
bot.follow()