#a='202003'
a=$1


# mannuly modify $c
#c=`cat check_science_target_list.txt`
c='4C71-07'
#c='4C38-41'
#c='3C454-3'
#c='DA406'
#c='OJ49'
#c='OJ248'
#c='OJ287'
#c='S4_0954+65'
#c='ON231'
#c='Mkn421'
#c='Mkn501'
#c='3C454-3'
#c='3C371'
#c='PKS0735+17'
#c='PKS2155-304'
#c='L-Lacertae'
#c='AO0235+16'
#c='ES2344+514'

year=`echo $a|cut -c-4`
month=`echo $a|cut -c5-6`
ym=`echo $year'-'$month`

last_date=`cat gasp_target_fitsheader_info_exclude_baddata_join.txt | grep $ym|tail -1| cut -d "|" -f2| cut -d - -f3`

d1=$a'01'
d2=$a$last_date

for i in $c;do python Rmag_aperture_annulus_r_file_median_w1_subplot_date_target.py $d1 $d2 $i | tee 'Rmag_aperture_annulus_r_file_median_w1_subplot_'$d1'-'$d2'_'$i'.log';done
