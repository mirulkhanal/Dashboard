import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('PAPERQUOTES_TOKEN')


def quote_of_the_day():
    qod_url = os.getenv('PAPERQUOTES_QOD_URL')
    response = requests.get(qod_url, headers={
        'Authorization': 'TOKEN {}'.format(token)})
    quotes = json.loads(response.text)
    quote_text = quotes['quote']
    quote_author = quotes['author']
    return quote_text, quote_author


def get_quote_by_author():
    quote_list = []
    name = input('Author\'s name:\n>>> ')
    fname = name.split(' ')[0]
    lname = name.split(' ')[1]
    author_url = f"https://api.paperquotes.com/apiv1/quotes/?author={fname}%20{lname}"
    print(author_url)
    response = requests.get(author_url, headers={
        'Authorization': 'TOKEN {}'.format(token)})
    quotes = json.loads(response.text)['results']
    author = quotes[0]['author']
    for quote in quotes:
        quote_list.append(quote['quote'])
        # print(quote)
    return quote_list, author


def display_quote():
    print('1.\tGet Quote of the day')
    print('2.\tGet Quote from an Author\n')
    choice = input('>>>\t')
    if choice == '1':
        quote_text, quote_author = quote_of_the_day()
        print(f'{quote_text}\n\t-by {quote_author}')
    elif choice == '2':
        quote_list, author = get_quote_by_author()
        count = 0
        print(f'\nQuotes by {author}')
        try:
            while count <= len(quote_list):
                os.system('cls')
                print(f'{quote_list[count]}')
                cont = input(f'\nMore quotes by {author}(Y/N): ')
                if cont == 'y' or cont == 'Y':
                    count += 1
                elif cont == 'n' or cont == 'N':
                    print('\nExited without error')
                    break
                else:
                    os.system('cls')
                    print('\nError Input, Try Again')
        except IndexError:
            print('\nThats all of them for now')
