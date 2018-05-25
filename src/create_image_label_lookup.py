import sys
import json
import pydash as _

def get_category_lookup(category_info_path):
  lookup = {}
  with open(category_info_path) as f:
    while True:
      line = f.readline()
      if line == '': break
      category = json.loads(line)
      lookup[category['id']] = category['name']
  return lookup

def get_caption_lookup(captions_path):
  lookup = {}
  with open(captions_path) as f:
    while True:
      line = f.readline()
      if line == '': break
      image = json.loads(line)
      lookup[image['image_id']] = image['caption']
  return lookup

def main():
  category_info_path = 'datasets/category_info.json'
  category_lookup = get_category_lookup(category_info_path)
  captions_path = 'datasets/captions.json'
  caption_lookup = get_caption_lookup(captions_path)
  image_label_lookup = {}
  with open('datasets/image_label_info.json') as f:
    while True:
      line = f.readline()
      if line == '': break
      image = json.loads(line)
      if image_label_lookup.get(image['image_id']):
        image_label_lookup[image['image_id']].append(category_lookup[image['category_id']])
      else:
        image_label_lookup[image['image_id']] = [category_lookup[image['category_id']]]
  image_label_lookup = _.objects.map_values(image_label_lookup, _.arrays.uniq)
  image_lookup = _.objects.map_values(image_label_lookup, lambda val, key: {'labels': val,
                                                                            'caption': caption_lookup.get(key)})
  with open('out/' + sys.argv[1], 'w') as f:
    f.write(json.dumps(image_lookup, sort_keys=True, indent=4))

if __name__ == "__main__": main()
