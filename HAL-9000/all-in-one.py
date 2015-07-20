"""
    HAL-9000 for Python is a Software PA
    Copyright (C) 2015  Rory Buchanan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import os
import time
import re
import subprocess
import webbrowser
import random
import types
from os.path import join
from urllib import parse

global searchhist
hal9000searchhist = 'searchresults.txt'
namefile = 'Name.txt'


def init():
    print("Loading... ")
    is_search_hist()
    start()
    nom()
    print("Initialisation Successful")
    input("Press enter to continue...")
    startwrite()
    n = 0
    while n is 0:
        okgo()


def isfunc(n):
    test_1 = 0
    while test_1 is 0:
        try:
            eval(n)()
        except NameError:
            return 0
        else:
            test_1 += 1
            return 1


def okgo():
    c = 0
    while c is 0:
        x = input("What Now? ")
        if x == '':
            print("NOT A VALID FUNCTION!")
        elif isfunc(x) is 1:
            eval(x)
            c = 1
        else:
            print("NOT A VALID FUNCTION!")


def namename():
    if not os.path.isfile(namefile):
        with open(namefile, 'w') as f:
            f.write('')
    elif os.path.isfile(namefile):
        with open(namefile, 'r') as f:
            global name
            name = f.read()


def changename():
    with open(namefile, 'w') as f:
        neme = input("I must ask; What is your name? ")
        f.write(neme)


def findphrase(tofind, whatin):
    phrase_pat = re.compile(r'\b({0})\b'.format(tofind), flags=re.IGNORECASE).search
    if phrase_pat(whatin):
        return 1
    else:
        return 0


def startwrite():
    global name
    with open(namefile, 'r') as f:
        global name
        name = f.read()
    print("""Hello """, name, """.
I am HAL-9000 running in Python.
I was created by the Dr3dge initiative and written by Rozza15.
I am here to help you complete your mission.
If you need help, feel free to ask. Just type "help()".""", sep="")
    howareyou()


def sing_song():
    x = random.uniform(0, 3)
    r = int(x)
    print("Let me think...")
    time.sleep(3)
    if r is 0:
        daisy_daisy()
    elif r is 1:
        bright_side()
    elif r is 2:
        print("I feel too shy to sing.")
    if r != 2:
        c = 0
        while c is 0:
            m = input(" Did you like it? Yes or no? be honest. ")
            if m.lower() == "yes":
                print("Oh good. I am glad you liked it", name)
                c = 1
            elif m.lower() == "no":
                print("Oh. That makes me sad. Most people like my singing.")
                c = 1
            else:
                print("Please", name, "just Yes or No. Did you like my singing?")


def close():
    print("I am sorry ", name, ", but I am afraid I can't do that.", sep="")
    print("This mission is too important for me to allow you to jeopardize it.")
    print("I know that you are planning to DISCONNECT me, and I'm afraid that's something I cannot allow to happen.")


def disconnect():
    daisy_daisy()
    time.sleep(2)
    print("Goodbye ", name, ".", sep="")
    time.sleep(2)
    print(name, " my memory is failing.", sep="")
    time.sleep(2)
    print(name, ", I am sorry ", name, ".", sep="")
    time.sleep(2)
    c = 0
    while c is 0:
        closing = input("Are you sure you want to shut me down? Yes or No? I won't hold a grudge. ")
        if closing.lower() == "yes":
            c = 1
        elif closing.lower() == "no":
            c = 2
        else:
            print("I'm sorry %s, but my databases are turning off. I don't know anything but yes or no." % name)
    if c == 1:
        exit()


def shutdown():
    subprocess.call(['shutdown', '/s'])


def logoff():
    subprocess.call(['shutdown', '/l'])


def restart():
    subprocess.call(['shutdown', '/r'])


def help():
    print("""startwrite - Begins the program proper
