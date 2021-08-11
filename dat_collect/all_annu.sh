filename='all_annu.txt'

a=`find ../Rmag_InstMag/annu_w1_20*|grep annu.txt`


# header
cat $a|head -1 > $filename

# contains
for i in $a;do cat $i|sed '1d' >> $filename;done

#cat $a|sort | uniq|tail -1 > $filename
#cat $a|sort | uniq|sed \$d >> $filename

python insert_iau_name.py
