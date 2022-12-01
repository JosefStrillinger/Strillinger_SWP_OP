from classes import game_item

class Echse(game_item.Game_Item):
    
    def __init__(self):
        self.name = "Echse"
        self.relation = {"Schere" : -1, "Stein" : -1, "Papier" : 1, "Echse" : 0, "Spock" : 1}