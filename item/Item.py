import JsonParser
from Rarity import Rarity


class Item():

    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = Rarity[rarity]

    def __str__(self):
        file = open(self.get_path(), 'r')
        ret = file.read()
        file.close()
        return ret

    def __repr__(self):
        return self.name

    def get_path(self): 
        return JsonParser.json_paths[self.name]