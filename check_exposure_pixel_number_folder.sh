folder=$1
file='check_exposure_pixel_'$folder'.txt'
echo "-------------"
echo "GASP 1024"
cat $file|grep GASP|grep 180S|cut -f2|grep 1024|wc -l
echo "bias 1024"
cat $file|grep bias|cut -f2|grep 1024|wc -l
echo "dark 1024"
cat $file|grep dark|cut -f2|grep 1024|wc -l
echo "flat 1024"
cat $file|grep flat|cut -f2|grep 1024|wc -l
echo "-------------"
echo "GASP 2048"
cat $file|grep GASP|grep 180S|cut -f2|grep 2048|wc -l
echo "bias 2048"
cat $file|grep bias|cut -f2|grep 2048|wc -l
echo "dark 2048"
cat $file|grep dark|cut -f2|grep 2048|wc -l
echo "flat 2048"
cat $file|grep flat|cut -f2|grep 2048|wc -l
