from classes.game_item import Game_Item

class Echse(Game_Item):
    
    def __init__(self):
        self.name = "Echse"
        self.relation = {"Schere" : -1, "Stein" : -1, "Papier" : 1, "Echse" : 0, "Spock" : 1}