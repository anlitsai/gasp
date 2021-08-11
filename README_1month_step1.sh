#a='202003'
a=$1
for i in $a;do
  echo "python slt_calibration_master_bias_1month_180S.py $i | tee slt_calibration_master_bias_1month_180S_$i.log"
  python slt_calibration_master_bias_1month_180S.py $i | tee slt_calibration_master_bias_1month_180S_$i.log
  echo "python slt_calibration_master_dark_1month_180S.py $i | tee slt_calibration_master_dark_1month_180S_$i.log"
  python slt_calibration_master_dark_1month_180S.py $i | tee slt_calibration_master_dark_1month_180S_$i.log
  echo "python slt_calibration_master_flat_1month_180S.py $i | tee slt_calibration_master_flat_1month_180S_$i.log"
  python slt_calibration_master_flat_1month_180S.py $i | tee slt_calibration_master_flat_1month_180S_$i.log
done



