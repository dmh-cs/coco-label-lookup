cat $1 | jq -c '.categories []' > datasets/category_info.json
