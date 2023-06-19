# web_scraping_cafe_locations
Visualizing Berlin's McDonalds addresses on an interactive map

Scraped Berlin's McDonalds addresses from their website and using Geocoding API finding their latitude and longitude location and plotting them on maps using Folium API package in python.

To execute the project correctly run the scripts in the following way:
- crawl.py -> script for scraping Berlin's McDonalds store addresses from the McDonalds website and saving them in a CSV file.
- getGeo.py -> script for extracting latitude and longitude value from the addresses saved above using Google Geocoding API and merging them into the CSV file.
- visualization.py -> Plotting these above acquired latitude and longitude values in an interactive map using Folium API package in python.
