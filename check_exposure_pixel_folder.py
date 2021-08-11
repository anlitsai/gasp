#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:54:00 2019

@author: altsai
"""

"""
Spyder Editor

data calibration for science target.
$ condaa
$ python slt_calibration_science_target.py _FOLDER_NAME_

for example:
$ python slt_calibration_science_target.py slt2020101018
"""

import os
import sys
import shutil
#import re
import numpy as np
#import numpy
from astropy.io import fits
#import pyfits
import matplotlib.pyplot as plt
#import scipy.ndimage as snd
#import glob
#import subprocess
#from scipy import interpolate
#from scipy import stats
#from scipy.interpolate import griddata
#from time import gmtime, strftime
#import pandas as pd
from datetime import datetime

#print()
#print('format: python check_exposure_pixel.py slt20201010')
#print()

folder=sys.argv[1]
#folder='nowt/bg_flatten'
#folder='nowt/20201008/clusters_TW/Fu_Ori/'
#folder='nowt/20201008/'
#folder='slt20191201'
#print("Which Folder you are going to process ?")li
#folder=input("Enter a Folder (ex: slt20190822): ")
print()
print('python check_exposure_pixel.py',folder)
print()

#date=folder[3:]
#year=str(date[0:4])
#month=str(date[4:6])
#yearmonth=year+month
#day=str(date[6:8])
#folder='slt'+date
#dir_folder=yearmonth+'/'+folder+'/'
dir_folder=folder



#dir_sci=yearmonth+'/'+folder+'/'

#dir_calib_sci=yearmonth+'/'+folder+'_calib_sci/'
#dir_calib_sci='data/'+yearmonth+'/'+folder+'_calib_sci/'

#print(dir_sci)



#sys.exit(0)



print(' ---------------------------')
print(' All Targets ')
print(' ---------------------------')

print(folder)
#cmd_search_file_sci="find ./ | grep "+dir_folder+" | grep fts | grep FU_Ori "
#cmd_search_file_sci="find ./ | grep "+dir_folder+" | grep 'fts\|new' | grep FU_Ori "
#cmd_search_file_sci="find ./"+dir_folder+" | grep Ori|grep 'fits' "
cmd_search_file_sci="find ./"+dir_folder+" |grep 'fts' "
print(cmd_search_file_sci)
list_file_sci=os.popen(cmd_search_file_sci,"r").read().splitlines()
print('...check exposure time and pixel size of all files...')
#print(list_file_sci)
print(len(list_file_sci))
#sys.exit(0)



for i in list_file_sci:
    hdu=fits.open(i)[0]
    imhead=hdu.header
    imdata=hdu.data
#    print(imdata.shape)
    exptime=imhead['EXPTIME']
    idx_time=str(int(exptime))+'S'
#    print(idx_time)
#    print(exptime)
#    imtype=imhead['IMAGETYP']
#    naxis=imhead['NAXIS']
#    print(naxis)
#    jd=imhead['JD']
    obj=imhead['OBJECT']
#    try:
#        fwhm=imhead['FWHM']
#    except:
#        fwhm=-9999
#    try:
#        zmag=imhead['ZMAG']
#    except:
#        zmag=-9999
#    airmass=imhead['AIRMASS']
#    altitude=imhead['ALTITUDE']
#    ra=imhead['RA']
#    dec=imhead['Dec']
    nx1=imhead['NAXIS1']
    nx2=imhead['NAXIS2']
    xbin=imhead['XBINNING']
    ybin=imhead['YBINNING']
#    xc=str(int(imhead['CRVAL1']))
#    yc=str(int(imhead['CRVAL2']))
#    xc=str(int(imhead['XCNTPIX']))
#    yc=str(int(imhead['YCNTPIX']))

#    print(i, "\t", str(nx1)+"x"+str(nx2),"\t",idx_time,"\t",str(imtype),"\t",str(obj))
#    print(i, "\t", str(nx1)+"x"+str(nx2),"\t",str(xc)+"x"+str(yc),"\t",idx_time,"\t",str(obj))
    print(i, "\t", str(nx1)+"x"+str(nx2),"\t",str(xbin)+"x"+str(ybin),"\t",idx_time,"\t",str(obj))
    
#sys.exit(0)


print(' ---------------------------')

print()


