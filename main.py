import json
from item.Item import Item
from item.Item import json_paths
from tkinter import *

items = []


def parse(file_name):
    try:
        file = open(file_name,'r')
    except:
        print("File {} is not found".format(file_name))
        return None
    raw_data = file.read()
    json_data = json.dumps(raw_data)
    ret = Item(json_data['name'], json_data['description'], json_data['rarity']) 
    file.close()
    print("Loaded data from",file_name) #temp
    return ret


def load_items():
    for val in json_paths.values():
        item = parse(val)
        if not item == None:
            items.append(item)

def start():
    load_items()

def main():
    #make the rendering in this file or another one if you want
    # also pls replace the print text with like on screen stuff
    print("Press enter to start!") # you can replace enter with a butto
    input("")
    start()
    


if __name__ == "__main__":
    main()

