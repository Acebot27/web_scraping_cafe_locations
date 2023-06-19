import pandas as pd
import folium
from folium.plugins import MarkerCluster


# Create the base Map
m = folium.Map(location=[52.500, 13.50000],
               tiles='OpenStreetMap',
               zoom_start=8)

# Read the data
df = pd.read_csv("Restaurants_GEO.csv")

# Create the markers
markerCluster = MarkerCluster().add_to(m)
for i, row in df.iterrows():
    lat = df.iloc[i]['latitude']
    lng = df.iloc[i]['longitude']

    restaurant = df.iloc[i]['restaurant']
    popup = df.iloc[i]['restaurant'] + '<br>' + str(df.iloc[i]['street']) + '<br>' + str(df.iloc[i]['zip'])

    if restaurant == 'McDonalds':
        color = 'blue'
    else:
        color = 'red'

    folium.Marker(location=[lat, lng], popup=popup, icon=folium.Icon(color=color)).add_to(markerCluster)

m.save("restaurants_marked_index.html")