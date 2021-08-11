echo "wchen123"
month=`pwd| cut -d / -f6`
rsync -av wchen@140.115.34.99:lulin_data/slt$month* ./
