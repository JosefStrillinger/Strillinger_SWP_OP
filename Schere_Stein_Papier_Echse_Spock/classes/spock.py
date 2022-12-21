from classes.game_item import Game_Item

class Spock(Game_Item):
    
    def __init__(self):
        self.name = "Spock"
        self.relation = {"Schere" : 1, "Stein" : 1, "Papier" : -1, "Echse" : -1, "Spock" : 0}