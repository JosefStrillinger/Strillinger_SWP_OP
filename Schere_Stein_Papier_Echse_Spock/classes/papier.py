from classes import game_item

class Papier(game_item.Game_Item):
    
    def __init__(self):
        self.name = "Papier"
        self.relation = {"Schere" : -1, "Stein" : 1, "Papier" : 0, "Echse" : -1, "Spock" : 1}