import pandas as pd
from app.view.menu import Menu
from app.constants import DisplayMessages, Question, City, \
    Period, Month, Boolean, Day, ErrorMessages, CommonConstants

class BikeshareView:
    """
    (module) BikeshareView
    """
    def __init__(self):
        self.menu = Menu()

    def show_welcome_message(self):
        """
            Display Welcome message at the start of the app

            Display:
                Hello! Let's explore some US bikeshare data!
        """
        print(DisplayMessages.WELCOME)

    def show_city_menu(self) -> str:
        """
        Display the menu of the city the user wants to filter the data.

        Input:
            String: Provide a numerical or descriptive input based on 
            the information presented in the specified city list menu.

        Returns:
            String: Name of the city selected
        
        Raise:
            Invalid Mesaage: If the input is invalid or not in the list provided

        Exmple:
            Method 1 (Numeric value): 
                Enter Here: 1
                Enter Here: 3
            Method 2 (Descriptive value): 
                Enter Here: Chicago
                Enter Here: washington
        """
        city_list = [city.value for city in City]
        return self.menu.get_menu(Question.WHICH_CITY,city_list)

    def show_period_menu(self) -> str:
        """
        Display the menu of the period the user wants to filter the data.

        Input:
            String: Provide a numerical or descriptive input based on 
            the information presented in the specified period list menu.

        Returns:
            String: Name of the period selected

        Raise:
            Invalid Mesaage: If the input is invalid or not in the list provided

        Exmple:
            Method 1 (Numeric value): 
                Enter Here: 1
                Enter Here: 2
            Method 2 (Descriptive value): 
                Enter Here: month
                Enter Here: day
        """
        period_list = [period.value for period in Period]
        return self.menu.get_menu(Question.HOW_TO_FILTER, period_list)

    def show_month_menu(self) -> str:
        """
        Display the menu of the month the user wants to filter the data.

        Input:
            String: Provide a numerical or descriptive input based on 
            the information presented in the specified month list menu.

        Returns:
            String: Name of the month selected
        
        Raise:
            Invalid Mesaage: If the input is invalid or not in the list provided
        
        Exmple:
            Method 1 (Numeric value): 
                Enter Here: 1
                Enter Here: 2
            Method 2 (Descriptive value): 
                Enter Here: month
                Enter Here: day
        """
        month_list = [month.value for month in Month]
        return self.menu.get_menu(Question.WHICH_MONTH, month_list)

    def show_individual_trip_data_menu(self) -> str:
        """
        Display the menu of the individual trip for the user .

        Input:
            String: Provide a numerical or descriptive input based on 
            the information presented in the specified individual trip list menu.

        Returns:
            String: Yes if the user want display individual trip, else no
        
        Raise:
            Invalid Mesaage: If the input is invalid or not in the list provided
        
        Exmple:
            Method 1 (Numeric value): 
                Enter Here: 1
                Enter Here: 2
            Method 2 (Descriptive value): 
                Enter Here: Yes
                Enter Here: No
        """
        boolean_list = [boolean.value for boolean in Boolean]
        boolean_list.append("")
        return self.menu.get_menu(Question.INDIVIDUAL_TRIP_DATA, boolean_list)

    def show_day_menu(self) -> str:
        """
        Display the menu of the day the user wants to filter the data.

        Input:
            String: Provide a numerical or descriptive input based on 
            the information presented in the specified day list menu.

        Returns:
            String: Name of the day selected
        
        Raise:
            Invalid Mesaage: If the input is invalid or not in the list provided

        Exmple:
            Method 1 (Using Numeric value): 
                Enter Here: 1
                Enter Here: 2
            Method 2 (Using Descriptive value): 
                Enter Here: monday
                Enter Here: thursday
        """
        day_list = [day.value for day in Day]
        return self.menu.get_menu(Question.HOW_TO_FILTER, day_list)

    def show_reset_menu(self):
        """
        Display the menu of reset

        Input:
            String: Provide a numerical or descriptive input based on 
            the information presented in the specified reset menu.

        Returns:
            String: Yes or No
        
        Raise:
            Invalid Mesaage: If the input is invalid or not in the list provided
        """
        boolean_list = [boolean.value for boolean in Boolean]
        return self.menu.get_menu(Question.LIKE_TO_RESTART,boolean_list)

    def show_csv_file_not_found(self):
        """
        Thie fuction will print message 'No CSV file not found'
        """
        print(ErrorMessages.NO_CSV_FILE)

    def display_time_travel_message(self):
        """
        This fuction will display message "Calculating The Most Frequent Times of Travel"
        """
        print(DisplayMessages.MOST_TIME_TRAVEL)

    def display_time_travel_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical of The Most Frequent Times of Travel

        Args:
            data (pd.DataFrame): Table from previously used function time_stats
        """
        print(f'{data}\n{CommonConstants.LINE}')

    def display_station_message(self):
        """
        This fuction will display message "Calculating The Most Popular Stations and Trip"
        """
        print(DisplayMessages.MOST_POPULAR_STATIONS)

    def display_station_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical of The Most Frequent Times of Travel

        Args:
            data (pd.DataFrame): Table from previously used function station_stats
        """
        print(f'{data}\n{CommonConstants.LINE}')

    def display_duration_message(self):
        """
        This fuction will display message "Calculating Trip Duration"
        """
        print(DisplayMessages.TRIP_DURATION)

    def display_duration_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical on the total and average trip duration

        Args:
            data (pd.DataFrame): Table from previously used function trip_duration_stats
        """
        print(f'{data}\n{CommonConstants.LINE}')

    def display_user_stats_message(self):
        """
        This fuction will display message "Calculating User Stats"
        """
        print(DisplayMessages.USER_STATS)

    def display_user_stats_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical on the total and average trip duration

        Args:
            data (pd.DataFrame): Table from previously used function trip_duration_stats
        """
        print(f'{data}\n{CommonConstants.LINE}')

    def display_individual_trip_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical of 5 individual \
        trip_data each time user request for data

        Args:
            data (pd.DataFrame): for the csv file loaded
        """
        print(f'{data}\n{CommonConstants.LINE}')
