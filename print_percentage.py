# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:11:18 2020

@author: Matheus Murdiga
"""

# I wrote this code for my thesis in Materials Engineering.
# I was looking for a code to print a progress bar in Python, 
# 		but I could't find something that could handle any maximum value (like 827) 
#		and any number of divisions (like 100, but you can use any value).
# Remove line 39 and then line 14 to use in your code, these lines are useless.

import sys
from time import sleep
import numpy as np
    
# Define the mininum and maximum value and the number of divisions to print
minValue = 1
maxValue = 827
nDivision = 100

# Get an Array with 100 values between minValue and maxValue and convert to int
linearSpace = np.around(np.linspace(minValue, maxValue, nDivision), 0).tolist()
linearSpace = [int(i) for i in linearSpace]


# Loop in a range between the mininum value and the maximum with closed interval
for n in range(minValue, maxValue+1):
    # If the loop value is on the list, you need to print this value in progress bar
    if (n in linearSpace):
        # Using the index you know how far you are in the progress bar
        index = linearSpace.index(n) + 1
        blankSpaces = (nDivision - index)
        percentage = str(round((100*n)/(maxValue/minValue), 2))
        
        # Print '=' index times, and ' ' blankSpace times.
        sys.stdout.write("\r[" + "=" * index +  " " * blankSpaces + "] " + percentage + "%   ")
        sys.stdout.flush()
        sleep(0.1)