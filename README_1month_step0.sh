#a='202003'
a=$1

#step0
python search_no_wcs.py $a
# upload no_wcs_files to ycc and modify them

b='wcsfixed_'$a
cd $b
ln -s ../cp_wcsfixed_file.sh ./
./cp_wcsfixed_file.sh

