
find ./Rmag_InstMag/annu_w1_2020* |grep dat | sort -t "/" -k4 > dat_list_2020.txt 

ff=`cat check_science_target_list.txt`

#for i in $ff;do echo $i;done
#for i in $ff;do echo $i;cat dat_list_2020.txt|grep $i;done

rm -rf dat_file/dat_file_2020/*
for i in $ff;do echo $i;iau_name=`cat dat_list_2020.txt|grep $i|cut -d "/" -f5|cut -d _ -f1|uniq`;lst=`cat dat_list_2020.txt|grep $i`;for j in $lst;do cat $j >> dat_file/dat_file_2020/$iau_name"_LuS_2020.dat";done;done

