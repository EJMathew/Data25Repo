import json
#json.dumps (serialises to string)
#json.dump (writes to a json file)

# car_data = {'name': 'tesla', 'engine': 'electric'}
# car_data_json_string = json.dumps(car_data)

with open('new_json_file.json') as jsonfile:
    car = json.load(jsonfile)
    print(car['name'])
    print(car['engine'])