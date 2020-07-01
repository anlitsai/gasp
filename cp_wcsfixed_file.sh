a=`ls |grep new`;for i in $a;do b=`echo $i|cut -d . -f1`; cp $i $b.fts; c=`echo $b| cut -d "@" -f1|rev|cut -d - -f1|rev`;d=`echo $c|cut -c1-6`;echo "cp $b.fts ../$d/slt$c/wchen/wchen_03_GASP_01/"; cp $b.fts ../$d/slt$c/wchen/wchen_03_GASP_01/; done

