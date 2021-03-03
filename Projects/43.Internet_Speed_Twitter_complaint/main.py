from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PROMISE_DOWN = 150
PROMISE_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""
INTERNET_SPEED_CHECK_URL = "https://www.speedtest.net/"
edge_driver_path = r""

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Edge(executable_path=driver_path)
        self.up = 0
        self.down = 0
    
    def get_internert_speed(self):
        self.driver.get(INTERNET_SPEED_CHECK_URL)
        time.sleep(2)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.up)
        print(self.down)


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISE_DOWN}down/{PROMISE_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(edge_driver_path)
bot.get_internert_speed()
bot.tweet_at_provider()


