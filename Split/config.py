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
import urllib
import types

def namename():
    with open('Name.txt','r') as f:
        global name
        name = f.read()

def changename():
    with open('Name.txt','w') as f:
        neme = input("I must ask; What is your name? ")
        with open('Name.txt','w') as f:
            f.write(neme)

def findphrase(tofind,whatin):
    phrase_pat = re.compile(r'\b({0})\b'.format(tofind), flags=re.IGNORECASE).search
    if phrase_pat(whatin):
        return 1
    else:
        return 0
