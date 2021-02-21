# generate light curve plot for Mkn501 from 201701-202010
# -----------------------------
# before run this script, remember to move special range to the directory in Rmag_InstMag/special_range
# -----------------------------
folder=`cat folder_Mkn501_201701-202010.list`

a=`for i in $folder;do dir='Rmag_InstMag/annu_w1_'$i'01'*/;echo $dir;done`
# -----------------------------

file_root='Mkn501_201701_202010'
file_dat='dat_'$file_root'.list'

dir_dat='dat_'$file_root
rm -rf $dir_dat
mkdir $dir_dat

id='g1652r'

for i in $a;do find ./$i|grep dat|grep $id;done > $file_dat
dat_list=`cat $file_dat`

dat_Mkn501='g1652r_LuS_20200220.dat'
rm -rf $dat_Mkn501

for i in $dat_list;do cat $i >> $dir_dat/$dat_Mkn501;done



#for i in $id; do echo $i;f=`cat $file_dat|grep $i`;cat $f |sort > ./$dir_dat/$i"_LuS_"$file_root".dat";done

# -----------------------------
# after finishing above steps, run:
# -----------------------------
python dat_plot_Mkn501_201701-202010.py


