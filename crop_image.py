# -*- coding: utf-8 -*-
#! /usr/bin/python3
# final fit result: CROPS IMAGES WITH A TRANSPARENT BACKGROUND
# RESULTS: CROPS IMAGES WITH A TRANSPARENT BACKGROUND
# RESULTS FOR: CROPS IMAGES WITH A TRANSPARENT BACKGROUND

import os
import glob
import re
import sys
from PIL import Image

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

dirName = 'images_cropped'
try:
	# Create target Directory
	os.mkdir(dirName)
	print("Directory " , dirName ,  " Created ") 
except FileExistsError:
	print("Directory " , dirName ,  " already exists")
	
# the below not working correctly
#if not os.path.exists('dirName'):
    #os.mkdir(dirName)
if len(sys.argv) > 1:
	fname = sys.argv[1]
	fname_write = dirName + '/' + fname.split('.png')[0] + '_crp.png'
	im=Image.open(fname)
	im.size
	im.getbbox()
	im_crp = im.crop(im.getbbox())
	im_crp.size
	im_crp.save(fname_write)
else:
	#fname = "../data/comp_0_3840000.png"
	#if fname == fname:
	for fname in sorted(glob.glob('contour_*.png'), key=numericalSort):
		fname_write = dirName + '/' + fname.split('.png')[0] + '_crp.png'
		im=Image.open(fname)
		im.size
		im.getbbox()
		im_crp = im.crop(im.getbbox())
		im_crp.size
		im_crp.save(fname_write)
