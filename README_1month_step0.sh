#a='202003'
folder=$1

#step0
python search_no_wcs.py $folder
# upload no_wcs_files to ycc and modify them

./no_wcs_dir.sh $folder

#./ycc_upload.sh $folder


dir='wcsfixed_'$folder
mkdir -p $dir
cd $dir

search_file='search_no_wcs_$folder.txt'

a=`cat $search_file|grep fts|cut -d / -f2-9`

ln -s ../cp_wcsfixed_file.sh ./
./cp_wcsfixed_file.sh

