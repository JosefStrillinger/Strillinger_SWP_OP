import json

class Player:
    def __init__(self, name):
        self.name = name
    
    def set_name(self, changed_name):
        self.name = changed_name
        
    def get_name(self):
        return self.name
    
    def init_player(self):
        with open("player_save.txt", "r") as save_r:
            player_save = json.load(save_r)
        
        if self.name not in player_save:
            player_save[self.name] = {"Schere" : 0, "Stein" : 0, "Papier" : 0, "Echse" : 0, "Spock" : 0, "win":0, "draw" : 0, "loss": 0}
            with open("player_save.txt", "w") as save_w:
                save_w.write(json.dumps(player_save))