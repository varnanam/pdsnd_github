import time
import pandas as pd
import numpy as np
# Bikeshare App
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=str(input('Enter the city.\n')).lower()
    while city not in CITY_DATA:
        city=str(input('Sorry we were not able to process the name of the city to analyze data, Please input either chicago, new york city or washington.\n')).lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month=str(input("Enter full name of anyone of the first 6 months (eg: january, february, ... , june) or type 'all'. \n ")).lower()
    months=['january', 'february', 'march', 'april', 'may', 'june','all']
    while month not in months:
        month=str(input("Invalid input.Please enter only the First 6 months or type 'all'. \n")).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=str(input("Enter the day  in the week, or type 'all' \n")).lower()
    days=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday' ,'all']
    while day not in days:
        day=str(input("Please Enter a valid input.(Eg: sunday,monday,...saturday or type 'all') .\n")).lower()


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
    df = pd.read_csv(CITY_DATA[city])
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':  #filter by month
        months=['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month=months.index(month)+1
        df=df[df['month']==month]

    if day != 'all': #filter by day
        df = df[df['day_of_week'] == day.title()]
   

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print(f'The most common month is:{common_month}')

    # TO DO: display the most common day of week
    print('The most common day is: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." %  round((time.time() - start_time),2))
    
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station is: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination= df['Start Station'] + ' to ' +df['End Station'] 
    most_frequent_combination=most_frequent_combination.mode()[0]
    print(f'Most frequent combination of start station and end station trip is:{most_frequent_combination}')

    print("\nThis took %s seconds." %  round((time.time() - start_time),2))
    
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print(f'Total travel time is: {total_time}sec')

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print(f'Mean travel time is: {mean_time}sec')

    print("\nThis took %s seconds." %  round((time.time() - start_time),2))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"The types of users are shown below:\n{user_type}")
    
    
    # TO DO: Display counts of gender
    # using try clause we can display the numebr of users by Gender for a perticular city in the dataset
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")    
        
    
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"earliest, most recent, and most common year of birth are : {earliest} , {recent} , {common_year}")
    except:
        print("There are no birth year details in this file.")  
    
        
    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def view_raw_data(df):
    print(df.head())
    count=0
    while True:
          raw_data=input('Would you like to view next five row of raw data? Enter yes or no.\n')
          if (raw_data.lower()!= 'yes' and  raw_data.lower()!= 'no'):
              raw_data= input ("Invalid input, Please Enter 'YES' or 'NO' \n")
          if raw_data.lower() != 'yes':
              return
          count = count + 5
          print(df.iloc[count:count+5])
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            raw_data = input('Would you like to view first five row of raw data? Enter yes or no.\n')
            if (raw_data.lower()!= 'yes' and  raw_data.lower()!= 'no'):
                raw_data= input ("Invalid input, Please Enter 'YES' or 'NO' \n")
                
            if raw_data.lower() != 'yes':
                break
            view_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if (restart.lower()!= 'yes' and  restart.lower()!= 'no'):
                restart= input ("Invalid input, Please Enter 'YES' or 'NO' \n")
                
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
    main()
