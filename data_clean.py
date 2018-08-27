import pandas as pd
import numpy as np

import pickle

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_squared_log_error

import secret_key
import re

def f(x):
    return x[0][:-2]

def filter_stations(input):
    return (re.sub(r"[0-9]+[a-zA-Z][a-zA-Z]", f, input)).upper()

def load_pickle(filename):
    f = open(filename, 'rb')
    df = pickle.load(f)
    f.close()

    return df

def store_pickle(filename, df):
    f = open(filename, 'wb')
    pickle.dump(df, f)
    f.close()

mta_loc = load_pickle('storage/mta_loc.pckl')

def get_mta_loc():
    print("Getting MTA Locations...")
    mta_loc = pd.read_csv("data/mta_turnstile/StationEntrances.csv")

    mta_loc['Station_Name'] = mta_loc.Station_Name.apply(filter_stations)
    mta_loc['Line'] = mta_loc['Line'].apply(lambda x : x.upper())

    mta_loc[['Route_1', 'Route_2', 'Route_3', 'Route_4', 'Route_5', 'Route_6', 'Route_7', 'Route_8', 'Route_9', 'Route_10', 'Route_11']] = mta_loc[['Route_1', 'Route_2', 'Route_3', 'Route_4', 'Route_5', 'Route_6', 'Route_7', 'Route_8', 'Route_9', 'Route_10', 'Route_11']].fillna('')
    mta_loc['Linename'] = mta_loc['Route_1'] + mta_loc['Route_2'] + mta_loc['Route_3'] + mta_loc['Route_4'] + mta_loc['Route_5'] + mta_loc['Route_6'] + mta_loc['Route_7']

    mta_loc = mta_loc.groupby(['Station_Name', 'Linename', 'Division'])['Station_Latitude', 'Station_Longitude'].mean().reset_index()
    mta_loc['zone'] = mta_loc['Station_Name'] + " " + mta_loc['Linename'] + " " + mta_loc['Division']

    store_pickle('storage/mta_loc.pckl', mta_loc)


def clean_mta(df, mta_loc):
    df['DATE'] = pd.to_datetime(df.DATE)
    df['month'] = df.DATE.dt.month
    df['year'] = df.DATE.dt.year
    df['day_of_week'] = df.DATE.dt.weekday_name
    df['TIME'] = pd.to_datetime(df['TIME'], format='%H:%M:%S')
    df['time_of_day'] = df.TIME.dt.hour
    df['DATE'] = pd.to_datetime(df.DATE).dt.date

    df = df.rename(index=str, columns={'EXITS                                                               ': "EXITS"})
    df['DELTA'] = df['EXITS'].diff().abs()
    df = df[df.time_of_day != 3]
    df = df[df.DELTA < 8600]

    df['day_of_the_month'] = pd.to_datetime(df.DATE).dt.day
    df['zone'] = df['STATION'] + " " + df['LINENAME'] + " " + df['DIVISION']

    df = df.groupby(['zone', 'DATE', 'time_of_day'])['DELTA'].sum().reset_index()

    return df

def bin_time(x):
    if x.hour <= 3 or x.hour == 24:
        return 3
    elif x.hour < 7:
        return 7
    elif x.hour < 11:
        return 11
    elif x.hour < 15:
        return 15
    elif x.hour < 19:
        return 19
    else:
        return 23

def biketomtazone(coor):
    lat = coor[0]
    long = coor[1]
    bike_id = coor[2]

    for index, location in mta_loc.iterrows():
        station_lat = location['Station_Latitude']
        station_long = location['Station_Longitude']
        if( ((station_lat + 0.002000) >= lat)  and ((station_lat - 0.002000) <= lat) ):
            if( ((station_long + 0.003000) >= long) and ((station_long - 0.003000) <= long) ):
                if(mta_loc['bike_station'][index] == 0):
                    mta_loc['bike_station'][index] = bike_id
                    return location['zone']
                elif(mta_loc['bike_station'][index] == bike_id):
                    return location['zone']
    return False

def clean_citibike(df):
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Stop Time'] = pd.to_datetime(df['Stop Time'])
    df['month'] = df['Start Time'].dt.month
    df['year'] = df['Start Time'].dt.year
    df['day_of_week_name'] = df['Start Time'].dt.weekday_name
    df['time_of_day'] = df['Start Time'].dt.hour
    df['DATE'] = df['Start Time'].dt.date
    df["time_of_day"] = df["Start Time"].apply(bin_time)
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['day_of_month'] = df['Start Time'].dt.day

    print("Mapping bike station with subway...")
    mta_loc['bike_station'] = 0
    df['zone'] = df[['Start Station Latitude', 'Start Station Longitude', 'Start Station ID']].apply(biketomtazone,  axis=1)

    return df