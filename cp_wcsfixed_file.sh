#month=`pwd|cut -d / -f5|cut -d _ -f2`
month=`pwd|cut -d / -f6|cut -d _ -f2`
echo $month

#pathfile=`cat ../data/search_no_wcs_$month.txt |grep slt|cut -d / -f2-5`
pathfile=`cat ../search_no_wcs_$month.txt |grep slt|cut -d / -f2-6`
echo $pathfile

a=`ls |grep new`;for i in $a;do b=`echo $i|cut -d . -f1`; cp -f $i $b.fts;c=`find ../$month|grep $b|cut -d / -f1-5`;echo "cp -f $b.fts $c"; cp $b.fts $c; done
#a=`ls |grep new`;for i in $a;do b=`echo $i|cut -d . -f1`; echo $i $b.fts;c=`find ../$month|grep $b|cut -d / -f1-5`;echo "cp -f $b.fts $c"; echo $b.fts $c; done

