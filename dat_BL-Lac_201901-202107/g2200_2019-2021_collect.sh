a=`find ../Rmag_InstMag/annu_w1_2021*|grep g2200`
cat $a > g2200_2021.dat

cat g2200_2019.dat g2200_2020.dat g2200_2021.dat > g2200_2019-2021.dat
