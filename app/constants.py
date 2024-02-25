"""
list of Constants Variable
"""
from enum import Enum

# CommonConstants
class CommonConstants:
    """
    A collection of commonly used constants in the program.
    """
    NONE            =   'none'
    ALL             =   'all'
    LINE            =   "\n" + ("-"*40) + "\n"
    SEPARATOR       =   "    :   "
    EMPTY_LIST      =   ['','']
    NULL            =   ""

# Constants Data Table Header
class TableHeader:
    
    """
    A collection of City used for displaying information in the program.

    Attributes:
        CHICAGO (str)        :   chicago
        NEW_YORK_CITY (str)  :   new york city
        WASHINGTON (str)     :   washington
    """

    # Orignal list
    START_TIME      =   'Start Time'
    END_TIME        =   'End Time'
    START_STATION   =   'Start Station'
    END_STATION     =   'End Station'
    COMBINE_STATION =   'Combine Station'
    GENDER          =   'Gender'
    TRIP_DURATION   =   'Trip Duration'
    USER_TYPE       =   'User Type'
    BIRTH_YEAR      =   'Birth Year'
    # New list
    COMBINE_STATION =   'Combine Station'
    MONTH           =   'Month'
    HOUR            =   'Hours'
    DAY_OF_WEEK     =   'Day of week'

# City List
class City(Enum):
    """
    A collection of City used for displaying information in the program.

    Attributes:
        CHICAGO (str)        :   chicago
        NEW_YORK_CITY (str)  :   new york city
        WASHINGTON (str)     :   washington
    """
    CHICAGO         = 'chicago'
    NEW_YORK_CITY   = 'new york city'
    WASHINGTON      = 'washington'

# Period List
class Period(Enum):
    """
    A collection of Period used for displaying information in the program.

    Attributes:
        MONTH (str) : month
        DAY (str)   : day
        BOTH (str)  : both
        NONE (str)  : none
    """
    MONTH   = 'month'
    DAY     = 'day'
    BOTH    = 'both'
    NONE    = 'none'

# Month List
class Month(Enum):
    """
    A collection of Day of the week used for displaying information in the program.

    Attributes:
        JANUARY (str)   : Display january
        FEBRUARY (str)  : Display february
        MARCH (str)     : Display march
        APRIL (str)     : Display april
        MAY (str)       : Display may
        JUNE (str)      : Display june
    """
    JANUARY     = 'january'
    FEBRUARY    = 'february'
    MARCH       = 'march'
    APRIL       = 'april'
    MAY         = 'may'
    JUNE        = 'june'

# Day List
class Day(Enum):
    """
    A collection of Day of the week used for displaying information in the program.

    Attributes:
        MONDAY  (str)   : Display monday
        TUESDAY (str)   : Display tuesday
        WEDNESDAY(str)  : Display wednesday
        THURSDAY (str)  : Display thursday
        FRIDAY  (str)   : Display friday
        SATURDAY (str)  : Display saturday
        SUNDAY (str)    : Display sunday
    """
    MONDAY      = 'monday'
    TUESDAY     = 'tuesday'
    WEDNESDAY   = 'wednesday'
    THURSDAY    = 'thursday'
    FRIDAY      = 'friday'
    SATURDAY    = 'saturday'
    SUNDAY      = 'sunday'

# Boolean List
class Boolean(Enum):
    """
    A collection of Boolean used for displaying information in the program.

    Attributes:
        YES (str)   : Display Yes
        No (str)    : Display No
    """
    YES = 'yes'
    NO  = 'no'

# Constants Question
class Question:
    """
    A collection of questions used for displaying information in the program.

    Attributes:
        WHICH_CITY (str): The question asking the user which city they would like to see data for.
        HOW_TO_FILTER (str): The question asking the user how they would like to filter the data.
        WHICH_MONTH (str): The question asking the user which month they would like to filter \
        the data by.
        WHICH_DAY (str): The question asking the user which day of the week they would like to \
        filter the data by.
        LIKE_TO_RESTART (str): The question asking the user if they would like to restart the \
        program.
        INDIVIDUAL_TRIP_DATA (str): The question asking the user if they would like to view 5 \
        rows of individual trip data.
    """
    WHICH_CITY              =   'Which city you like to see the data for?'
    HOW_TO_FILTER           =   'How would you like to filter the data?'
    WHICH_MONTH             =   'Which Month would you like to filter the data?'
    WHICH_DAY               =   'Which day of the week you like to filter the data?'
    LIKE_TO_RESTART         =   'Would you like to restart?'
    INDIVIDUAL_TRIP_DATA    =   'Would you like to view 5 rows of individual trip data?'

# Constants Error Messages
class ErrorMessages:
    """
    A collection of constant error messages used for displaying information in the program.
    """
    INVALID_INPUT                   =   '\nInvalid, Please enter valid Input'
    NO_CSV_FILE                     =   '\nNo csv file found'

# Constants Display Messages
class DisplayMessages:
    """
    A collection of constant messages used for displaying information in the program.
    """
    WELCOME                         =   '\nHello! Let\'s explore some US bikeshare data!\n'
    TRIP_DURATION                   =   '\nCalculating Trip Duration...\n'
    USER_STATS                      =   '\nCalculating User Stats...\n'
    INPUT_HERE                      =   "\nEnter Here: "
    SECONDS_TOOK                    =   'This took (seconds)'
    AVERAGE_TRAVEL_TIME             =   'The average(mean) travel time (Hours)'
    OLDEST_YEAR_OF_BIRTH            =   'The oldest year of birth'
    MOST_TIME_TRAVEL                =   '\nCalculating The Most Frequent Times of Travel...\n'
    MOST_POPULAR_STATIONS           =   '\nCalculating The Most Popular Stations and Trip...\n'
    MOST_POPULAR_DAY                =   'Most popular day of the week'
    MOST_POPULAR_MONTH              =   'Most Popular Month'
    MOST_POPULAR_HOUR               =   'Most popular hour of the Month'
    MOST_COMMONLY_START_STATION     =   'Most commonly used start station'
    MOST_COMMONLY_END_STATION       =   'Most commonly used end station'
    MOST_FREQUENT_COMBINATION       =   'Most frequent combination'
    MOST_RECENT_YEAR_OF_BIRTH       =   'Most recent year of birth'
    MOST_COMMAND_YEAR_OF_BIRTH      =   'Most command year of birth'
    TOTAL_TRAVEL_TIME               =   'Total travel time (Hours)'
    TOTAL_COUNTS_OF                 =   'Total counts of '
    TOTAL_COUNTS_OF_ALL_USER_TYPES  =   'Total counts of all user types'
    TOTAL_COUNTS_OF_ALL_GENDER      =   'Total counts of all gender'
