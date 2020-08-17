a=`ls  -d Rmag_InstMag/annu_w1_20????01*/`
#for i in $a;do echo $i; find ./$i|grep dat;done
#for i in $a;do find ./$i|grep dat;done
for i in $a;do find ./$i|grep dat;done > dat.list
#for i in $a;do  find ./$i|grep dat;done |sort  -t '/' -k4,4 -k3,3n
#b=`for i in $a;do  find ./$i|grep dat;done |sort  -t '/' -k4,4 -k3,3n`
#c=`cat check_science_target_list.txt`
#for i in $c;do echo $i; for j in $b; do echo $j|grep $i;done;done
#for i in $c;do echo $i; d=`for j in $b; do echo $j|grep $i;done`;echo $d; cat $d > done

id=`for i in $a;do find ./$i|grep dat;done| cut -d '/' -f5 | cut -d _ -f1|sort|uniq`
#for i in $id; do echo $i;cat dat.list|grep $i;done
for i in $id; do echo $i;f=`cat dat.list|grep $i`;cat $f |sort > ./Rmag_InstMag/dat_file/$i"_LuS_20180401-now.dat";done

