from selenium import webdriver
from selenium.webdriver.common.by import By
import time


from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# input_form_fname = driver.find_element(By.NAME, 'fName')
# input_form_fname.send_keys("M. Abdullah")
# input_form_lname = driver.find_element(By.NAME, 'lName')
# input_form_lname.send_keys("Bin Aftab")
# input_form_email = driver.find_element(By.NAME, 'email')
# input_form_email.send_keys("binaftaba@gmail.szoom")
# button = driver.find_element(By.XPATH,'/html/body/form/button')
# button.click()

# timeout = 5 #seconds
# timeout_start = time.time()
#
# cookie = driver.find_element(By.XPATH,'//*[@id="cookie"]')
#
# while time.time() < timeout_start + timeout :
#     cookie.click()

# panel_list = []
right_panel = driver.find_elements(By.ID, 'store')
for panel in right_panel:
    panel_text=(panel.text)
    # print(panel_text)

splitting = panel_text.split("\n")
print(splitting)
print(type(splitting))





