import requests
import pandas as pd
import time
from datetime import datetime, timedelta

def fetch_usgs_data(start_date, end_date, min_magnitude=0):
    """
    Fetch earthquake data from USGS API for Indonesia in a date range
    """
    base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    
    params = {
        'format': 'geojson',
        'starttime': start_date,
        'endtime': end_date,
        'minmagnitude': min_magnitude,
        'minlatitude': -11,
        'maxlatitude': 6,
        'minlongitude': 95,
        'maxlongitude': 141,
        'limit': 20000  # max per request
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['features']
    else:
        print(f"Error fetching data: {response.status_code}")
        return []


def process_usgs_data(features):
    """Process USGS earthquake data into a DataFrame"""
    earthquakes = []
    
    for feature in features:
        props = feature['properties']
        coords = feature['geometry']['coordinates']
        
        earthquake = {
            'id': feature['id'],
            'time': datetime.fromtimestamp(props['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S'),
            'longitude': coords[0],
            'latitude': coords[1],
            'depth': coords[2],
            'magnitude': props['mag'],
            'magnitude_type': props.get('magType', None),
            'place': props['place'],
            'type': props['type'],
            'alert': props.get('alert', None),
            'tsunami': props.get('tsunami', 0),
            'significance': props.get('sig', None),
            'felt': props.get('felt', None),
            'cdi': props.get('cdi', None),
            'mmi': props.get('mmi', None),
            'status': props.get('status', None),
            'net': props.get('net', None)
        }
        earthquakes.append(earthquake)
    
    return pd.DataFrame(earthquakes)

# Scrape 5 years of data with magnitude 4.0+ to get substantial but manageable dataset
def scrape_usgs_multi_year(years=5, min_magnitude=4.0):
    all_data = []
    end_date = datetime.now()
    
    for year in range(years):
        start_date = end_date - timedelta(days=365)
        print(f"Fetching data from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
        
        features = fetch_usgs_data(
            start_date.strftime('%Y-%m-%d'), 
            end_date.strftime('%Y-%m-%d'), 
            min_magnitude
        )
        
        all_data.extend(features)
        end_date = start_date
        
        # Be nice to the server
        time.sleep(2)
    
    return process_usgs_data(all_data)

# Execute
earthquake_df = scrape_usgs_multi_year(years=10, min_magnitude=4.0)
print(f"Total records: {len(earthquake_df)}")
print(earthquake_df.head())

# Save to CSV
earthquake_df.to_csv('./collectiondata/usgs_earthquake_data_ID.csv', index=False)