import json
import Item

json_paths = {
    "coca_cola_can": "json/coca_cola_can.json",
}

items = []


def parse(file_name):
    file = open(file_name,'r')
    raw_data = file.read()
    json_data = json.loads(raw_data)
    item = Item(json_data['name'], json_data['description'], json_data['value']) 
    file.close()
    print("Loaded data from",file_name) #temp
    return item


def load():
    for val in json_paths.values():
        items.append(parse(json_paths[val]))