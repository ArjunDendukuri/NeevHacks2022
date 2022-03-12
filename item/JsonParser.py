import json
import Item

json_paths = {
    "coca_cola_can": "item/json/coca_cola_can.json",
}


def parse(file_name):
    file = open(file_name,'r')
    raw_data = file.read()
    json_data = json.loads(raw_data)
    item = Item(json_data['name'], json_data['description'], json_data['value']) 
    file.close()

    return item
