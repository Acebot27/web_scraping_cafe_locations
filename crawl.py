from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from time import sleep
import csv

# Create a Chrome driver and crawl the URL
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/berlin')

sleep(25)  # give time for all javascripts to be finished running
page = driver.page_source
soup = bs(page, "lxml")

# Find restaurant list
content = soup.find('ul', class_='ubsf_sitemap-list')
restaurantList = content.find_all('div', class_='ubsf_sitemap-location-address')

# Create dataset
with open(f'Restaurants.csv', mode='w', newline='', encoding='utf-8') as outputFile:
    restaurantCSV = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    restaurantCSV.writerow(['restaurant', 'street', 'zip', 'city', 'country'])

    restaurantName = 'McDonalds'
    country = 'Germany'
    city = 'Berlin'
    for restaurant in restaurantList:
        street = restaurant.text.split(",")[0]
        zipCode = restaurant.text.split(",")[1][1:6]
        restaurantCSV.writerow([restaurantName, street, zipCode, city, country])

driver.close()