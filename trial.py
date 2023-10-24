from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep

# Set up the Selenium WebDriver (make sure you have chromedriver installed)
driver = webdriver.Firefox()

# Replace 'your_url_here' with the actual URL you want to scrape
url = 'https://www.amazon.in/Wesley-Milestone-Waterproof-Backpack-Business/dp/B084JGJ8PF/ref=sr_1_4?keywords=bags&qid=1697885232&sr=8-4&th=1'
driver.get(url)

for _ in range(15):  
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    sleep(2)
# Replace 'your_th_class' with the actual class name of the th tag
th_class_name = 'a-color-secondary a-size-base prodDetSectionEntry'

# Wait for the th element to be present with a longer wait time
th_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, th_class_name))
)

# Get the text of the th element
th_text = th_element.text.strip()

# Check if the th text contains "Manufacturer"
if 'Manufacturer' in th_text:
    # Find the corresponding td element
    td_element = th_element.find_element(By.XPATH, './following-sibling::td')
    
    # Get the text of the td element
    td_text = td_element.text.strip()
    
    print(f'Manufacturer: {td_text}')
else:
    print('Manufacturer information not found.')

# Close the WebDriver
driver.quit()
