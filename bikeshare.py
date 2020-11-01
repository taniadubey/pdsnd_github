#libraries used in this code:
import time
import pandas as pd
import numpy as np

# creating a dictionary for csv files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks user to specify a city to analyze

    Returns:
        (str) city - name of city to analyze
    """
    #while loop to make sure a valid city is entered
    while True:
        city = input('Choose a city [Chicago, New York City, Washington]: ').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Invalid city, please try again.")
        else:
            break
    
    return city

def get_filter_choice():
    """
    Asks user for their filter preference

    Returns:
        (str) filter_choice: month, day, both, or none
    """    
    while True:
        filter_choice = input('How would you like to filter your data? [Month, Day, Both, None]: ').lower()
        if filter_choice not in ('month', 'day', 'both', 'none'):
            print('Not a valid choice, please try again.')
        else:
            break
    
    return filter_choice

def get_month():
    """
    Asks user to specify a month to analyze

    Returns:
        (str) month - name of the month to filter by
    """
    while True:
        month = input('Choose a month [January, February, March, April, May, June]: ').lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june'):
            print('Invalid month, please try again.')
        else:
            break
    
    return month

def get_day():
    """
    Asks user to specify a day of week to analyze

    Returns:
        (str) day - name of the month to filter by
    """
    while True:
        day = input('Choose a day [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]: ' ).lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            print('Invalid day, please try again.')
        else:
            break
    
    return day

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Use get_city() function to select a city to analyze
    city = get_city()

    # Get user input for their choice of filter by month, day, both or none
    filter_choice = get_filter_choice()
    
    # conditional statement for filter choice:
    # use get_month() function if month filter is selected and assign day to all
    if filter_choice == 'month':
        month = get_month()
        day = 'all'
    # use get_day() function if day filter is selected and assign month to all
    elif filter_choice == 'day':
        month = 'all'
        day = get_day()
    # use get_month() and get_day() function if both filter is selected
    elif filter_choice == 'both':
        month = get_month()
        day = get_day()
    # assign month and day to all if no filter is selected
    elif filter_choice == 'none':
        print('No time filter is selected\n')
        month = 'all'
        day = 'all'
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    # find the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Start Month:', popular_month)

    # TO DO: display the most common day of week
    # extract day from the Start Time column to create an day of week column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # find the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Start Hour:', common_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combo_station = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    print('Most Freequent Combination of Start and End Station:', common_combo_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = np.sum(df['Trip Duration'])
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('Counts of User Types: \n', user_count, '\n')

    # TO DO: Display counts of gender
    if 'Gender' in df:
            gender_count = df['Gender'].value_counts()
            print('Counts of Gender: \n', gender_count, '\n')
    else:
        print('No Gender information')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        min_birth_year = np.min(df['Birth Year'])
        print('Earliest year of birth: ', min_birth_year)

        max_birth_year = np.max(df['Birth Year'])
        print('Most recent year of birth: ', max_birth_year)

        common_birth_year = df['Birth Year'].mode()[0]
        print('Most common year of birth: ', common_birth_year)
        
    else:
        print('No Birth Year information')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Asks user is they want to see raw data

    Returns:
        If Yes: 5 lines of raw data
        If No: None
    """ 
    while True:
        raw_data_choice = input('\nWould you like to see 5 lines of raw data? [Yes, No]:\n').lower()
        if raw_data_choice.lower() == 'no':
            break
        elif raw_data_choice.lower() == 'yes':
            print(df.sample(n=5))
        else:
            print('Not a valid choice, please try again.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
