#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 04:48:28 2019

@author: altsai
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

generate master bias, master dark, master flat for one month.
$ condaa
$ python slt_calibration_science_target.py slt201908
or
$ python slt_calibration_science_target.py slt20190822

"""



dir_root='/home/altsai/project/20190801.NCU.EDEN/data/gasp/data/'
#dir_root='/home/altsai/gasp/lulin_data/2019/slt/'
#dir_month='slt201908'
#date=dir_month+'22'
#dir_master=dir_month+'_master/'
#dir_calib_sci=date+'_calib_sci/'


import os
import sys
import shutil
#import re
import numpy as np
#import numpy
from astropy.io import fits
#import matplotlib.pyplot as plt
#import scipy.ndimage as snd
#import glob
#import subprocess
#from scipy import interpolate
#from scipy import stats
#from scipy.interpolate import griddata
#from time import gmtime, strftime
import pandas as pd
from datetime import datetime
#from scipy import interpolate
#from scipy import stats



#print("Which Month you are going to process ?")
#yearmonth=input("Enter a year-month (ex: 201908): ")
yearmonth=sys.argv[1]
#yearmonth='201911'
year=str(yearmonth[0:4])
month=str(yearmonth[4:6])

#folder=sys.argv[1]
#folder='slt201908'
dir_month='slt'+yearmonth
#print(dir_month)
dir_master='data/'+yearmonth+'/'+dir_month+'_master/'
#dir_master='data/'+yearmonth+'/'+dir_month+'_master/'

print(dir_master)
#dir_calib_sci=date+'_calib_sci/'
#print(dir_calib_sci)

#if os.path.exists(dir_master):
#    shutil.rmtree(dir_master)
#os.makedirs(dir_master,exist_ok=True)

print('...generate master files on '+dir_month+'...')

#sys.exit(0)


'''
logfile=dir_month+'_master.log'
sys.stdout=open(logfile,'w')
print(sys.argv)
'''




#time_calib_start=strftime("%Y-%m-%d %H:%M:%S", gmtime())
#time_calib_start=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
time_calib_start=str(datetime.now())  
print('Data calibrated by An-Li Tsai at '+time_calib_start+' UTC')


print(' ---------------------------')
print(' Load Master Bias ')
print(' ---------------------------')

cmd_search_file_bias='find ./data/ | grep '+dir_master+' | grep fits | grep master_bias'
print(cmd_search_file_bias)
file_bias=os.popen(cmd_search_file_bias,"r").read().splitlines()[0]

#array_each_bias=np.array([pyfits.getdata(i) for i in file_bias])
master_bias=fits.open(file_bias)[0].data
#print(master_bias)
print('...load master bias: '+file_bias+'...')

#sys.exit(0)





print(' ---------------------------')
print(' Master Dark (subtract from Bias) ')
print(' ---------------------------')
#cmd_search_file_dark='find ./ |grep '+dir_month+' | grep fts | grep Dark'
#list_file_dark=os.popen(cmd_search_file_dark,"r").read().splitlines()
#print(list_file_dark)

array_each_dark=[]
cmd_search_dark='find ./ |grep '+dir_month+' | grep fts | grep Dark | grep 180S'
print(cmd_search_dark)
list_file_dark=os.popen(cmd_search_dark,"r").read().splitlines()
print(list_file_dark)
n_dark=len(list_file_dark)
#sys.exit(0)
print('number of total dark:',n_dark)
#sys.exit(0)
#array_each_bias=np.array([pyfits.getdata(i) for i in list_file_bias])
#array_each_bias=np.array([fits.open(i)[0].data for i in list_file_bias])
n_dark_2048=0
for i in range(n_dark):
    j=list_file_dark[i]
#    print(j)
    imdata=fits.open(j)[0].data
    imhead=fits.open(j)[0].header
    nx=imhead['NAXIS1']
#    print('NAXIS1',nx)
    if nx==2048:
        array_each_dark.append(imdata)
        n_dark_2048=n_dark_2048+1
array_each_dark=np.array(array_each_dark,dtype=int)
print(array_each_dark)
#print(type(array_each_dark))

del list_file_dark

print('number of selected dark:',n_dark_2048)

#print(array_each_dark.shape)
#n_arr_bias=(array_each_dark.shape[0])
#n_arr_bias=len(array_each_dark)
print('number of total px: 2048x2048x',n_dark_2048,' = ', 2048*2048*n_dark_2048)




#print('...start to remove outlier dark...')

#master_dark={}

#array_dark=np.array([fits.open(j)[0].data for j in list_file_dark])
#print('...remove outlier data...')
#dark_keep=reject_outliers_data(array_dark,par1)
#    dark_each_time_keep2=reject_outliers_data(dark_each_time_keep,3)
#    print(dark_keep)
print('...generate master dark...')
#dark_subtract=array_dark-master_bias
dark_subtract=array_each_dark-master_bias
mean_dark=np.mean(dark_subtract,axis=0)
#print('...remove outlier pixel...')
#mean_dark_keep=reject_outliers_px(mean_dark,par2)
master_dark=mean_dark
#print('skip this step')
#    master_dark[i]=mean_dark_each_time_keep
#    print(master_dark_each_time[1000][1000])
#    plt.title('Master Dark '+i)
#    plt.imshow(master_dark_each_time)
#    plt.show()
print('...output master dark to fits file...')
fitsname_master_dark='master_dark_180S_'+dir_month+'.fits'
now=str(datetime.now())  
#    fits.header.add_history('Master Dark generated at '+now+' UTC')
#    hdu=fits.PrimaryHDU(master_dark[i])
hdu=fits.PrimaryHDU(master_dark)
hdu.writeto(dir_master+fitsname_master_dark,overwrite=True)
#    now=str(datetime.now())  
#    imhead.add_history('Master bias is applied at '+now+' UTC')
#    fits.writeto(fitsname_master_dark,data=master_dark_each_time,header=imhead,overwrite=True)

#del list_file_dark
del array_each_dark
#del array_dark

print('... finished ...')

