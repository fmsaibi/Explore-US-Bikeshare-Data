from app.model.data_loader import DataLoader
from app.view.bikeshare_view import BikeshareView
from app.calculation.statistics_calculation import StatisticsCalculation
from app.constants import CommonConstants, Boolean, Period


class BackshareController:
    """
    Module
    """
    def __init__(self):
        self.model              =   DataLoader()
        self.view               =   BikeshareView()
        self.statistics         =   StatisticsCalculation()
        self.city               =   CommonConstants.NULL
        self.duration           =   CommonConstants.NULL
        self.month              =   CommonConstants.ALL
        self.day                =   CommonConstants.ALL
        self.df                 =   CommonConstants.NULL
        self.data_count         =   0

    def run_app(self):
        while True:
            # Display Welcome Message
            self.display_welcome_message()
            # Display City Menu
            self.city_menu()
            # Display Period Menu
            self.period_menu()
            # Display Month Menu
            self.month_menu()
            # Display Day Menu
            self.day_menu()
            # Loading Data
            self.load_data()
            # Displays statistics on the most frequent times of travel
            self.display_time_travel_statistics()
            # Displays statistics on the most popular stations and trip
            self.display_station_statistics()
            # Displays statistics on the total and average trip duration
            self.display_duration_statistics()
            # Displays statistics on bikeshare users
            self.display_user_stats_statistics()
            # Display statistics trip data 
            self.display_individual_trip_statistics()
            # Restating Bikeshare app
            if self.view.show_reset_menu() == Boolean.YES.value:
                self.reset_data()
            else:
                break

    def display_welcome_message(self):
        self.view.show_welcome_message()

    def city_menu(self):
        if not self.city:
            self.city = self.view.show_city_menu()
    
    def period_menu(self):
        if not self.duration:
            self.duration =self.view.show_period_menu()
    
    def month_menu(self):
        if self.duration in [Period.MONTH.value, Period.BOTH.value]:
            self.month = self.view.show_month_menu()

    def day_menu(self):
        if self.duration in [Period.DAY.value, Period.BOTH.value]:
            self.day = self.view.show_day_menu()

    def load_data(self):
        if self.city:
            if self.model.load_data(self.city):
                self.model.prepare_data(self.month, self.day)
                self.df = self.model.get_data()
            else:
                self.view.show_csv_file_not_found()
    
    def display_time_travel_statistics(self):
        # Displays statistics on the most frequent times of travel
        if self.df.bool:
            self.view.display_time_travel_message()
            time = self.statistics.time_stats(self.df, self.month, self.day)
            self.view.display_time_travel_data(time)

    def display_station_statistics(self):
        if self.df.bool:
            self.view.display_station_message()
            station = self.statistics.station_stats(self.df)
            self.view.display_station_data(station)

    def display_duration_statistics(self):
        if self.df.bool:
            self.view.display_duration_message()
            duration = self.statistics.trip_duration_stats(self.df)
            self.view.display_duration_data(duration)
    
    def display_user_stats_statistics(self):
        if self.df.bool:
            self.view.display_user_stats_message()
            user = self.statistics.user_stats(self.df)
            self.view.display_user_stats_data(user)

    def display_individual_trip_statistics(self):
        if self.df.bool:
            individual_trip = Boolean.YES.value
            while individual_trip == Boolean.YES.value:
                # Display trip_data Menu
                individual_trip = self.view.show_individual_trip_data_menu()
                if individual_trip in [Boolean.YES.value, CommonConstants.NULL]:
                    # Display statistics on trip_data Menu
                    trip_data = self.statistics.individual_trip_data(self.df, self.data_count)
                    self.view.display_individual_trip_data(trip_data)
                    # Incremneting data count
                    self.data_count += 5

    def reset_data(self):
        self.city               =   CommonConstants.NULL
        self.duration           =   CommonConstants.NULL
        self.month              =   CommonConstants.ALL
        self.day                =   CommonConstants.ALL
        self.df                 =   CommonConstants.NULL
        self.data_count         =   0
