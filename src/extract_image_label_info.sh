cat $1 | jq -c '.annotations [] | {image_id: .image_id, category_id: .category_id}' > datasets/image_label_info.json
