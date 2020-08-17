#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:15:21 2020

@author: altsai
"""


#import os
#import sys
#import shutil
import numpy as np
#import csv
#import time
#import math
import pandas as pd
import matplotlib.pyplot as plt

nn=30

'''
 0|0219+428|3C66A      |g0219r_LuS_20180401-now.dat|
 1|0235+164|AO0235+16  |g0235r_LuS_20180401-now.dat|
 2|0716+714|S5_0716+71 |g0716r_LuS_20180401-now.dat|
 3|0735+178|PKS0735+17
 4|0827+243|OJ248      |g0827r_LuS_20180401-now.dat|
 5|0829+046|OJ49       |g0829r_LuS_20180401-now.dat|
 6|0836+710|4C71-07    |g0836r_LuS_20180401-now.dat|
 7|0851+202|OJ287
 8|0954+658|S4_0954+65 |g0954r_LuS_20180401-now.dat|
 9|1101+384|Mkn421     |g1101r_LuS_20180401-now.dat|
10|1156+295|4C29-45    |g1156r_LuS_20180401-now.dat|
11|1219+285|ON231      |g1219r_LuS_20180401-now.dat|
12|1226+023|3C273      |g1226r_LuS_20180401-now.dat|
13|1253-055|3C279      |g1253r_LuS_20180401-now.dat|
14|1510-089|KS1510-08
15|1611+343|DA406
16|1633+382|4C38-41
17|1641+399|3C345
18|1652+398|Mkn501     |g1652r_LuS_20180401-now.dat|
19|1739+522|4C51-37    |g1739r_LuS_20180401-now.dat|
20|1807+698|3C371      |g1807r_LuS_20180401-now.dat|
21|2155-304|PKS2155-304|g2155r_LuS_20180401-now.dat|
22|2200+420|L-Lacertae |g2200r_LuS_20180401-now.dat|
23|2230+114|CTA102     |g2230r_LuS_20180401-now.dat|
24|2251+158|3C454-3    |g2251r_LuS_20180401-now.dat|
25|2344+514|ES2344+514 |g2344r_LuS_20180401-now.dat|
'''
list_objname=['3C66A', 'AO0235+16', 'S5_0716+71', 'PKS0735+17', 'OJ248', 'OJ49', '4C71-07', 'OJ287', 'S4_0954+65', 'Mkn421', '4C29-45', 'ON231', '3C273', '3C279', 'KS1510-08', 'DA406', '4C38-41', '3C345', 'Mkn501', '4C51-37', '3C371', 'PKS2155-304', 'L-Lacertae', 'CTA102', '3C454-3', 'ES2344+514']
list_iauname=['0219+428','0235+164','0716+714','0735+178','0827+243','0829+046','0836+710','0851+202','0954+658','1101+384','1156+295','1219+285','1226+023','1253-055','1510-089','1611+343','1633+382','1641+399','1652+398','1739+522','1807+698','2155-304','2200+420','2230+114','2251+158','2344+514']


n_data=len(list_objname)

fig,axs=plt.subplots(4,7,figsize=(20,16))
fig.subplots_adjust(hspace=.5,wspace=0.5)
axs=axs.ravel()

for i in range(n_data):
    file_iau=list_iauname[i]
    file_obj=list_objname[i]

    w1_file='dat_file/g'+file_iau[0:4]+'r_LuS_20180401-now.dat'
    df_w1=pd.read_csv(w1_file,delim_whitespace=True,header=None,usecols=[0,1,2]) 
    JD1=df_w1[0].map('{:.5f}'.format).astype(np.float64)
#    print(JD1)
    R1=df_w1[1]
#    print(R1)
    eR1=df_w1[2]
#    print(eR1)
    

#    axs[i].errorbar(JD0,R0,yerr=eR0,linestyle='--',label='no w',lw=1)
    axs[i].errorbar(JD1,R1,yerr=eR1,linestyle='--',lw=1)  
    axs[i].set_xlabel('JD')
    axs[i].set_ylabel('Rmag')
    axs[i].set_title(file_obj)
    axs[i].invert_yaxis()
#    axs[i].legend(loc='best')
    


plt.savefig('dat_file.pdf')   
    
