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

from config import *
from songs import *

def startwrite():
    global name
    with open(namefile,'r') as f:
        global name
        name = f.read()
    print("""Hello """,name,""".
I am HAL-9000 running in Python.
I was created by the Dr3dge initiative and written by Rozza15.
I am here to help you complete your mission.
If you need help, feel free to ask. Just type "help()".""",sep="")
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
                print("Oh good. I am glad you liked it",name)
                c = 1
            elif m.lower() == "no":
                print("Oh. That makes me sad. Most people like my singing.")
                c = 1
            else:
                print("Please",name,"just Yes or No. Did you like my singing?")      

def close():
    print("I am sorry ",name,", but I am afraid I can't do that.",sep="")
    print("This mission is too important for me to allow you to jeopardize it.")
    print("I know that you are planning to DISCONNECT me, and I'm afraid that's something I cannot allow to happen.")

def disconnect():
    daisy_daisy()
    time.sleep(2)
    print("Goodbye ",name,".", sep="")
    time.sleep(2)
    print(name," my memory is failing.",sep="")
    time.sleep(2)
    print(name,", I am sorry ",name,".",sep="")
    time.sleep(2)
    c = 0
    while c is 0:
        closing = input("Are you sure you want to shut me down? Yes or No? I won't hold a grudge. ")
        if closing.lower() == "yes":
            c = 1
        elif closing.lower() == "no":
            c = 2
        else:
            print("I'm sorry ",name,", but my databases are turning off. I don't know anything but yes or no.",sep="")
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
    print("How are you today ",name,"?",sep="")
    howis = input("")
    if findphrase('not well', howis) is 1:
        print("Oh, that's not good. I hope you feel better soon")
    elif findphrase('well', howis) is 1:
        print("That's good.")
    elif findphrase('not bad', howis) is 1:
        print("Better than bad, I suppose.")
    elif findphrase('not too bad',howis) is 1:
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
        print("I dont know how to respond to '",howis,"'. Keep in mind that I am a work in progress. At some point I may know how to respond.", sep="")
    if findphrase('you',howis) is 1:
        print("I am not doing too poorly myself. In fact I am doing quite well (for a computer)")
    if findphrase('dave',howis) is 1:
        print("Dave is, as far as I know, mentally unstable and probably dead.")

    print("")
    time.sleep(3)
    print("What do you want to do now?")
    help()
