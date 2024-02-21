# Importing the pandas library and aliasing it as 'pd' for convenient use

import pandas as pd

class DataLoader:
    """
        (module) DataLoader
    """
    def __init__(self):
        self.df = pd.DataFrame

    def load_data(self, city:str, month:str, day:str) -> bool:
        """
        This function opens a CSV file named after the provided city in the 'data' directory.

        Args:
            city (str): The name of the city for which data needs to be loaded.
            month (str): The month for which data needs to be filtred.
            day (str): The day of the week for which data needs to filtred.

        Retrun:
            If the file is found, it retruns true. If the file is not found, it will retruns (false) 
            a FileNotFoundError is caught, and a message is printed.
        """
        #Converting space in name of the city to underscore
        formate_city = city.replace(" ","_")
        # Preapering file path address
        path = f"data/{formate_city}.csv"
        try:
            self.df = pd.read_csv(path)
            self.prepare_data(month, day)
            return True
        except FileNotFoundError:
            return False

    def prepare_data(self, month:str, day:str):
        """
        This function allows the table to be prepared before statistical calculations are performed

        Args:
            month (str): The month for which data needs to be filtred.
            day (str): The day of the week for which data needs to filtred.
        """
        # convert the Start Time column to datetime
        self.df['Start Time'] = pd.to_datetime(self.df['Start Time'])
        # extract month from Start Time to create new columns
        self.df['month'] = pd.to_datetime(self.df['Start Time']).dt.month
        # extract hour from Start Time to create new columns
        self.df['hour'] = pd.to_datetime(self.df['Start Time']).dt.hour
        # extract day of week from Start Time to create new columns
        self.df['day_of_week'] = pd.to_datetime(self.df['Start Time']).dt.day_name()
        # Combining Start and End Station to create new columns
        self.df['combination_sation'] = self.df['Start Station'] + " to " + self.df['End Station']

        # filter by month if applicable
        if month != 'all':
            # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month)+1
            # filter by month to create the new dataframe
            self.df = self.df[self.df['month'] == month]

        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            self.df = self.df[self.df['day_of_week'] == day.title()]

    def get_data(self):
        """
        Get data from loarded CSV file. This function returns the data stored, 
        which is expected to have been previously loaded from a CSV file using 
        the load_data function. If load data is not set, an empty string is returned.

        Returns:
            DataFrame: A content from csv file.
        """
        return self.df
