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
df12=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202009.txt',sep='|')
df13=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202010.txt',sep='|')
df14=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202011.txt',sep='|')
df15=pd.read_csv('gasp_target_fitsheader_info_exclude_baddata_202012.txt',sep='|')

df_all=pd.concat([df01,df02,df03,df04,df05,df06,df07,df08,df09,df10,df11,df12,df13,df14,df15]).reset_index(drop=True)
#print(df_all)
#print(df_all.ID)

#sys.exit(0)
#idx=df_all.values
idx=df_all.index.values
#print(idx)
#sys.exit(0)

ID=idx+1
#print(ID)
#sys.exit(0)

df_out=df_all
#df_out.col_ID=ID
#print(df_out.col_ID)
df_out[df_out.columns[0]]=ID
#print(df_out[df_out.columns[0]])
#sys.exit(0)

print(df_out)

file_join='gasp_target_fitsheader_info_exclude_baddata_join.txt'

df_out.to_csv(file_join,sep='|',index=False)

cmd_replace_head='find ./|grep calib | grep slt201908[1-3][0-9]| cut -d / -f3 | sort |uniq'
list_file_sci1=os.popen(cmd_replace_head,"r").read().splitlines()



print('')
print('... join all table files to '+file_join+' ...')
print('')


