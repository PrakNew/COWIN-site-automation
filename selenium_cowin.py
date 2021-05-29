# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:10:36 2021

@author: prakhar.newatia
"""

#https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
#//*[contains(text(),'District')]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def runthepage(driver,state,city,age,timing):

    browser = driver.get("https://www.cowin.gov.in/home") #opens the home page
    driver.maximize_window()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 300)") #scrolls the whole web page down
     
    
    #pincodeInput = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
    #pincodeInput.click()
    
     
    
    #pincodeInput.send_keys("208001")
    
     
    
    driver.find_element_by_xpath("//div[contains(text(),'Search by District')]").click()
    #//div[contains(text(),'Search by District')]
    #this is for selecting the search by pin / search by district
    
     
    
    time.sleep(1)
    
     
    
    driver.find_element_by_xpath("//mat-select[@id='mat-select-0']").click()
    #clicking on the first select state
    #//*[@id="mat-select-value-1"]/span
    
     
    
    time.sleep(1)
    #driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[4]/div/div[2]/label').click()
    
     
    
    
    #STATE
    
     
    #//*[@id="mat-option-1"]
    driver.find_element_by_xpath("//div[@id='mat-select-0-panel']").send_keys(Keys.DOWN)#selecting the dropdown and pressing the key down
    text = driver.find_element_by_xpath("//mat-option[@id='mat-option-1']").text#get the text for the first value in the dropdown
    print("sldfhalfasfladfhlasdhflhasf",text)
    i=1
    while(text.strip().lower() != state.strip()):
        text = driver.find_element_by_xpath("//mat-option[@id='mat-option-{0}']".format(i)).text
        i+=1
        
    driver.find_element_by_xpath("//mat-option[@id='mat-option-{0}']".format(i-1)).click()#selecting the state 
    time.sleep(1)
    
     
    
    #DISTRICT
    
     
    driver.find_element_by_xpath("//mat-select[@id='mat-select-2']").click()
    #driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/div[2]/mat-form-field/div/div[1]/div').click()
    #selecting the city dropdown
    
     
    
    driver.find_element_by_xpath("//div[@id='mat-select-2-panel']").send_keys(Keys.DOWN)
    text1 = driver.find_element_by_xpath("//mat-option[@id='mat-option-37']").text
    i=37
    while(text1.strip().lower() != city.strip()):
        text1 = driver.find_element_by_xpath("//mat-option[@id='mat-option-{0}']".format(i)).text
        print(text1,'--------')
        i+=1
        
    driver.find_element_by_xpath("//mat-option[@id='mat-option-{0}']".format(i-1)).click()
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(text(),'Search')]").click()
    #selecting search
    
     
    
    if age.strip() == '45':

        driver.find_element_by_xpath("//label[contains(text(),'Age 45+')]").click()
    #selecting 45+
    elif age.strip() == '18':
        driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()
    #selecting 18+
    else:
        driver.find_element_by_xpath("//label[contains(text(),'Age 18+')]").click()
        driver.find_element_by_xpath("//label[contains(text(),'Age 45+')]").click()
    
    #driver.execute_script("window.scrollTo(0, 500)") 
    time.sleep(1)

    #------------------------- doing this for moving to the center of the page
    element = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-home[1]/div[2]/div[1]/appointment-table[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[7]/div[1]")
    
    desired_y = (element.size['height'] / 2) + element.location['y']
    current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
    scroll_y_by = desired_y - current_y
    driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    print(text,text1)
    #doing this for scrolling the web page
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.click()
    for x in range(10):
        actions.key_down(Keys.DOWN)
        actions.perform()
        time.sleep(0.5)
     
    
    print(driver.title)
    time.sleep(timing)
    driver.refresh()
    runthepage(driver,state,city,age,timing)
    
state = input("enter the state ")
city= input("enter the city ")
age= input("enter the age either 18 or 45 or both ")
timing = int(input("enter the timing in seconds in which the data will be refreshed (atleast 15 sec) "))
driver = webdriver.Chrome('D:/chromedriver')
runthepage(driver,state,city,age,timing)
 
    
