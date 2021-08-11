folder=$1

python search_no_wcs.py $folder
./no_wcs_dir.sh $folder
./ycc_upload.sh $folder
