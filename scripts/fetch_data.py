# This Script will fetch the data from the api
''' plz properly comment the changes and the code :-)'''

# importing the required libraries

import requests
import logger
import pandas as pd
import load_env
import os
import datetime

# loading environment variables
load_env.load_env()


# defining the class
class FetchData :
    def __init__(self):
        # defining the url
        self.url = os.environ.get("WEATHER_API")
        self.key = os.environ.get("WEATHER_API_KEY")

        # defining the headers
        self.headers = headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

        # defining the logger
        self.logger = logger.get_logger(__name__)
        self.dataframe = None

    # defining the function to fetch the data
    def fetch_data(self,date):

        # defining the url
        url = self.url.format(self.key,date)

        # fetching the data from the api
        response = requests.get(url, headers=self.headers)
        response_status = response.status_code

        try:
            # checking if the response is successful
            if response_status == 200:
                # returning the data
                self.logger.info("Data fetched successfully")
                return response.json().get('observations')

            else:
                # returning the error message
                self.logger.error(f"Data not fetched error {response_status}")
                return False

        except Exception as e:
            logger.error(f"Cant fetch data {e}")
            return False

    def to_dataframe(self,data):

        # columns to be extracted
        columns =['valid_time_gmt','expire_time_gmt','temp','dewPt','rh','pressure',
                  'wdir','wdir_cardinal','gust','wspd','precip_total','precip_hrly',
                  'vis',"clds","wx_phrase"]

        # naming the columns
        names = ["valid_time","expire_time","temperature","dew_point","relative_humidity",
                 "pressure","wind_direction","wind_direction_cardinal","gust","wind_speed",
                 "precipitation_total","precipitation_hourly","visibility","clouds","weather_phrase"]

        # creating the dataframe
        self.dataframe = pd.DataFrame(data, columns=columns)
        self.dataframe.columns = names

        self.logger.info("Dataframe created successfully")

    def get_date(self):
        # getting current datetime
        date = datetime.datetime.now()

        return date.strftime("%Y%m%d")

    def run(self):

        # fetching the data
        data = self.fetch_data(self.get_date())

        if data:
            # converting the data to dataframe
            self.to_dataframe(data)
        else:
            logger.error("Cant create dataframe")
    # function to get dataframe
    def get_dataframe(self):
        return self.dataframe

data = FetchData()
data.run()
