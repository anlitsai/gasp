#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  30 15:18:28 2019

@author: altsai
"""

"""
Spyder Editor

"""
import os
import sys
import numpy as np
import pandas as pd

df01=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_201804-201901.txt',sep='|')
df02=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_201902-201910.txt',sep='|')
df03=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_201911-201912.txt',sep='|')
df04=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202001.txt',sep='|')
df05=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202002.txt',sep='|')
df06=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202003.txt',sep='|')
df07=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202004.txt',sep='|')
df08=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202005.txt',sep='|')
df09=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202006.txt',sep='|')
df10=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202007.txt',sep='|')
df11=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202008.txt',sep='|')

df_all=pd.concat([df01,df02,df03,df04,df05,df06,df07,df08,df09,df10,df11]).reset_index(drop=True)
#print(df_all)
#print(df_all.ID)

#sys.exit(0)
#idx=df_all.values
idx=df_all.index.values
#print(idx)

ID=idx+1
#print(ID)

df_out=df_all
df_out.ID=ID
#print(df_out.ID)

print(df_out)

file_join='gasp_target_fitsheader_info_exclude_baddata_join.txt'

df_out.to_csv(file_join,sep='|',index=False)

head_info_1='ID|DateObs|TimeObs|Filename|Object|RA_hhmmss|DEC_ddmmss|RA_deg|DEC_deg|RA_pix|Dec_pix|FilterName|JD|ExpTime_sec|Zmag|FWHM|Altitude|Airmass'
head_info_2='1.ID|2.DateObs|3.TimeObs|4.Filename|5.Object|6.RA_hhmmss|7.DEC_ddmmss|8.RA_deg|9.DEC_deg|10.RA_pix|11.Dec_pix|12.FilterName|13.JD|14.ExpTime_sec|15.Zmag|16.FWHM|17.Altitude|18.Airmass'

cmd_replace_head='find ./|grep calib | grep slt201908[1-3][0-9]| cut -d / -f3 | sort |uniq'
list_file_sci1=os.popen(cmd_replace_head,"r").read().splitlines()



print('')
print('... join all table files to '+file_join+' ...')
print('')


