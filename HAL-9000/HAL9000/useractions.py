from os import path
from datetime import date

credentials = {}
d = date.today()
ds = str(d)
filename = 'user_login_codes.txt'
history = 'login_history.txt'
logged_in = False
current_user = ''


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
    global logged_in
    global current_user
    if logged_in == False:
        with open(history, 'a') as f:
            if username in credentials:
                creds(filename)
                if credentials[username] == password:
                    print('Logged in.')
                    f.write(username)
                    f.write("logged in")
                    f.write(ds)
                    f.write('{}\n')
                    logged_in = True
                    current_user = username
                else:
                    print('Not logged in')
            else:
                print('Invalid Credentials')
    else:
        print("Someone is Already Logged In.")


def logout(username):
    global current_user
    global logged_in
    if logged_in == True:
        if username == current_user:
            logged_in = False
            current_user = ''
        else:
            print("Not Current User.")
    else:
        print("Not Logged In.")


def del_login(username):
    with open(filename, 'w') as f:
        if username in credentials:
            creds(filename)
            del credentials[username]
        else:
            print("No such user.")


def edit_login(username,password):
    if username in credentials:
        creds(filename)
        if credentials[username] == password:
            new_password = input("What is the new password? ")
            with open(history, 'a') as f:
                if username in credentials:
                    creds(filename)
                    credentials[username] = new_password
                    f.write(username)
                    f.write("changed password from:")
                    f.write(password)
                    f.write("to:")
                    f.write(new_password)
                    f.write('{}\n')
                    
        
def do_stuff(foo,bar):
    if logged_in == True:
        print(foo,bar)
    else:
        print("Not Logged In.")


while is_file(filename) is False:
    is_file(filename)
creds(filename)

