# Importing the time module for handling time-related functionalit
import time
# Importing the pandas library and aliasing it as 'pd' for convenient use
import pandas as pd

class StatisticsCalculation:
    """
    Module
    """
    def __init__(self):
        self.all         = "all"
        self.empty_list  = ['','']
        self.separator   = "    :   "

    def time_stats(self, df:pd.DataFrame, month, day):
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
        if month == self.all:
            data["Most Popular Month:"] = [self.separator,df['month'].mode()[0]]
        # filtering the most common day of week
        if day == self.all:
            data["Most popular day of the week:"] = [self.separator,df['day_of_week'].mode()[0]]
        # filtering the most common start hour
        data["Most popular hour of the Month:"] = [self.separator,df['hour'].mode()[0]]
        # Adding empty row in table
        data[""] = self.empty_list
        # Adding time spend for calucation
        data["This took (seconds)"] = [self.separator,f'{time.time() - start_time}']

        return pd.DataFrame(data=data.values(), index=data.keys(), columns=self.empty_list)

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
        data["Most commonly used start station:"] = [self.separator,df['Start Station'].mode()[0]]
        # display most commonly used end station
        data["Most commonly used end station:"] = [self.separator,df['End Station'].mode()[0]]
        # display most frequent combination of start station and end station trip
        data["Most frequent combination:"] = [self.separator,df['combination_sation'].mode()[0]]

        # Adding empty row in table
        data[""] = self.empty_list
        # Adding time spend for calucation
        data["This took (seconds)"] = [self.separator,f'{time.time() - start_time}']

        return pd.DataFrame(data=data.values(), index=data.keys(), columns=self.empty_list)

    def trip_duration_stats(self, df:pd.DataFrame):
        """
        Filtering statistics on the total and average trip duration.
        """

        start_time = time.time()
        # Create empty dictionary
        data = {}
        # display total travel time
        data["Total travel time (Hours)"] = [self.separator,df["Trip Duration"].sum()]
        # display mean travel time
        data["The average(mean) travel time (Hours)"] = [self.separator,df["Trip Duration"].mean()]
        # Adding empty row in table
        data[""] = self.empty_list
        # Adding time spend for calucation
        data["This took (seconds)"] = [self.separator,f'{time.time() - start_time}']
        return pd.DataFrame(data=data.values(), index=data.keys(), columns=self.empty_list)


    def user_stats(self, df:pd.DataFrame):
        """
        Filtering statistics on bikeshare users.
        """
        start_time = time.time()
        # Create empty dictionary
        data = {}

        data["User Types"] = self.empty_list
        # Display counts of user types
        data["Total counts of all user types"] = [self.separator,df["User Type"].count()]
        user_type = df.groupby(['User Type'])['User Type'].count()

        for each_user in user_type.keys():
            data[f'Total counts of {each_user}'] = [self.separator,user_type[each_user]]

        # Display counts of gender
        if "Gender" in df.columns:
            # Adding empty row in table
            data["Gender"] = self.empty_list

            data["Total counts of all gender"] = [self.separator,df["Gender"].count()]
            gender = df.groupby(['Gender'])['Gender'].count()

            for each_gender in gender.keys():
                data[f'Total count of {each_gender}'] = [self.separator,gender[each_gender]]

        # Display earliest, most recent, and most common year of birth
        if "Birth Year" in df.columns:
            # Adding empty row in table
            data["Birth Year"] = self.empty_list
            # Display earliest year of birth
            data["The oldest year of birth"] = [self.separator,df['Birth Year'].min()]
            # Display most recent year of birth
            data["Most recent year of birth"] = [self.separator,df['Birth Year'].max()]
            # Display most commonly used start station
            data["Most command year of birth"] = [self.separator,df['Birth Year'].mode()[0]]

        # Adding empty row in table
        data[""] = self.empty_list
        # Adding time spend for calucation
        data["This took (seconds)"] = ["    :   ",f'{time.time() - start_time}']
        return pd.DataFrame(data=data.values(), index=data.keys(), columns=self.empty_list)
