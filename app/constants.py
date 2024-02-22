"""
list of Constants Variable
"""
# Others
NONE            =   'none'
ALL             =   'all'
BOTH            =   'both'
DAY             =   'day'
YES             =   'yes'
NO              =   'no'
LINE_SPACE      =   "\n" + ("-"*40) + "\n"
SEPARATOR       =   "    :   "
EMPTY_LIST      =   ['','']
NULL            =   ""

# Constants Data Table Header
START_TIME      =   'Start Time'
END_TIME        =   'End Time'
MONTH           =   'Month'
HOUR            =   'Hours'
DAY_OF_WEEK     =   'Day_of_week'
START_STATION   =   'Start Station'
END_STATION     =   'End Station'
COMBINE_STATION =   'Combine Station'
GENDER          =   'Gender'
TRIP_DURATION   =   'Trip Duration'
USER_TYPE       =   'User Type'
BIRTH_YEAR      =   'Birth Year'

# Constants List
CITY_LIST                   =   ['chicago', 'new york city', 'washington']
PERIOD_LIST                 =   [MONTH, DAY, BOTH, NONE]
MONTH_LIST                  =   ['january', 'february', 'march', 'april', 'may', 'june']
DAY_LIST                    =   ['monday', 'tuesday', 'wednesday', 'thursday','friday',\
                                'saturday', 'sunday']
BOOLEAN_LIST                =   [YES, NO]

# Constants Message
WELCOME_MESSAGE             =   '\nHello! Let\'s explore some US bikeshare data!\n'
TIME_TRAVEL_MESSAGE         =   '\nCalculating The Most Frequent Times of Travel...\n'
POPULAR_STATIONS_MESSAGE    =   '\nCalculating The Most Popular Stations and Trip...\n'
DURATION_MESSAGE            =   '\nCalculating Trip Duration...\n'
USER_STATS_MESSAGE          =   '\nCalculating User Stats...\n'
INPUT_MESSAGE               =   "\nEnter Here: "

# Question
WHICH_CITY_QUESTION             =   'Which city you like to see the data for?'
HOW_TO_FILTER_QUESTION          =   'How would you like to filter the data?'
WHICH_MONTH_QUESTION            =   'Which Month would you like to filter the data?'
WHICH_DAY_QUESTION              =   'Which day of the week you like to filter the data?'
RESTART_QUESTION                =   'Would you like to restart?'
INDIVIDUAL_TRIP_DATA_QUESTION   =   'Would you like to view 5 rows of individual trip data?'

# Constants Error Messages
INVALID_INPUT_MESSAGE       =    '\nInvalid, Please enter valid Input'
NO_CSV_FILE_MESSAGE         =    '\nNo csv file found\nThis app will be terminated\n'

# Constants Display Messages
DISPLAY_SECONDS_TOOK                    =   'This took (seconds)'
DISPLAY_MOST_POPULAR_DAY                =   'Most popular day of the week'
DISPLAY_MOST_POPULAR_MONTH              =   'Most Popular Month'
DISPLAY_MOST_POPULAR_HOUR               =   'Most popular hour of the Month'
DISPLAY_MOST_COMMONLY_START_STATION     =   'Most commonly used start station'
DISPLAY_MOST_COMMONLY_END_STATION       =   'Most commonly used end station'
DISPLAY_MOST_FREQUENT_COMBINATION       =   'Most frequent combination'
DISPLAY_TOTAL_TRAVEL_TIME               =   'Total travel time (Hours)'
DISPLAY_AVERAGE_TRAVEL_TIME             =   'The average(mean) travel time (Hours)'
DISPLAY_TOTAL_COUNTS_OF	                =	'Total counts of '
DISPLAY_TOTAL_COUNTS_OF_ALL_USER_TYPES	=	'Total counts of all user types'
DISPLAY_TOTAL_COUNTS_OF_ALL_GENDER	    =	'Total counts of all gender'
DISPLAY_THE_OLDEST_YEAR_OF_BIRTH	    =	'The oldest year of birth'
DISPLAY_MOST_RECENT_YEAR_OF_BIRTH	    =	'Most recent year of birth'
DISPLAY_MOST_COMMAND_YEAR_OF_BIRTH	    =	'Most command year of birth'
