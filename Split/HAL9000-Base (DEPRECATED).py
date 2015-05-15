import os
import time
import re
import subprocess
import webbrowser
import urllib
import types
from os.path import join

def findphrase(tofind,whatin):
    phrase_pat = re.compile(r'\b({0})\b'.format(tofind), flags=re.IGNORECASE).search
    if phrase_pat(whatin):
        return 1
    else:
        return 0

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
        startwrite()
