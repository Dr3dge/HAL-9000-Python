from config import *
from datetime import date

credentials = {}
d = date.today()
ds = str(d)
filename = 'user_login_codes.txt'



def is_file(file):
    if not path.isfile(file):
        with open(file, 'w') as f:
            f.write('')
            return False


def creds(file):
    with open(file, 'r') as f:
        for line in f:
            global credentials
            user, pwd = line.strip().split(':')
            credentials[user] = pwd


def make_login(username, password):
    if username in credentials:
        print('User already exists.')
    else:
        with open(filename, 'a') as f:
            f.write(username)
            f.write(":")
            f.write(password)
            f.write('\n')
            print('User created')
        creds(filename)

def login(username, password):
    with open(filename, 'r') as f:
        if username in credentials:
            creds(filename)
            if credentials[username] == password:
                print('Logged in.')
            else:
                print('Not logged in')
        else:
            print('No such user')

while is_file(filename) is False:
    is_file(filename)
creds(filename)