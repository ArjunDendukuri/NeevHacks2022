import JsonParser


class Item():

    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

    def __repr__(self):
        return self.name

    def get_path(self): 
        return JsonParser.json_paths[self.name]