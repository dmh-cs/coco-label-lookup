./src/extract_image_label_info.sh $1
./src/extract_category_info.sh $1
./src/extract_captions.sh $2
python src/create_image_label_lookup.py $3
