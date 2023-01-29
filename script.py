import json

MULTIPLY = 0
ADD = 1
MINUS = 2
DIVIDE = 3

PATH_ORIGINAL = 'data/fkwwi/worldgen/noise_settings/islands_medium.json'
PATH_NEW_CONFIG = 'islands_medium.json'


path = PATH_ORIGINAL


with open(path, 'r') as f:
  data = json.load(f)
f.close()

def recurse(data, find):
  if isinstance(data, list):
    for elem in data:
      recurse(elem, find)
  elif isinstance(data, dict):
    if find in data:
        diff = data['max_threshold'] - data['min_threshold']
        new_diff = diff/2
        if data['min_threshold'] + new_diff == 0:
          data['min_threshold'] = 0
        else:
          data['min_threshold'] = data['min_threshold'] + new_diff + 1

    for k, v in data.items():
      recurse(v, find)

#continentalness_coeff = 0.0001
#action = MULTIPLY
#param = 'continentalness'
#generator = data['generator']
#biome_source = generator['biome_source']
#biomes = biome_source['biomes']

#for biome in biomes:
#  biome_params = biome['parameters']
#  biome_continentalness = biome_params[param]
#  new_biome_cont = []
#  for biom_cont_val in biome_continentalness:
#    if action == MULTIPLY:
#      new_biome_cont.append(float(biom_cont_val) * continentalness_coeff)
#    elif action == ADD:
#      new_biome_cont.append(float(biom_cont_val) + continentalness_coeff)
#    elif action == MINUS:
#      new_biome_cont.append(float(biom_cont_val) - continentalness_coeff)
#    else:
#      new_biome_cont.append(float(biom_cont_val) / continentalness_coeff)
#  
#  biome_params[param]=(new_biome_cont)

#print(biomes)

recurse(data, 'min_threshold')

with open("islands_medium.json", "w") as jsonFile:
    json.dump(data, jsonFile)

jsonFile.close()