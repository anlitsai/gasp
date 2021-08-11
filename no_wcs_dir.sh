
folder=$1
echo $folder
a=`cat ./data/search_no_wcs_$folder.txt|grep fts|cut -d " " -f2`;
echo $a
 
rm -rf ./data/no_wcs_$folder;
mkdir -p ./data/no_wcs_$folder;
cp $a ./data/no_wcs_$folder;

echo "generate search_no_wcs_$folder.txt"

