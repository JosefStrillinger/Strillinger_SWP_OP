from classes import game_item

class Schere(game_item.Game_Item):
    
    def __init__(self):
        self.name = "Schere"
        self.relation = {"Schere" : 0, "Stein" : -1, "Papier" : 1, "Echse" : 1, "Spock" : -1}