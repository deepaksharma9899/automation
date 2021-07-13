from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# type this command in terminal
# chrome.exe -remote-debugging-port=9014 --user-data-dir="C:\Users\Neeraj Sharma\AppData\Local\Google\Chrome\User Data\Profile 1"




options = Options()

options.add_experimental_option("debuggerAddress", "localhost:9014")

driver = webdriver.Chrome(options=options)

while True:
    driver.get("https://ads.google.com/aw/campaigns?ocid=86111406&euid=266286189&__u=1582619461&uscid=86111406&__c=3259413694&authuser=0")
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="cmExtensionPoint-id"]/base-root/div/div[2]/div[1]/view-loader/campaign-view/tableview/div[4]/div/section/toolbelt/toolbelt-bar[1]/div[2]/div[7]/element/toolbelt-material-menu/material-menu/material-button').click()
    time.sleep(8)
    driver.find_element_by_xpath('/html/body/div[4]/div[5]/div/div/div[2]/div[2]/div/menu-item-groups/div[2]/material-select-item[6]').click()
    time.sleep(20)


    driver.get("https://ads.google.com/aw/campaigns?ocid=367869996&workspaceId=0&euid=266286189&__u=1582619461&uscid=367869996&__c=9422406604&authuser=0")
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="cmExtensionPoint-id"]/base-root/div/div[2]/div[1]/view-loader/campaign-view/tableview/div[4]/div/section/toolbelt/toolbelt-bar[1]/div[2]/div[7]/element/toolbelt-material-menu/material-menu/material-button').click()
    time.sleep(8)
    driver.find_element_by_xpath('/html/body/div[4]/div[4]/div/div/div[2]/div[2]/div/menu-item-groups/div[2]/material-select-item[6]').click()
    time.sleep(900)




