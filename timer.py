import time
import os


def create_timer(time_in_seconds):
    begin_time = time.time()
    while True:
        now = time.time()
        if now > begin_time and int(now-begin_time) < time_in_seconds:
            os.system('cls')
            print(
                f'Timer for: {int(((time_in_seconds-(now-begin_time))/3600))}:{int(((time_in_seconds-(now-begin_time))%3600)/60)}:{int(time_in_seconds-(now-begin_time))%60}')
        elif int(now-begin_time) == time_in_seconds:
            os.system('cls')
            print('Timer completed')
            break


def get_hours():
    while True:
        hour = input('Enter Hours: ')
        if bool(hour) == False:
            hour = 0
            return hour
        else:
            try:
                hour = int(hour)
            except ValueError:
                print('Invalid entry, Please enter number')
            else:
                hour = int(hour)
                return hour


def get_minutes():
    while True:
        minute = input('Enter Minutes: ')
        if bool(minute) == False:
            minute = 0
            return minute
        else:
            try:
                minute = int(minute)
            except ValueError:
                print('Invalid entry, Please enter number')
            else:
                minute = int(minute)
                return minute


def get_seconds():
    while True:
        second = input('Enter second: ')
        if bool(second) == False:
            second = 0
            return second
        else:
            try:
                second = int(second)
            except ValueError:
                print('Invalid entry, Please enter number')
            else:
                second = int(second)
                return second


time_in_seconds = (get_hours()*60*60) + (get_minutes()*60) + get_seconds()
create_timer(time_in_seconds)
