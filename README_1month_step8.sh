# generate NCU Lulin Observation target list

date=`cat gasp_target_fitsheader_info_exclude_baddata_join.txt|tail -1|cut -d"|" -f2|sed 's/-//g'`
file=NCU_gasp_daily_target_until_$date.txt

echo "YYYY-MM-DD       JulianDate          Filter  Target" > $file
#sed 's/|/\t/g' gasp_target_fitsheader_info_exclude_baddata_join.txt |awk -F"\t" '{printf "%-16s %-19.5f %-12s %-12s\n", $2,$13,$12,$5}'|sed 's/_Astrodon_2018//'|sed 's/_30508//'   |tail -n +2 >> $file
sed 's/|/\t/g' gasp_target_fitsheader_info_exclude_baddata_join.txt |awk -F"\t" '{printf "%-16s %-19.5f %-12s %-12s\n", $2,$13,$12,$5}'|sed 's/_Astrodon_2018//'|sed 's/_30508//' |sed 's/R\ \ \ \ \ \ /R\ /' | sed 's/R\ /R\ \ \ \ \ \ \ /' |sed 's/V\ /V\ \ \ \ \ \ \ /' |sed 's/PKS/KS/'| sed 's/KS/PKS/'| sed 's/BL-L/L-L/'|sed 's/L-L/BL-L/'  |tail -n +2 >> $file

echo ""
echo "...... output file: $file ......"
echo ""

