"""Module providing a fuction to preapre One-dimensional ndarray with axis labels"""
import pandas as pd
import app.constants as cs

class BikeshareView:
    """
    (module) BikeshareView
    """

    def show_welcome_message(self):
        """
            Display Welcome message at the start of the app
        """
        print(cs.WELCOME_MESSAGE)

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
        return self.get_menu(cs.WHICH_CITY_QUESTION, cs.CITY_LIST)

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
        return self.get_menu(cs.HOW_TO_FILTER_QUESTION, cs.PERIOD_LIST)

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
        return self.get_menu(cs.WHICH_MONTH_QUESTION, cs.MONTH_LIST)

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
        return self.get_menu(cs.INDIVIDUAL_TRIP_DATA_QUESTION, cs.BOOLEAN_LIST)

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
        return self.get_menu(cs.HOW_TO_FILTER_QUESTION, cs.DAY_LIST)

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
        return self.get_menu(cs.RESTART_QUESTION,cs.BOOLEAN_LIST)

    def get_menu(self, question:str, items:list) -> str:
        """
        Take user input from the terminal or command prompt, based on the display period list

        Args:
            User Input: Numeric value or String associated with the period table

        Returns:
            String: The Name of the Period selected
        
        Raise:
            Invalid Mesaage: If the input is invalid or not in the list provided
        """
        selected = str()
        print(question)
        menu_table = pd.Series(data=items, index=range(1, len(items)+1))

        for index, value in menu_table.items():
            print(f'{index}. {value.title()}')

        while not selected:
            user_input = input(cs.INPUT_MESSAGE)
            try:
                if (user_input.lower() in menu_table.values) or \
                    (int(user_input) in menu_table.index):
                    if user_input.isnumeric():
                        selected = menu_table[int(user_input)]
                    else:
                        selected = user_input.lower()
                else:
                    print(cs.INVALID_INPUT_MESSAGE)
            except ValueError:
                print(cs.INVALID_INPUT_MESSAGE)

        print(cs.LINE_SPACE)

        return selected

    def show_csv_file_not_found(self):
        """
        Thie fuction will print message 'No CSV file not found' 
        """
        print(cs.NO_CSV_FILE_MESSAGE)

    def display_time_travel_message(self):
        """
        This fuction will display message "Calculating The Most Frequent Times of Travel"
        """
        print(cs.TIME_TRAVEL_MESSAGE)

    def display_time_travel_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical of The Most Frequent Times of Travel

        Args:
            data (pd.DataFrame): Table from previously used function time_stats
        """
        print(f'{data}\n{cs.LINE_SPACE}')

    def display_station_message(self):
        """
        This fuction will display message "Calculating The Most Popular Stations and Trip"
        """
        print(cs.POPULAR_STATIONS_MESSAGE)

    def display_station_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical of The Most Frequent Times of Travel

        Args:
            data (pd.DataFrame): Table from previously used function station_stats
        """
        print(f'{data}\n{cs.LINE_SPACE}')

    def display_duration_message(self):
        """
        This fuction will display message "Calculating Trip Duration"
        """
        print(cs.DURATION_MESSAGE)

    def display_duration_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical on the total and average trip duration

        Args:
            data (pd.DataFrame): Table from previously used function trip_duration_stats
        """
        print(f'{data}\n{cs.LINE_SPACE}')

    def display_user_stats_message(self):
        """
        This fuction will display message "Calculating Trip Duration"
        """
        print(cs.USER_STATS_MESSAGE)

    def display_user_stats_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical on the total and average trip duration

        Args:
            data (pd.DataFrame): Table from previously used function trip_duration_stats
        """
        print(f'{data}\n{cs.LINE_SPACE}')

    def display_individual_trip_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical of 5 individual \
        trip_data each time user request for data

        Args:
            data (pd.DataFrame): for the csv file loaded
        """
        print(f'{data}\n{cs.LINE_SPACE}')