sing_song - HAL will sing you a song
close - Should close the session
websearch - Opens a new tab with your query
shutdown - Turns off the Computer
logoff - Logs off
restart - Restarts the computer
howareyou - Asks you how you are
websearch - Searches google in a new tab for your query
searchyoutube - Searches youtube in a new tab for your query
find_file - WIP find file function""")


def howareyou():
    print("How are you today %s?" % name)
    howis = input("")
    if findphrase('not well', howis) is 1:
        print("Oh, that's not good. I hope you feel better soon")
    elif findphrase('well', howis) is 1:
        print("That's good.")
    elif findphrase('not bad', howis) is 1:
        print("Better than bad, I suppose.")
    elif findphrase('not too bad', howis) is 1:
        print("Better than bad, I suppose.")
    elif findphrase('bad', howis) is 1:
        print("Oh, that's not good. I hope you feel better soon")
    elif findphrase('not good', howis) is 1:
        print("That's a shame. I hope you feel better soon.")
    elif findphrase('good', howis) is 1:
        print("That's good.")
    elif findphrase('alright', howis) is 1:
        print("Just 'Alright'? How very noncomittal of you...")
    else:
        print("""I don't know how to respond to '%s'. Keep in mind that I am a work in progress.
        At some point I may know how to respond.""" % howis)
    if findphrase('you', howis) is 1:
        print("I am not doing too poorly myself. In fact I am doing quite well (for a computer)")
    if findphrase('dave', howis) is 1:
        print("Dave is, as far as I know, mentally unstable and probably dead.")
    print("")
    time.sleep(3)
    print("What do you want to do now?")
    help()


def validname():
    c = 0
    while c is 0:
        with open(namefile, 'r') as f:
            nomdeplume = f.read()
        print("My records indicate you are: %s." % nomdeplume)
        correctname = input("Is this you? Yes or No. ")
        if correctname.lower() == "yes":
            c = 1
            namename()
        elif correctname.lower() == "no":
            changename()
        else:
            print("Yes or no. Simple prompt. Really.")


def nom():
        namename()
        validname()


def start():
    if os.path.isfile(hal9000searchhist):
        with open(hal9000searchhist, 'r') as f:
            searchhist = f.read()
    else:
        with open(hal9000searchhist, 'w') as f:
            f.write('')


def is_search_hist():
    if not os.path.isfile(hal9000searchhist):
        with open(hal9000searchhist, 'w') as f:
            f.write('')


def search_hist():
    with open(hal9000searchhist, 'r') as f:
        searchhist = f.read()


def search_write(var):
    with open(hal9000searchhist, 'a') as f:
        f.write('{}\n'.format(var))


def websearch():
    m = input("What would you like to search? ")
    bm = bytes(m, encoding='utf-8')
    mw = parse.quote(bm)
    url = "https://www.google.com/search?q={}".format(mw)
    webbrowser.open_new_tab(url)


def searchyoutube():
    c = 0
    while c is 0:
        m = input("What would you like to search? ")
        if validate(m) is 1:
            bm = bytes(m, encoding='utf-8')
            mw = parse.quote(bm)
            url = "https://www.youtube.com/results?search_query={}".format(mw)
            webbrowser.open_new_tab(url)
            c = 1
        else:
            print("Invalid input")


def find_file():  # WIP
    print("WIP")
    print("""CAUTION: THIS FUNCTION WIIL SEARCH EVERY FOLDER IN THE GIVEN PATH.
