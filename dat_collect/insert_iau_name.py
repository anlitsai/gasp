#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:53:52 2021

@author: altsai
"""


import numpy as np
#import csv
#import time
import math
import pandas as pd
import sys


file_in='all_annu.txt'
#file_in='test2.txt'
#file_in='test.txt'

df_in=pd.read_csv(file_in,sep='|')
print(df_in)
n_in=int(np.float64(len(df_in)))
#n_in=len(df_in)
print('# of data in',n_in)

#sys.exit(0)

      
file_iau='iau_name.txt'
df_iau=pd.read_csv(file_iau,sep="|")

iau_name=['']*n_in

i=0
for i in range(n_in):
#while i < n_in:
    obj_name=df_in['Object'][i]
#    print(obj_name)
    date=df_in['DateObs'][i]
    time=df_in['TimeObs'][i]
    filename=df_in['Filename'][i]
    iau_name[i]=df_iau[df_iau['obj_name']==obj_name]['IAU_name'].tolist()[0]
#    print(iau_name[i])
#    print(i,iau_name[i],obj_name,date,time,filename)
#    i += 1


#file_out=''
df_out=df_in.drop(['Unnamed: 0'],axis=1)
#df_out=df_out.insert(4,"IAU_name",iau_name)
df_out['IAU_name']=iau_name
print(df_out)
#print(df_out['IAU_name'])
file_out='all_annu_iau.txt'
df_out.to_csv(file_out,sep='|')

print('... write file to : ',file_out)
