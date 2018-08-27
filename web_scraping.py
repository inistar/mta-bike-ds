import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

def scrape_mta_data():
    url = "http://web.mta.info/developers/"
    response = requests.get(url+"turnstile.html")

    soup = BeautifulSoup(response.text, 'lxml')
    for link in soup.find_all('a'):
        if '2017' in link.get_text().split(' '):
            d_file = link.get("href")
            print("Downloading " + d_file + "...")
            response = requests.get(url+d_file)

            file_name = d_file.split("/")[-1]

            fp = open('data/'+ file_name, 'w')
            fp.write(response.text)
            fp.close()

            time.sleep(10)

files = ['201701-citibike-tripdata.csv.zip',
'201702-citibike-tripdata.csv.zip',
'201703-citibike-tripdata.csv.zip',
'201704-citibike-tripdata.csv.zip',
'201705-citibike-tripdata.csv.zip',
'201706-citibike-tripdata.csv.zip',
'201707-citibike-tripdata.csv.zip',]
files = ['201708-citibike-tripdata.csv.zip',
'201709-citibike-tripdata.csv.zip',
'201710-citibike-tripdata.csv.zip',
'201711-citibike-tripdata.csv.zip',
'201712-citibike-tripdata.csv.zip']

def scrape_citibike_data():
    url = "https://s3.amazonaws.com/tripdata/"

    for d_file in files:
        print("Downloading " + d_file + "...")
        response = requests.get(url+d_file)

        fp = open('data/'+ d_file, 'w')
        fp.write(response.text)
        fp.close()

        time.sleep(10)

if __name__ == '__main__':
    # scrape_mta_data()
    scrape_citibike_data()