from selenium import webdriver
from time import sleep
class InstaBot:
	def __init__(self, u, pw):
		self.driver = webdriver.Chrome()
		self.driver.get("https://instagram.com")
		sleep(2)
		name = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
		name.send_keys(u)
		passw = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
		passw.send_keys(pw)
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		sleep(4)
		self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()




InstaBot('write here your username','write your password')

while True:
	sleep(0.1)
