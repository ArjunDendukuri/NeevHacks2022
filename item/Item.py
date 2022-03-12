from item.Rarity import Rarity
import random

json_paths = {
    "can": "can.json",
    "captain_kidd_coin":"captain_kidd_coin.json",
    "glass_bottles":"glass_bottles.json",
    "cigarretes":"cigarretes.json",
    "wrappers":"wrappers.json",
    "single_use_cutlery":"single_use_cutlery.json",
    "plastic_bag":"plastic_bag.json",
    "plastic_bottle":"plastic_bottle.json",
    "footwear":"footwear.json",
    "bottle_cap":"bottle_cap.json"
}

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
        return json_paths[self.name]

stats = ["Pollution is one of the biggest global killers, affecting over 100 million people. That's comparable to global diseases like malaria and HIV.",
"In 1975, the National Academy of Sciences estimated that ocean-based sources, such as cargo ships and cruise liners had dumped 14 billion pounds of garbage into the ocean",
"Over 1 million seabirds and 100,000 sea mammals are killed by pollution every year.",
"People who live in places with high levels of air pollutants have a 20% higher risk of death from lung cancer than people who live in less-polluted areas.",
"Approximately 40% of the lakes in America are too polluted for fishing, aquatic life, or swimming.",
"Each year 1.2 trillion gallons of untreated sewage, stormwater, and industrial waste are dumped into US water.",
"Recycling and composting prevented 85 million tons of material away from being disposed of in 2010, up from 18 million tons in 1980."]

stat = random.choice(stats)
print(stat)