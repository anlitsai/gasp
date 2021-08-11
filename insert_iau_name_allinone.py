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
import os

file_iau='iau_name.txt'
df_iau=pd.read_csv(file_iau,sep="|")
#print(df_iau)

#cmd_search_file_raw='find ./ | grep 2107|grep barnards|grep fit|cut -d / -f4' 
cmd_search_file_annu='find ./Rmag_InstMag/annu_w1_* | grep annu.txt' 
print(cmd_search_file_annu)
list_file_annu=os.popen(cmd_search_file_annu,"r").read().splitlines() #[0]
#print(list_file_annu)
n_file_annu=len(list_file_annu)




sys.exit(0)

#file_in='all_annu.txt'
#file_in='test2.txt'
#file_in='test.txt'



#for i in range(n_file_annu):
n_nodata=0

for i in range(n_file_annu):
    print('------')
    print(i,'/',n_file_annu)
    file_in=list_file_annu[i]
    print(file_in)
    file_root=file_in.split('.',-1)[1]
#    print(file_root)
    file_out='.'+file_root+'_iau.txt'
#    print(file_out)  
#    print('------')


        
    df_in=pd.read_csv(file_in,sep='|').reset_index(drop=True)
#    print(df_in)
    n_in=len(df_in)
#    print(n_in)

        
    
#    df_out=df_in.drop(['Unnamed: 0','ID'],axis=1).reset_index(drop=True)
#    print(df_out)
    
    #n_in=len(df_in)
#    print('# of data in',n_in)


    if n_in>0:
    
        obj_name=df_in['Object'][0]
        print('obj_name = ',obj_name)
#    iau_name=df_iau[df_iau['obj_name'].str.contains(obj_name)]['IAU_name'].tolist()[0]
        iau_name=df_iau[df_iau['obj_name']==obj_name]['IAU_name'].tolist()[0]
#    print(iau_name)
        print('iau_name = ', iau_name)


#    sys.exit(0)

#    iau_name=['']*n_in

#    for j in range(n_in):
        
#        date=df_in['DateObs'][j]
#        time=df_in['TimeObs'][j]
#        filename=df_in['Filename'][j]
#        obj_name=df_in['Object'][j]
#        print(obj_name)
#        iau_name[j]=df_iau[df_iau['obj_name'].str.contains(obj_name)]['IAU_name'].tolist()[0]
#        iau_name[j]=df_iau[df_iau['obj_name']==obj_name]['IAU_name'].tolist()[0]
#        print(iau_name[j])

#        print(iau_name[i])
#        print(i,iau_name[i],obj_name,date,time,filename)
        
    
        df_out=df_in
#    print('df_out (1)', df_out)

#    df_out=df_out.insert(4,"IAU_name",iau_name)
#    print(df_out)
#    print(df_out['IAU_name'])

        df_out=df_in.drop(['Unnamed: 0'],axis=1)
#    print('df_out (2)',df_out)
    
        df_out.insert(5,'IAU_name',iau_name)
#    df_out.insert(5,"IAU_name",iau_name)

#    print('df_out (3)',df_out)


#        file_out='.'+file_root+'_iau.txt'
        print('write file to : ', file_out)    
        df_out.to_csv(file_out,sep='|')
    
        del df_in
        del df_out

    else:
        f=open(file_out,'w')
        f.write("|ID|DateObs|TimeObs|Filename|Object|IAU_name|RA_hhmmss|DEC_ddmmss|RA_deg|DEC_deg|RA_pix|Dec_pix|FilterName|JD|ExpTime_sec|Zmag|FWHM|Altitude|Airmass|Rmag|ErrorCounts|ErrorInstMag|ErrorFitting|ErrorRmag")
        f.close()
        n_nodata=n_nodata+1


print(n_nodata,'files have no data......')
