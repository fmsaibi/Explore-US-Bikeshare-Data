# Importing the time module for handling time-related functionalit
import time
# Importing the pandas library and aliasing it as 'pd' for convenient use
import pandas as pd
# Importing constants variable  and aliasing it as 'cs' for convenient use
import app.constants as cs

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
        if month == cs.ALL:
            data[cs.DISPLAY_MOST_POPULAR_MONTH] = [cs.SEPARATOR,df[cs.MONTH].mode()[0]]
        # filtering the most common day of week
        if day == cs.ALL:
            data[cs.DISPLAY_MOST_POPULAR_DAY] = [cs.SEPARATOR,df[cs.DAY_OF_WEEK].mode()[0]]
        # filtering the most common start hour
        data[cs.DISPLAY_MOST_POPULAR_HOUR] = [cs.SEPARATOR,df[cs.HOUR].mode()[0]]
        # Adding empty row in table
        data[cs.NULL] = cs.EMPTY_LIST
        # Adding time spend for calucation
        data[cs.DISPLAY_SECONDS_TOOK] = [cs.SEPARATOR,f'{time.time() - start_time}']
        return pd.DataFrame(data=data.values(), index=data.keys(), columns=cs.EMPTY_LIST)

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
        data[cs.DISPLAY_MOST_COMMONLY_START_STATION] = [cs.SEPARATOR,df[cs.START_STATION].mode()[0]]
        # display most commonly used end station
        data[cs.DISPLAY_MOST_COMMONLY_END_STATION] = [cs.SEPARATOR,df[cs.END_STATION].mode()[0]]
        # display most frequent combination of start station and end station trip
        data[cs.DISPLAY_MOST_FREQUENT_COMBINATION] = [cs.SEPARATOR,df[cs.COMBINE_STATION].mode()[0]]
        # Adding empty row in table
        data[cs.NULL] = cs.EMPTY_LIST
        # Adding time spend for calucation
        data[cs.DISPLAY_SECONDS_TOOK] = [cs.SEPARATOR,f'{time.time() - start_time}']
        return pd.DataFrame(data=data.values(), index=data.keys(), columns=cs.EMPTY_LIST)

    def trip_duration_stats(self, df:pd.DataFrame):
        """
        Filtering statistics on the total and average trip duration.
        """
        start_time = time.time()
        # Create empty dictionary
        data = {}
        # display total travel time
        data[cs.DISPLAY_TOTAL_TRAVEL_TIME] = [cs.SEPARATOR,df[cs.TRIP_DURATION].sum()]
        # display mean travel time
        data[cs.DISPLAY_AVERAGE_TRAVEL_TIME] = [cs.SEPARATOR,df[cs.TRIP_DURATION].mean()]
        # Adding empty row in table
        data[cs.NULL] = cs.EMPTY_LIST
        # Adding time spend for calucation
        data[cs.DISPLAY_SECONDS_TOOK] = [cs.SEPARATOR,f'{time.time() - start_time}']
        return pd.DataFrame(data=data.values(), index=data.keys(), columns=cs.EMPTY_LIST)

    def user_stats(self, df:pd.DataFrame):
        """
        Filtering statistics on bikeshare users.
        """
        start_time = time.time()
        # Create empty dictionary
        data = {}
        data[cs.USER_TYPE] =cs.EMPTY_LIST
        # Display counts of user types
        data[cs.DISPLAY_TOTAL_COUNTS_OF_ALL_USER_TYPES] = [cs.SEPARATOR,df[cs.USER_TYPE].count()]
        user_type = df.groupby([cs.USER_TYPE])[cs.USER_TYPE].count()

        for each_user in user_type.keys():
            data[cs.DISPLAY_TOTAL_COUNTS_OF + each_user] = [cs.SEPARATOR,user_type[each_user]]

        # Display counts of gender
        if cs.GENDER in df.columns:
            # Adding empty row in table
            data[cs.GENDER] = cs.EMPTY_LIST

            data[cs.DISPLAY_TOTAL_COUNTS_OF_ALL_GENDER] = [cs.SEPARATOR,df[cs.GENDER].count()]
            gender = df.groupby([cs.GENDER])[cs.GENDER].count()

            for each_gender in gender.keys():
                data[cs.DISPLAY_TOTAL_COUNTS_OF + each_gender ] = [cs.SEPARATOR,gender[each_gender]]

        # Display earliest, most recent, and most common year of birth
        if cs.BIRTH_YEAR in df.columns:
            # Adding empty row in table
            data[cs.BIRTH_YEAR] = cs.EMPTY_LIST
            # Display earliest year of birth
            data[cs.DISPLAY_THE_OLDEST_YEAR_OF_BIRTH] = [cs.SEPARATOR,df[cs.BIRTH_YEAR].min()]
            # Display most recent year of birth
            data[cs.DISPLAY_MOST_RECENT_YEAR_OF_BIRTH] = [cs.SEPARATOR,df[cs.BIRTH_YEAR].max()]
            # Display most commonly used start station
            data[cs.DISPLAY_MOST_COMMAND_YEAR_OF_BIRTH] = [cs.SEPARATOR,df[cs.BIRTH_YEAR].mode()[0]]

        # Adding empty row in table
        data[cs.NULL] = cs.EMPTY_LIST
        # Adding time spend for calucation
        data[cs.DISPLAY_SECONDS_TOOK] = [cs.SEPARATOR,f'{time.time() - start_time}']
        return pd.DataFrame(data=data.values(), index=data.keys(), columns=cs.EMPTY_LIST)

    def individual_trip_data(self, df:pd.DataFrame, count:int):
        """
        This fuction retrun 5 row of individual trip data

        Args:
            df (pd.DataFrame): Table from csv file loaded
            count (int): Number of rows needed to be retruns from the tabls

        Returns:
            DataFrame: Table consist of 5 row of individual data
        """
        df = df.drop(columns=[cs.MONTH,cs.HOUR, cs.DAY_OF_WEEK,cs.COMBINE_STATION])

        return df.iloc[count:count+5]
