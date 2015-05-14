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
from searching import *
from name import *
from miscfunc import *
from os.path import join
from config import *

def init():
    print("Loading... ")
    is_search_hist()
    start()
    nom()
    print("Initialisation Successful")
    input("Press enter (↵) to continue...")
    startwrite()
