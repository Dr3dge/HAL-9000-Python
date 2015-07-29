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
    mw = urllib.parse.quote(bm)
    url = "https://www.google.com/search?q={}".format(mw)
    webbrowser.open_new_tab(url)


def searchyoutube():
    c = 0
    while c is 0:
        m = input("What would you like to search? ")
        if validate(m) is 1:
            bm = bytes(m, encoding='utf-8')
            mw = urllib.parse.quote(bm)
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
    searchfile.close()


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
