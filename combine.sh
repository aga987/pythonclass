#add header to chromosome data
echo "starting combaning script"
for file in human_chr*.txt
do
	echo '$file'
	echo "$file"
	cat raw/header.txt $file > processed/&file
done
echo "Switching into new directory"
cd processed
for input in *.txt
do 
	echo "Analysizing $input ..."
	python ../pseudocode.py $input
done
echo "Done!"
