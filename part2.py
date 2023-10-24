#Under Development!

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep


csv_directory = "output files"
all_dataframes = []
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(csv_directory, filename)
        df = pd.read_csv(filepath)
        all_dataframes.append(df)

combined_dataframe = pd.concat(all_dataframes, ignore_index=True)
output_filepath = os.path.join(csv_directory, "combined_data.csv")
combined_dataframe.to_csv(output_filepath, index=False, encoding='utf-8')
print(f"Combined data written to: {output_filepath}")


driver = webdriver.Firefox()

url = 'https://www.amazon.in/Wesley-Milestone-Waterproof-Backpack-Business/dp/B084JGJ8PF/ref=sr_1_4?keywords=bags&qid=1697885232&sr=8-4&th=1'
driver.get(url)

for _ in range(15):  
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    sleep(2)

th_class_name = 'a-color-secondary a-size-base prodDetSectionEntry'


th_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, th_class_name))
)


th_text = th_element.text.strip()


if 'Manufacturer' in th_text:
    
    td_element = th_element.find_element(By.XPATH, './following-sibling::td')
    
   
    td_text = td_element.text.strip()
    
    print(f'Manufacturer: {td_text}')
else:
    print('Manufacturer information not found.')


driver.quit()

