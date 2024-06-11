from selenium import webdriver
from selenium.webdriver.common.by import By
import time


userName = "bzarnitz91@outlook.com"
password = "Isles#91bz"
driver = webdriver.Chrome()

  

#open program and log into account
driver.get("https://app.dataannotation.tech/users/sign_in")
time.sleep(5)

userNameButton = driver.find_element(By.XPATH, '//*[@id="user_email"]')
passwordButton = driver.find_element(By.XPATH, '//*[@id="user_password"]')
login = driver.find_element(By.XPATH, '//*[@id="new_user"]/div[3]/input')

userNameButton.send_keys(userName)
time.sleep(1)

passwordButton.send_keys(password)
time.sleep(1)

login.click()
time.sleep(2)

driver.get("https://app.dataannotation.tech/workers/tasks/abcbfb1f-ca8a-4b77-a4bd-b98ad7f25774?task_response_id=fb35ecce-8026-43f2-ae10-6399010ab155")
time.sleep(3)
textbox = driver.find_element(By.XPATH, '//*[@id="question-1"]/div/div[2]/div[2]/div/textarea')


textbox.send_keys("Write me a function in java that will use an API to give me the time it will take to the nearest gas station. This function will take in coordintates for my current location in coordinates.")


driver.quit()