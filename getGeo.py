import pandas as pd
import requests
import json

GOOGLE_API_KEY = 'AIzaSyCKXJT1QGzbAOVW6kMzGInjM8BSjiLLelc'


def extract_address_from_scraped_data(restaurants_df: pd.DataFrame):
    addresses_list = []
    for i, row in restaurants_df.iterrows():
        addresses_list.append(str(restaurants_df.iloc[i]['street']) + ', ' + str(restaurants_df.iloc[i]['zip']) + ', '
                              + str(restaurants_df.iloc[i]['city']) + ', ' + str(restaurants_df.iloc[i]['country']))
    return addresses_list


def extract_lat_long_via_address(address_or_zipcode):
    lat, lng = None, None
    api_key = GOOGLE_API_KEY
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address_or_zipcode}&key={api_key}"
    # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except Exception as e:
        print(e)
        pass
    return lat, lng


def store_lat_lng_data_in_a_csv_file(filename: str = 'Restaurants.csv'):
    address_df = pd.read_csv(filepath_or_buffer=filename)
    # print(address_df.head())
    address_list = extract_address_from_scraped_data(restaurants_df=address_df)
    lat_list = []
    lng_list = []
    for i, address in enumerate(address_list):
        latitude, longitude = extract_lat_long_via_address(address_or_zipcode=address)
        lat_list.append(latitude)
        lng_list.append(longitude)

    address_df['latitude'] = lat_list
    address_df['longitude'] = lng_list

    address_df.to_csv(path_or_buf='Restaurants_GEO.csv', index=False)
    print(address_df.head())
    return


store_lat_lng_data_in_a_csv_file()
# print(len(extract_address_from_scraped_data()))