# generate light curve plot for all targets
# before run this script, remember to clean the directory Rmag_InstMag

a=`ls  -d Rmag_InstMag/annu_w1_20????01*/`
for i in $a;do find ./$i|grep dat;done > dat.list
#for i in $a;do  find ./$i|grep dat;done |sort -t '/' -k4,4 -k3,3n

id=`for i in $a;do find ./$i|grep dat;done| cut -d '/' -f5 | cut -d _ -f1|sort|uniq`
for i in $id; do echo $i;f=`cat dat.list|grep $i`;cat $f |sort > ./dat_file/$i"_LuS_20180401-now.dat";done

python dat_plot.py


