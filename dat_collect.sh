

echo "=== collect dat files ==="

iau_list=`cat iau_name.txt`

for i in $iau_list;do 
  iau_idx=`echo ${i:0:4}`;
  echo $iau_idx;
  dat_list=`find ./Rmag_InstMag/annu_w1_2*|grep dat|grep $iau_idx`;
  #echo $dat_list;
  date=`find ./Rmag_InstMag/annu_w1_2*|grep dat|grep $iau_idx|cut -d / -f3|cut -d _ -f3`;
  #echo $date;
  for j in $date;do
    dat_out='g'$iau_idx'r_LuS_'$j'.dat';
    #echo $dat_out;
    cat $dat_list > dat_collect/$dat_out;
  done
done



echo "=== collect annu.txt data files ==="

txt_list1=`find ./Rmag_InstMag/annu_w1_2*|grep annu.txt`
txt_list2=`find ../gasp_Mkn501_201701-202010/Rmag_InstMag/annu_w1_2*|grep annu.txt`
cat $txt_list1 $txt_list2 |sort -t "|" -k3 -k4  |uniq |cut -d "|" -f3- > dat_collect/all_annu.txt

echo "... done ..."
