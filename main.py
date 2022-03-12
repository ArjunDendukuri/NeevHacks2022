import json
from item.Item import Item
from item.Item import json_paths
from tkinter import *
import os
from GUI.FullGUI import tk_run

items = []


def parse(file_name):
    scr_name = os.path.dirname(__file__)
    name = scr_name + "\item\json\\" + file_name
    print(name)
    try:
        with open(name, 'r') as f:
            json_data = json.load(f) 
            ret = Item(json_data['name'], json_data['description'], json_data['rarity']) #error here
            f.close()
            print("Loaded data from",file_name) #temp
            return ret
    except FileNotFoundError:
        return None


def load_items():
    for val in json_paths.values():
        item = parse(val)
        if not item == None:
            items.append(item)
        else:
            print("Error loading item",val)

def start():
    pass

def main():
    #make the rendering in this file or another one if you want
    # also pls replace the print text with like on screen stuff
    load_items()
    tk_run()
    


if __name__ == "__main__":
    main()

