cat $1 | jq -c '.annotations []' > datasets/captions.json
