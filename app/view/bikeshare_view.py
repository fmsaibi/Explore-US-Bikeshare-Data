"""Module providing a fuction to preapre One-dimensional ndarray with axis labels"""
import pandas as pd

class BikeshareView:
    """
    (module) BikeshareView
    """

    def show_welcome_message(self):
        """
            Display Welcome message at the start of the app
        """
        print('\nHello! Let\'s explore some US bikeshare data!\n')

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
        city_list = [
            'chicago', 
            'new york city', 
            'washington'
        ]
        question = "Which city you like to see the data for?"
        selected = self.get_menu(question, city_list)
        return selected

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
        period_list = [
            'month', 
            'day', 
            'both',
            'none'
        ]
        question = "How would you like to filter the data?"
        selected = self.get_menu(question, period_list)

        return "all" if selected == "none" else selected

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
        month_list = [
            'january', 
            'february', 
            'march',
            'april',
            'may',
            'june'
        ]
        question = "Which Month would you like to filter the data?"
        selected_month = self.get_menu(question, month_list)
        return selected_month

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
        day_list = ['monday',
                    'tuesday',
                    'wednesday',
                    'thursday',
                    'friday',
                    'saturday',
                    'sunday'
                    ]

        question = "Which day of the week you like to filter the data?"
        selected = self.get_menu(question, day_list)
        return selected

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
        boolean_list = [
            'yes',
            'no' 
        ]

        question = 'Would you like to restart?'
        selected = self.get_menu(question,boolean_list)
        return selected


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
        invalid_input_message = "Invalid, Please enter valid Input"
        print(question)
        menu_table = pd.Series(data=items, index=range(1, len(items)+1))

        for index, value in menu_table.items():
            print(f'{index}. {value.title()}')

        while not selected:
            user_input = input("Enter Here: ")
            try:
                if (user_input.lower() in menu_table.values) or \
                    (int(user_input) in menu_table.index):
                    if user_input.isnumeric():
                        selected = menu_table[int(user_input)]
                    else:
                        selected = user_input.lower()
                else:
                    print(invalid_input_message)
            except ValueError:
                print(invalid_input_message)

        print("\n" + ("-"*40) + "\n")

        return selected

    def show_csv_file_not_found(self):
        """
        Thie fuction will print message 'No CSV file not found' 
        """
        print("No csv file found\nThis app will be terminated\n")

    def display_time_travel_message(self):
        """
        This fuction will display message "Calculating The Most Frequent Times of Travel"
        """
        print('\nCalculating The Most Frequent Times of Travel...\n')

    def display_time_travel_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical of The Most Frequent Times of Travel

        Args:
            data (pd.DataFrame): Table from previously used function time_stats
        """
        print(data)
        print("\n" + '-'*40)

    def display_station_message(self):
        """
        This fuction will display message "Calculating The Most Popular Stations and Trip"
        """
        print('\nCalculating The Most Popular Stations and Trip...\n')

    def display_station_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical of The Most Frequent Times of Travel

        Args:
            data (pd.DataFrame): Table from previously used function station_stats
        """
        print(data)
        print("\n" + '-'*40)

    def display_duration_message(self):
        """
        This fuction will display message "Calculating Trip Duration"
        """
        print('\nCalculating Trip Duration...\n')

    def display_duration_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical on the total and average trip duration

        Args:
            data (pd.DataFrame): Table from previously used function trip_duration_stats
        """
        print(data)
        print("\n" + '-'*40)

    def display_user_stats_message(self):
        """
        This fuction will display message "Calculating Trip Duration"
        """
        print('\nCalculating User Stats...\n')

    def display_user_stats_data(self, data:pd.DataFrame):
        """
        This fuction will dsiplay the statstical on the total and average trip duration

        Args:
            data (pd.DataFrame): Table from previously used function trip_duration_stats
        """
        print(data)
        print("\n" + '-'*40)
