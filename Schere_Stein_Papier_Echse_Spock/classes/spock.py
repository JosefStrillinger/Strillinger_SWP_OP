from classes import game_item

class Spock(game_item.Game_Item):
    
    def __init__(self):
        self.name = "Spock"
        self.relation = {"Schere" : 1, "Stein" : 1, "Papier" : -1, "Echse" : -1, "Spock" : 0}