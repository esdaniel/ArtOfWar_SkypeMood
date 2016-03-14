#!/usr/bin/python3

"""
Created on Sat Mar 12 20:57:41 2016

Script to change Skype mood status to a
random quote from Sun Tzu's 'The Art of War'
http://www.artofwarquotes.com/

@author: esdaniel
"""

import os
import sys
import random
from skype_mood import mood

# Change working path to location of this script
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# Populate list from quotes.txt
try:
    fname = "quotes.txt"

    with open(fname) as f:
        quotes = f.readlines()

    # Pick a random quote and strip carriage return
    quote = '"' + random.choice(quotes)[:-1] + '"'
    #print(quote)
    
    # Update skype mood with quote
    mood(quote)

except:
    print("Could not read file")
    mood("")
    exit()