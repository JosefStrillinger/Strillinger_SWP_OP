class Game_Item():
    
    def __init__(self):
        self.name = "game"
        self.relation = {"Schere" : 0, "Stein" : 0, "Papier" : 0, "Echse" : 0, "Spock" : 0}
    
    def get_relation(self, item2):
        return self.relation[item2]
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return str(self.name)