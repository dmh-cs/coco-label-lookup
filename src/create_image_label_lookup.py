import sys
import json

def get_category_lookup(category_info_path):
  lookup = {}
  with open(category_info_path) as f:
    while True:
      line = f.readline()
      if line == '': break
      category = json.loads(line)
      lookup[category['id']] = category['name']
  return lookup

def main():
  category_info_path = 'datasets/category_info.json'
  category_lookup = get_category_lookup(category_info_path)
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
  with open('out/' + sys.argv[1], 'w') as f:
    f.write(json.dumps(image_label_lookup, sort_keys=True, indent=4))

if __name__ == "__main__": main()
