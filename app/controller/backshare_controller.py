from app.model.data_loader import DataLoader
from app.view.bikeshare_view import BikeshareView
from app.calculation.statistics_calculation import StatisticsCalculation


class BackshareController:
    """
    Module
    """
    def __init__(self):
        self.model      = DataLoader()
        self.view       = BikeshareView()
        self.statistics = StatisticsCalculation()
        self.city       = ""
        self.duration   = "none"
        self.month      = "all"
        self.day        = "all"

    def run_app(self):
        """_summary_
            Run user input menu list
        """
        # Display Welcome Message
        self.view.show_welcome_message()

        while True:
            # # Display City Menu
            city = self.view.show_city_menu()
            self.city = city if city else ""
            # Display Period Menu
            period = self.view.show_period_menu()
            self.duration = period if period else "none"
            # Display Month Menu
            if self.duration in ["month","both"]:
                month = self.view.show_month_menu()
                self.month = month if month else "all"
            # Display Day Menu
            if self.duration in ["day","both"]:
                day = self.view.show_day_menu()
                self.day = day if day else "all"
            # Loading Data
            if self.city:
                if self.model.load_data(self.city, self.month, self.day):
                    # Getting loaded data
                    df = self.model.get_data()
                    
                    # Displays statistics on the most frequent times of travel
                    self.view.display_time_travel_message()
                    time = self.statistics.time_stats(df, self.month, self.day)
                    self.view.display_time_travel_data(time)

                    # Displays statistics on the most popular stations and trip
                    self.view.display_station_message()
                    station = self.statistics.station_stats(df)
                    self.view.display_station_data(station)

                    # Displays statistics on the total and average trip duration
                    self.view.display_duration_message()
                    duration = self.statistics.trip_duration_stats(df)
                    self.view.display_duration_data(duration)

                    # Displays statistics on bikeshare users
                    self.view.display_user_stats_message()
                    user = self.statistics.user_stats(df)
                    self.view.display_user_stats_data(user)
                else:
                    self.view.show_csv_file_not_found()
                    break

            # Restating Data app
            if self.view.show_reset_menu() != 'yes':
                break
