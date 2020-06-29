import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
import random

cred = credentials.Certificate(
    'C:\\Users\\Mirul\\Desktop\\Pypro\\relaxation\\firebase-sdk.json')
firebase_admin.initialize_app(
    cred, {'databaseURL': 'https://pyhome-28d02.firebaseio.com/'})


def gen_random_id():
    merger = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(65, 91):
        merger.append(chr(i))
    for j in range(97, 123):
        merger.append(chr(j))
    # random.shuffle(merger)
    random_list = random.sample(merger, 4)
    print(random_list)
    unique_code = ""
    for char in random_list:
        unique_code += char
    return unique_code


def add_data(data, noteID, day, month, year):
    ref = db.reference('/Reminders').child(f'{noteID}')
    ref.push(data)
    print(
        f'Success!!! added the reminder with id {noteID} for {year}-{month}-{day}')


def format_data(noteID, reminder_text, day, month, year):
    data = {
        'reminder_text': f'{reminder_text}',
        'reminder_date': {'day': f'{day}',
                          'month': f'{month}',
                          'year': f'{year}'}}
    return add_data(data, noteID, day, month, year)


def input_data():
    try:
        noteID = gen_random_id()
        reminder_text = input('Reminder text \n>>>')
        reminder_date = input(
            'Date(YYYY-MM-DD): or enter "n" for tomorrow\'s date\n>>>')
        if reminder_date == 'n':
            reminder_date = datetime.date.today() + datetime.timedelta(days=1)
            print(reminder_date)
        day, month, year = validationcheck(str(reminder_date))
        return format_data(noteID, reminder_text, day, month, year)
    except:
        print('and retry the process again....')


def validationcheck(date):
    date_list = date.split('-')
    try:
        if len(date_list[2]) == 2 and len(date_list[1]) == 2 and len(date_list[0]) == 4:
            try:
                day = int(date_list[2])
                month = int(date_list[1])
                year = int(date_list[0])
                return day, month, year
            except:
                print('Please enter numbers, not characters')
        elif len(date_list) > 3:
            print('Too many arguments, just enter date like 2024-12-31')
    except IndexError:
        print('Please enter date in the format YYYY-MM-DD')


input_data()
# gen_random_id()
