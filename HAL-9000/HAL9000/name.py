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


def validname():
    c = 0
    while c is 0:
        with open(namefile, 'r') as f:
            nomdeplume = f.read()
        print("My records indicate you are: ", nomdeplume, ".", sep="")
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
