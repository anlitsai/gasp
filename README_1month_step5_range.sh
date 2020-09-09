#a='202003'
#a=$1


#c=`cat check_science_target_list.txt`
#c='Mkn421'
#c='S4_0954+65'
c='L-Lacertae'

year=`echo $a|cut -c-4`
month=`echo $a|cut -c5-6`
ym=`echo $year'-'$month`

last_date=`cat gasp_target_fitsheader_info_exclude_baddata_join.txt | grep $ym|tail -1| cut -d "|" -f2| cut -d - -f3`

#d1=$a'01'
#d2=$a$last_date

d1='20200311'
d2='20200831'

for i in $c;do python Rmag_aperture_annulus_r_file_median_w1_subplot_date_target.py $d1 $d2 $i | tee 'Rmag_aperture_annulus_r_file_median_w1_subplot_'$d1'-'$d2'_'$i'.log';done


