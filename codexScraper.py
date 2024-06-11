from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import sqlite3


driver = webdriver.Chrome()
url = "https://ideator.yootils.com/generators/15"
driver.get(url)

conn = sqlite3.connect("codexPromptData.db")
cur = conn.cursor()

#cur.execute('''CREATE TABLE Prompts(
 #           first text, 
  #          second text, 
   #         third text, 
    #        fourth text, 
     #       fifth text            
      #      )''')

# Wait for user to login into the website
continueBTN = input('type yes when logged in:')
print(continueBTN)
if continueBTN.lower() != 'yes':
    print('program exited')
    driver.quit()
    quit()


wait = WebDriverWait(driver, 20)
generateBTN = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div/div/div[2]/div[1]/button')))

for x in range(1000):#looping through

    #load up new information
    try:
        # Using JavaScript to click the button
        driver.execute_script("arguments[0].click();", generateBTN)
    except Exception as e:
        print(f"Error clicking the button: {e}")
    time.sleep(15)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')


    #find the instructions from the page
    h2_element = soup.find('h2', string='Instructions:')
    if h2_element:
        ul_element = h2_element.find_next('ul')#find the next ul after the instructions header
        if ul_element:
            listItems = ul_element.find_all('li')
            item_texts = []
            for li in listItems:
                item_texts.append(li.text)
            
            while len(item_texts) < 5:
                item_texts.append('')
            
            if len(item_texts) > 5:
                while len(item_texts) > 5:
                    item_texts.pop(len(item_texts)-1)



            # Insert the data into the database
            cur.execute('''
                INSERT INTO Prompts (first, second, third, fourth, fifth)
                VALUES (?, ?, ?, ?, ?)
            ''', item_texts)
            conn.commit()

            query = "SELECT COUNT(*) FROM Prompts"
            cur.execute(query)

            # Fetch and print the rows
            total_rows = cur.fetchone()[0]
            print("row:",total_rows)

            for text in item_texts:
                print(text)
        else:
            print("Error: Could not find the list items under the 'Instructions' header")
    else: 
        print("Error: Could not find the 'Instructions' header")




cur.close()
conn.close()
driver.quit() 