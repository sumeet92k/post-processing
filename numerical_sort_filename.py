"""
Sorts file in a numerically ascending order
"""
import sys
import os
import glob
import re

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

for fname in sorted(glob.glob('time_*.h5'), key=numericalSort): # files are named as time_*.h5
	print(fname)