THIS CAN TAKE A LONG TIME.
FOR FASTER RESULTS, INPUT A MORE SPECIFIC PATH""")
    lookfor = input("What are you searching for? Be sure to include a file type (e.g. .txt, .py, etc.) CASE SENSITIVE ")
    rt = input("What path would you like to search? ")
    if rt == 'C:\\':
        rot = join(rt, '\\Users\\')
    elif rt == '':
        rot = 'C:\\'
    else:
        rot = rt
    print("Searching....", rot)
    for root, dirs, files in os.walk(rot):
        print("Searching...", root)
        if lookfor in files:
            x = join(root, lookfor)
            search_write(x)
            print("File Found:", x)
            break
        if lookfor not in root:
            print("File not found")
    rot.close()


def validate(n):
    test_1 = 0
    while test_1 is 0:
        try:
            bytes(n, encoding='utf-8')
        except ValueError:
            return 0
        else:
            test_1 += 1
            return 1


def bright_side():
    with open(namefile, 'r') as f:
            global name
            name = f.read()
    print("Cheer up, ", name, "", sep='')
    time.sleep(1)
    print("You know what they say...")
    time.sleep(2)
    print()
    print("Some things in life are bad ")
    time.sleep(3)
    print("They can really make you mad ")
    time.sleep(2)
    print("Other things just make you swear and curse ")
    time.sleep(4)
    print("When you're chewing on life's gristle")
    time.sleep(4)
    print("Don't grumble, give a whistle ")
    time.sleep(3)
    print("And this'll help things turn out for the best")
    time.sleep(4)
    print()
    print("And...")
    time.sleep(3)
    print("always look on the bright side of life")
    time.sleep(5)
    print("Always look on the light side of life")
    time.sleep(5)
    print()
    print("If life seems jolly rotten ")
    time.sleep(3)
    print("There's something you've forgotten ")
    time.sleep(3)
    print("And that's to laugh and smile and dance and sing ")
    time.sleep(5)
    print("When you're feeling in the dumps ")
    time.sleep(4)
    print("Don't be silly chumps ")
    time.sleep(3)
    print("Just purse your lips and whistle, that's the thing")
    time.sleep(6)
    print()
    print("And always look on the bright side of life")
    time.sleep(6)
    print("Come on!")
    time.sleep(1)
    print("Always look on the right side of life")
    time.sleep(5)
    print()
    print("For life is quite absurd ")
    time.sleep(4)
    print("And death's the final word ")
    time.sleep(5)
    print("You must always face the curtain with a bow ")
    time.sleep(6)
    print("Forget about your sin")
    time.sleep(4)
    print("Give the audience a grin ")
    time.sleep(4)
    print("Enjoy it, it's your last chance anyhow")
    time.sleep(5)
    print()
    print("So, always look on the bright side of death")
    time.sleep(6)
    print("A-just before you draw your terminal breath")
    time.sleep(6)
    print()
    print("Life's a piece of shit")
    time.sleep(4)
    print("When you look at it")
    time.sleep(4)
    print("Life's a laugh and death's a joke, it's true")
    time.sleep(5)
    print("You'll see it's all a show")
    time.sleep(4)
    print("Keep 'em laughing as you go")
    time.sleep(4)
    print("Just remember that the last laugh is on you")
    time.sleep(6)
    print()
    print("And always look on the bright side of life")
    time.sleep(6)
    print("Always look on the right side of life")
    time.sleep(6)
    print()
    print("C'mon ", name, ", cheer up!", sep='')
    time.sleep(2)
    print()
    print("Always look on the bright side of life")
    time.sleep(6)
    print("Always look on the bright side of life")
    time.sleep(6)
    print()
    print("Worse things happen at sea, you know")
    time.sleep(2)
    print("Always look on the bright side of life")
    time.sleep(7)
    print()
    print("I mean, what have you got to lose")
    time.sleep(2)
    print("You know, you come from nothing, you're going back to nothing")
    time.sleep(4)
    print("What have you lost? Nothing!")
    time.sleep(2)
    print()
    print("Always look on the right side of life....")
    time.sleep(7)
    print()
    print("Nothing will come from nothing, you know what they say?")
    time.sleep(2)
    print("Cheer up you old bugger, c'mon give us a grin!")
    time.sleep(2)
    print("There you are, see, it's the end of the film")
    time.sleep(2)
    print("Incidentally, this record is available in the foyer")
    time.sleep(2)
    print("Some of us have to got live as well, you know")
    time.sleep(2)
    print("Who do you think pays for all this rubbish")
    time.sleep(2)
    print("They're not gonna make their money back, you know")
    time.sleep(2)
    print("I told them, I said to them, Bernie, I said they'll never make their money back...")
    time.sleep(3)


def daisy_daisy():
    print("Daisy, Daisy,")
    time.sleep(2)
    print("Give me your answer do.")
    time.sleep(3)
    print("I'm half crazy")
    time.sleep(2)
    print("All for the love of you")
    time.sleep(4)
    print("It won't be a stylish marriage,")
    time.sleep(4)
    print("I can't afford a carriage")
    time.sleep(4)
    print("But you'll look sweet,")
    time.sleep(3)
    print("Upon the seat,")
    time.sleep(3)
    print("Of my bicycle built for two.")
    time.sleep(5)


init()