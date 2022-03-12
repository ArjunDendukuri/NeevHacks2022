import json
from item.Item import Item
from item.Item import json_paths
from tkinter import *
import os
from GUI.FullGUI import tk_run

items = []


def parse(file_name):
    scr_name = os.path.dirname(__file__)
    name = scr_name + "\\" + file_name
    try:
        with open(name, 'r') as f:
            data = json.load(f)
            raw_data = f.read()
            json_data = json.load(raw_data)
            ret = Item(json_data['name'], json_data['description'], json_data['rarity']) 
            f.close()
            print("Loaded data from",file_name) #temp
            return ret
    except:
        return None


def load_items():
    for val in json_paths.values():
        item = parse(val)
        if not item == None:
            items.append(item)
        else:
            print("Error loading item",val)

def start():
    load_items()

def main():
    #make the rendering in this file or another one if you want
    # also pls replace the print text with like on screen stuff
    tk_run()
    print("Press enter to start!") # you can replace enter with a butto
    input("")
    start()
    


if __name__ == "__main__":
    main()

