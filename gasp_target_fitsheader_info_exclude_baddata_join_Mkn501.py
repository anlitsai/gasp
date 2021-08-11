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

df01=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201702.txt',sep='|')
df02=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201703.txt',sep='|')
df03=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201704.txt',sep='|')
df04=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201705.txt',sep='|')
df05=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201706.txt',sep='|')
df06=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201707.txt',sep='|')
df07=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201708.txt',sep='|')
df08=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201709.txt',sep='|')
df09=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201710.txt',sep='|')
df10=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201802.txt',sep='|')
df11=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201803.txt',sep='|')
df12=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201804.txt',sep='|')
df13=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201805.txt',sep='|')
df14=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201806.txt',sep='|')
df15=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201807.txt',sep='|')
df16=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201808.txt',sep='|')
df17=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201809.txt',sep='|')
df18=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201810.txt',sep='|')
df19=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201811.txt',sep='|')
df20=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201901.txt',sep='|')
df21=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201902.txt',sep='|')
df22=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201903.txt',sep='|')
df23=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201904.txt',sep='|')
df24=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201905.txt',sep='|')
df25=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201906.txt',sep='|')
df26=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201907.txt',sep='|')
df27=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201908.txt',sep='|')
df28=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201909.txt',sep='|')
df29=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201910.txt',sep='|')
df30=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_201911.txt',sep='|')
df31=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_202001.txt',sep='|')
df32=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_202002.txt',sep='|')
df33=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_202003.txt',sep='|')
df34=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_202004.txt',sep='|')
df35=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_202005.txt',sep='|')
df36=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_202006.txt',sep='|')
df37=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_202007.txt',sep='|')
df38=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_202008.txt',sep='|')
df39=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_202009.txt',sep='|')
df40=pd.read_csv('./data/gasp_target_fitsheader_info_exclude_baddata_202010.txt',sep='|')

df_all=pd.concat([df01,df02,df03,df04,df05,df06,df07,df08,df09,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36,df37,df38,df39,df40]).reset_index(drop=True)
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

file_join='gasp_target_fitsheader_info_exclude_baddata_join_Mkn501.txt'

df_out.to_csv(file_join,sep='|',index=False)

cmd_replace_head='find ./|grep calib | grep slt201908[1-3][0-9]| cut -d / -f3 | sort |uniq'
list_file_sci1=os.popen(cmd_replace_head,"r").read().splitlines()



print('')
print('... join all table files to '+file_join+' ...')
print('')


