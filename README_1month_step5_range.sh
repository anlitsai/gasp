#a='202003'
#a=$1


c=`cat check_science_target_list.txt`
#c='3C279'
#c='4C29-45'
#c='4C71-07'
#c='DA406'
#c='Mkn501'
#c='Mkn421'
#c='OJ49'
#c='OJ248'
#c='ON231'
#c='S4_0954+65'
#c='L-Lacertae'

#year=`echo $a|cut -c-4`
#month=`echo $a|cut -c5-6`
#ym=`echo $year'-'$month`

#last_date=`cat gasp_target_fitsheader_info_exclude_baddata_join.txt | grep $ym|tail -1| cut -d "|" -f2| cut -d - -f3`

#d1=$a'01'
#d2=$a$last_date

#d1='20200501'
#d2='20200930'
#d1='20200101'
#d2='20201231'
#d1='20200801'
#d2='20201231'
#d1='20170101'
#d2='20191130'
d1='20210301'
d2='20210730'

for i in $c;do python Rmag_aperture_annulus_r_file_median_w1_subplot_date_target.py $d1 $d2 $i | tee 'Rmag_aperture_annulus_r_file_median_w1_subplot_'$d1'-'$d2'_'$i'.log';done


