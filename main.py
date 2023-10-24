from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os
from time import sleep

# Set a custom user agent to mimic a real browser
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

options = webdriver.FirefoxOptions()
options.add_argument(f"user-agent={user_agent}")

driver = webdriver.Firefox(options=options)

try:
    # Starting page URL
    base_url = "https://www.amazon.in/s?k=bags"

    for page_number in range(1, 10): 
        page_url = f"{base_url}&page={page_number}"

        driver.get(page_url)
        driver.implicitly_wait(10)

        #Explicit Wait
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')))

    
        for _ in range(5):  
            ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
            sleep(2)

        product_name_elements = driver.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
        rating_number_elements = driver.find_elements(By.XPATH, '//span[@class="a-size-base s-underline-text"]')
        star_rating_elements = driver.find_elements(By.XPATH, '//span[@class="a-icon-alt"]')
        price_elements = driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
        product_urls = driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
        
        # Extract and print the text content of each product name, number of ratings, and star rating, urls
        product_names = [element.text for element in product_name_elements]
        rating_numbers = [element.text for element in rating_number_elements]
        star_ratings = [element.get_attribute('innerHTML') for element in star_rating_elements]
        prices = [element.text for element in price_elements]
        urls = [element.get_attribute('href') for element in product_urls]
        
        sleep(5)        
        output_directory = "output files"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        with open(os.path.join(output_directory, f'product_details_page_{page_number}.csv'), 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Product Urls', 'Product Name', 'Product Price', 'Rating', 'Number of Reviews'])
            for url, name, price, star_rating, num_ratings in zip(urls, product_names, prices, star_ratings, rating_numbers):
                csv_writer.writerow([url, name, price, star_rating, num_ratings])

finally:
    driver.quit()
