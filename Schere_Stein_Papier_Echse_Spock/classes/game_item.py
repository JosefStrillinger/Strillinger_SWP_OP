class Game_Item():
    
    def __init__(self):
        self.name = "game"
        self.relation = {"Schere" : 0, "Stein" : 0, "Papier" : 0, "Echse" : 0, "Spock" : 0}
    
    def get_relation(self, item2):
        return self.relation[item2]
    
    def get_name(self):
        return self.name
    
    def get_weak_to(self):
        keys = [k for k, v in self.relation.items() if v == -1] # Find the error here, doesnt return the items with values == -1
        #keys = [i for i in self.relation if self.relation[i] == -1] # oder das
        #print(keys)
        return keys
    
    def __str__(self):
        return str(self.name)