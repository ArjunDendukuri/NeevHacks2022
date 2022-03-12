import json
from item.Item import Item

json_paths = {
    "coca_cola_can": "json/coca_cola_can.json",
}

items = []


def parse(file_name:str)-> Item | None:
    try:
        file = open(file_name,'r')
    except:
        print("File {} is not found".format(file_name))
        return None
    raw_data = file.read()
    json_data = json.loads(raw_data)
    item = item.Item(json_data['name'], json_data['description'], json_data['value']) 
    file.close()
    print("Loaded data from",file_name) #temp
    return item


def load_items():
    for val in json_paths.values():
        item = parse(val)
        if not item == None:
            items.append(item)