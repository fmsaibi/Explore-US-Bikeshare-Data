# Importing the time module for handling time-related functionalit
import time
# Importing the pandas library and aliasing it as 'pd' for convenient use
import pandas as pd
# Importing constants variable  and aliasing it as 'cs' for convenient use
from app.constants import CommonConstants, DisplayMessages, TableHeader

class StatisticsCalculation:
    """
    Module
    """
    def time_stats(self, df:pd.DataFrame, month:str, day:str):
        """ 
        Filtering statistics on the most frequent times of travel.

        Args:
            df(DataFrame): Data retrun from csv file
            month(String): The Month the user would like to filter the data 
            day(String): The Day the user would like to filter the data 

        Returns:
            DataFrame: table of the filtred data
        """
        start_time = time.time()
        # Create empty dictionary
        data = {}
        # filtering most common month
        if month == CommonConstants.ALL:
            data[DisplayMessages.MOST_POPULAR_MONTH] = [CommonConstants.SEPARATOR,df[TableHeader.MONTH].mode()[0]]
        # filtering the most common day of week
        if day == CommonConstants.ALL:
            data[DisplayMessages.MOST_POPULAR_DAY] = [CommonConstants.SEPARATOR,df[TableHeader.DAY_OF_WEEK].mode()[0]]
        # filtering the most common start hour
        data[DisplayMessages.MOST_POPULAR_HOUR] = [CommonConstants.SEPARATOR,df[TableHeader.HOUR].mode()[0]]
        # Adding empty row in table
        data[CommonConstants.NULL] = CommonConstants.EMPTY_LIST
        # Adding time spend for calucation
        data[DisplayMessages.SECONDS_TOOK] = [CommonConstants.SEPARATOR,f'{time.time() - start_time}']
        return pd.DataFrame(data=data.values(), index=data.keys(), columns=CommonConstants.EMPTY_LIST)

    def station_stats(self, df:pd.DataFrame):
        """
        Filtering statistics on the most popular stations and trip.
        
        Args:
            df(DataFrame): Data retrun from csv file
            month(String): The Month the user would like to filter the data 
            day(String): The Day the user would like to filter the data 

        Returns:
            DataFrame: table of statistical station stats
        """
        start_time = time.time()
        # Create empty dictionary
        data = {}
        # display most commonly used start station
        data[DisplayMessages.MOST_COMMONLY_START_STATION] = [CommonConstants.SEPARATOR,df[TableHeader.START_STATION].mode()[0]]
        # display most commonly used end station
        data[DisplayMessages.MOST_COMMONLY_END_STATION] = [CommonConstants.SEPARATOR,df[TableHeader.END_STATION].mode()[0]]
        # display most frequent combination of start station and end station trip
        data[DisplayMessages.MOST_FREQUENT_COMBINATION] = [CommonConstants.SEPARATOR,df[TableHeader.COMBINE_STATION].mode()[0]]
        # Adding empty row in table
        data[CommonConstants.NULL] = CommonConstants.EMPTY_LIST
        # Adding time spend for calucation
        data[DisplayMessages.SECONDS_TOOK] = [CommonConstants.SEPARATOR,f'{time.time() - start_time}']
        return pd.DataFrame(data=data.values(), index=data.keys(), columns=CommonConstants.EMPTY_LIST)

    def trip_duration_stats(self, df:pd.DataFrame):
        """
        Filtering statistics on the total and average trip duration.
        """
        start_time = time.time()
        # Create empty dictionary
        data = {}
        # display total travel time
        data[DisplayMessages.TOTAL_TRAVEL_TIME] = [CommonConstants.SEPARATOR,df[TableHeader.TRIP_DURATION].sum()]
        # display mean travel time
        data[DisplayMessages.AVERAGE_TRAVEL_TIME] = [CommonConstants.SEPARATOR,df[TableHeader.TRIP_DURATION].mean()]
        # Adding empty row in table
        data[CommonConstants.NULL] = CommonConstants.EMPTY_LIST
        # Adding time spend for calucation
        data[DisplayMessages.SECONDS_TOOK] = [CommonConstants.SEPARATOR,f'{time.time() - start_time}']
        return pd.DataFrame(data=data.values(), index=data.keys(), columns=CommonConstants.EMPTY_LIST)

    def user_stats(self, df:pd.DataFrame):
        """
        Filtering statistics on bikeshare users.
        """
        start_time = time.time()
        # Create empty dictionary
        data = {}
        data[TableHeader.USER_TYPE] =CommonConstants.EMPTY_LIST
        # Display counts of user types
        data[DisplayMessages.TOTAL_COUNTS_OF_ALL_USER_TYPES] = [CommonConstants.SEPARATOR,df[TableHeader.USER_TYPE].count()]
        user_type = df.groupby([TableHeader.USER_TYPE])[TableHeader.USER_TYPE].count()

        for each_user in user_type.keys():
            data[DisplayMessages.TOTAL_COUNTS_OF + each_user] = [CommonConstants.SEPARATOR,user_type[each_user]]

        # Display counts of gender
        if TableHeader.GENDER in df.columns:
            # Adding empty row in table
            data[TableHeader.GENDER] = CommonConstants.EMPTY_LIST

            data[DisplayMessages.TOTAL_COUNTS_OF_ALL_GENDER] = [CommonConstants.SEPARATOR,df[TableHeader.GENDER].count()]
            gender = df.groupby([TableHeader.GENDER])[TableHeader.GENDER].count()

            for each_gender in gender.keys():
                data[DisplayMessages.TOTAL_COUNTS_OF + each_gender ] = [CommonConstants.SEPARATOR,gender[each_gender]]

        # Display earliest, most recent, and most common year of birth
        if TableHeader.BIRTH_YEAR in df.columns:
            # Adding empty row in table
            data[TableHeader.BIRTH_YEAR] = CommonConstants.EMPTY_LIST
            # Display earliest year of birth
            data[DisplayMessages.OLDEST_YEAR_OF_BIRTH] = [CommonConstants.SEPARATOR,df[TableHeader.BIRTH_YEAR].min()]
            # Display most recent year of birth
            data[DisplayMessages.MOST_RECENT_YEAR_OF_BIRTH] = [CommonConstants.SEPARATOR,df[TableHeader.BIRTH_YEAR].max()]
            # Display most commonly used start station
            data[DisplayMessages.MOST_COMMAND_YEAR_OF_BIRTH] = [CommonConstants.SEPARATOR,df[TableHeader.BIRTH_YEAR].mode()[0]]

        # Adding empty row in table
        data[CommonConstants.NULL] = CommonConstants.EMPTY_LIST
        # Adding time spend for calucation
        data[DisplayMessages.SECONDS_TOOK] = [CommonConstants.SEPARATOR,f'{time.time() - start_time}']
        return pd.DataFrame(data=data.values(), index=data.keys(), columns=CommonConstants.EMPTY_LIST)

    def individual_trip_data(self, df:pd.DataFrame, count:int):
        """
        This fuction retrun 5 row of individual trip data

        Args:
            df (pd.DataFrame): Table from csv file loaded
            count (int): Number of rows needed to be retruns from the tabls

        Returns:
            DataFrame: Table consist of 5 row of individual data
        """
        df = df.drop(columns=[TableHeader.MONTH,TableHeader.HOUR, TableHeader.DAY_OF_WEEK,TableHeader.COMBINE_STATION])

        return df.iloc[count:count+5]
