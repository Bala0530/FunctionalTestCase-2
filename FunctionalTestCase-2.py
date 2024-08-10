# LIST OF IMPORTS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

# Load webdriver
driver = webdriver.Chrome()

# Opening web page
driver.get ('https://demo.dealsdray.com/')

# Login to the page
driver.find_element (By.ID,'mui-1').send_keys('prexo.mis@dealsdray.com')
driver.find_element (By.ID,'mui-2').send_keys('prexo.mis@dealsdray.com')
# Click login button
driver.find_element (By.XPATH,'/html/body/div/div/div/div/div[2]/div/form/div[3]/div/button').click()
time.sleep (2)

# Click order
driver.find_element (By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[1]/div[2]/button').click()
time.sleep (5)
# Click orders
driver.find_element (By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/a/button').click()
time.sleep (5)


# Empty click on body of the web to locate and click bulk
# NOTE
# I see this as a unwanted click to go out from the dashboard !!!!!!!!!!!!!!!!!!!!
driver.find_element (By.XPATH,'/html/body/div/div/div[1]/div/div[3]').click()
time.sleep (5)

# Click Add Bulk Orders
driver.find_element (By.XPATH,'/html/body/div/div/div/div[2]/div/div/div[2]/div[2]/button').click()
time.sleep (5)

# Choose file path and send through send keys
File_input = driver.find_element (By.XPATH,'/html/body/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/input')
filePath = "C:\\Users\\bbala\\Downloads\\demo-data.xlsx" # Replace the file path
File_input.send_keys (filePath)
time.sleep (5)
# Click import to read the file
driver.find_element (By.XPATH,'/html/body/div/div/div/div[2]/div/div/div[2]/div[3]/button').click()
time.sleep (5)

# Click Validate Button
driver.find_element (By.XPATH,'/html/body/div/div/div/div[2]/div/div/div[2]/div[3]/button').click()
time.sleep (5)
# Alert window
alrt = driver.switch_to.alert
# Acceot the alert
alrt.accept ()
time.sleep (5)

# Take screen shot of the page
driver.save_screenshot ("screenshot.png")
time.sleep (10)
