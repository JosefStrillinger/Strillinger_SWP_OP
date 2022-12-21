from classes.game_item import Game_Item

class Papier(Game_Item):
    
    def __init__(self):
        self.name = "Papier"
        self.relation = {"Schere" : -1, "Stein" : 1, "Papier" : 0, "Echse" : -1, "Spock" : 1}