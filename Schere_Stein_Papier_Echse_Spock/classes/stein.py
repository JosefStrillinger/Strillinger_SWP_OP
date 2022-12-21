from classes.game_item import Game_Item

class Stein(Game_Item):
    
    def __init__(self):
        self.name = "Stein"
        self.relation = {"Schere" : 1, "Stein" : 0, "Papier" : -1, "Echse" : 1, "Spock" : -1}