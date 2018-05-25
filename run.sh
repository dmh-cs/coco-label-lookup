./src/extract_image_label_info.sh $1
./src/extract_category_info.sh $1
python src/create_image_label_lookup.py $2
