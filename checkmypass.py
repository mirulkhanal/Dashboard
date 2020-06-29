import requests
import hashlib
import sys

try:
    if len(sys.argv) > 2:
        print('Invalid request, The program will only check the first password \n')
    password = sys.argv[1]
except IndexError:
    password = input('Enter your password:\t')


def api_check(hash_header):
    url = 'https://api.pwnedpasswords.com/range/' + hash_header
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Expected 200 got {res.status_code}')
    return res


def get_pass_hash(api_response, hash_rest):
    hash_header = (header.split(':')
                   for header in api_response.text.splitlines())
    for head, count in hash_header:
        if head == hash_rest:
            return count
        return 0


def password_check(password_text):
    hash_all = hashlib.sha1(password_text.encode(
        'utf-8')).hexdigest().upper()
    hash_first_five, hash_rest = hash_all[:5], hash_all[5:]
    api_response = api_check(hash_first_five)
    return get_pass_hash(api_response, hash_rest)


def response_parser(password):
    apple = password_check(password)
    print(apple)


response_parser(password)
