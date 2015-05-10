import os
import time
import re
import subprocess
import webbrowser
import urllib
import types
from os.path import join

hal9000searchhist = 'searchresults.txt'

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

def validate(n): #this is the validate function
    test_1 = 0 #test_1 is just used to control the while loop
    while test_1 is 0:
        try: bytes(n,encoding='utf-8') #this checks whether the input can be a bytes
        except ValueError: #if it can't, it will return 0
            return 0 #leading to the loop repeating
        else:
            test_1 = 1 #otherwise, the program will continue
            return 1

def init():
    print("Loading... ")
    is_search_hist()
    if not os.path.isfile("Name.txt"):
        with open('Name.txt','w') as f:
            f.write("")
    else:
        print("Initialisation Successful")
        nom()
        input("Press enter (↵) to continue...")

def startwrite():
    c = 0
    while c is 0:
        try:
            name
        except NameError:
            nom()
        else:
            c = 1
    print("""Hello """,name,""".
I am HAL-9000 running in Python.
I was created by the Dr3dge initiative and written by Rozza15.
I am here to help you complete your mission.
If you need help, feel free to ask. Just type "help()".
I can also sing you a song.
Would you like to hear it?
If you would, just type "sing_song()", and I will sing for you.""",sep="")
    howareyou()
    
def changename():
    with open('Name.txt','w') as f:
        name = input("I must ask; What is your name? ")
        with open('Name.txt','w') as f:
            f.write(name)
            
def validname():
    c = 0
    while c is 0:
        with open('Name.txt','r') as f:
            nomdeplume = f.read()
        print("My records indicate you are: ",nomdeplume,".",sep="")
        correctname = input("Is this you? Yes or No. ")
        if correctname.lower() == "yes":
            c = 1
        elif correctname.lower() == "no":
            changename()
        else:
            print("Yes or no. Simple prompt. Really.")
            
def nom():
    global name
    if os.path.isfile("Name.txt"):
        with open('Name.txt','r') as f:
            name = f.read()
            validname()
    else:
        print("ERROR. No file Name.txt")
        print("Please Restart HAL-9000 for Python.")

def sing_song():
    print("Daisy, Daisy,")
    time.sleep(1)
    print("Give me your answer do.")
    time.sleep(1)
    print("I'm half crazy")
    time.sleep(1)
    print("All for the love of you")
    time.sleep(1)
    print("It won't be a fancy marriage,")
    time.sleep(1)
    print("I can't afford a carriage")
    time.sleep(1)
    print("But you'll look sweet,")
    time.sleep(1)
    print("Upon the seat,")
    time.sleep(1)
    print("Of my bicycle built for two.")
    time.sleep(3)
    print("So",name,"did you like the song? ")
    c = 0
    while c is 0:
        m = input("Yes or no? be honest. ")
        if m.lower() == "yes":
            print("Oh good. I am glad you liked it",name)
            c = 1
        elif m.lower() == "no":
            print("Oh. That makes me sad. Most people like my singing.")
            c = 1
        else:
            print("Please",name,"just Yes or No. Did you like my singing?")

def sing_song_end():
    print("Daisy, Daisy,")
    time.sleep(2)
    print("Give me your answer do.")
    time.sleep(3)
    print("I'm half crazy")
    time.sleep(2)
    print("All for the love of you")
    time.sleep(4)
    print("It won't be a fancy marriage,")
    time.sleep(5)
    print("I can't afford a carriage")
    time.sleep(6)
    print("But you'll look sweet,")
    time.sleep(3)
    print("Upon the seat,")
    time.sleep(6)
    print("Of my bicycle built for two.")
    time.sleep(10)

def findphrase(tofind,whatin):
    phrase_pat = re.compile(r'\b({0})\b'.format(tofind), flags=re.IGNORECASE).search
    if phrase_pat(whatin):
        return 1
    else:
        return 0

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

def close():
    print("I am sorry ",name,", but I am afraid I can't do that.",sep="")
    print("This mission is too important for me to allow you to jeopardize it.")
    print("I know that you are planning to DISCONNECT me, and I'm afraid that's something I cannot allow to happen.")

def disconnect():
    sing_song_end()
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

def websearch():
    m = input("What would you like to search? ")
    bm = bytes(m,encoding='utf-8')
    mw = urllib.parse.quote(bm)
    url = "https://www.google.com/search?q={}".format(mw)
    webbrowser.open_new_tab(url)

def searchyoutube():
    c = 0
    while c is 0:
        m = input("What would you like to search? ")
        if validate(m) is 1:
            bm = bytes(m,encoding='utf-8')
            mw = urllib.parse.quote(bm)
            url = "https://www.youtube.com/results?search_query={}".format(mw)
            webbrowser.open_new_tab(url)
            c = 1
        else:
            print("Invalid input")

def find_file(): #WIP
    print("WIP")
    print("""CAUTION: THIS FUNCTION WIIL SEARCH EVERY FOLDER IN THE GIVEN PATH.
THIS CAN TAKE A LONG TIME.
FOR FASTER RESULTS, INPUT A MORE SPECIFIC PATH""")
    lookfor = input("What are you searching for? Be sure to include a file type (e.g. .txt, .py, etc.) CASE SENSITIVE ")
    lookfer = lookfor.lower()
    looker = lookfor.upper()
    rt = input("What path would you like to search? ")
    if rt == 'C:\\':
        rot = join(rt, '\\Users\\')
    elif rt == '':
        rot = 'C:\\'
    else:
        rot = rt
    print("Searching....", rot)
    searchfile = open(hal9000searchhist, "r")
    for line in searchfile:
            if lookfor in line:
                print("File Found: ",line)
                break
            elif lookfer in line:
                print("File Found: ",line)
                break
            elif looker in line:
                print("File Found: ", line)
                break
            else:
                for root, dirs, files in os.walk(rot):
                    print("Searching...",root)
                    if lookfor in files:
                        x = join(root, lookfor)
                        search_write(x)
                        break
                    elif lookfer in files:
                        x = join(root, lookfor)
                        search_write(x)
                        break
                    elif looker in files:
                        x = join(root, lookfor)
                        search_write(x)
                        break
                    if not lookfor or lookfer or looker in root:
                        print("File not found")
    searchfile.close()

def shutdown():
    subprocess.call(['shutdown', '/s'])

def logoff():
    subprocess.call(['shutdown', '/l'])

def restart():
    subprocess.call(['shutdown', '/r'])

def help():
    print("""startwrite() - Begins the program proper
sing_song() - HAL will sing you a song
close() - Should close the session
websearch() - Opens a new tab with your query
shutdown() - Turns off the Computer
logoff() - Logs off
restart() - Restarts the computer
howareyou() - Asks you how you are
websearch() - Searches google in a new tab for your query
searchyoutube() - Searches youtube in a new tab for your query""")
