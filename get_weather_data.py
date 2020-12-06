# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:38:52 2020

@author: bjorn
"""

from wwo_hist import retrieve_hist_data
import pandas as pd
from ast import literal_eval
from geopy.geocoders import Nominatim
import re 
import os
os.chdir("C:/Users/bjorn/OneDrive/Dokument/University/DTU/42577 Introduction to Business Analytics/challenge/42577-Introduction-to-Business-Analytics/weather data")

cities = pd.read_csv('C:/Users/bjorn/OneDrive/Dokument/University/DTU/42577 Introduction to Business Analytics/challenge/42577-Introduction-to-Business-Analytics/location_from_pickle.csv', index_col=0, skipinitialspace=True)
# geolocator = Nominatim(user_agent="user_agent")
# location_list = []
# coord = cities['Location']
# for i in coord:
#     #
#     if type(i)!=str:
#         continue
#     c = literal_eval(i)
#     c = c[0], c[1]
#     print(c)
#     geo_loc = geolocator.reverse(c)
#     words = re.findall(r'\w+', geo_loc[0])
#     city = words[5]
#     print(city)
    
    
# geolocator.reverse((39.2908816, -76.610759))    

location_list = cities['City']
for i in location_list:
    frequency = 24
    start_date = '01-JAN-2018'
    end_date = '01-JAN-2019'
    api_key = '51f671d92fce4a8d9aa162950200612'
    # location_list = '1.352, 103.819
    try:
        hist_weather_data = retrieve_hist_data(api_key,
                                        location_list,
                                        start_date,
                                        end_date,
                                        frequency,
                                        location_label = False,
                                        export_csv = True,
                                        store_df = True)
    except:
        continue


type(hist_weather_data)

import pandas as pd
df = pd.read_csv('california.csv')
df.shape
df.columns
df['precipMM']

