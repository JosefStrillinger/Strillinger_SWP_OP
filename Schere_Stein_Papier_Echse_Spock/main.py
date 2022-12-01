# TODO: make something decent

import json
import random

class Command(): # look into it
    def __init__(self, id, method, description, command):
        self.id = id
        self.method = method
        self.description = description
        self.command = command
    
    def run_cmd(self):
        self.method
        
    def __str__(self):
        print("Description: {0} \nCommand: {1}\n".format(self.description, self.command))
        
class Command_Manager():
    def __init__(self):
        self.commands = []
        
    def run_cmd(self, cmd):
        if len(cmd) > 0:
            pass
         
    def add_cmd(self, cmd):
        cmd.id = len(self.commands)
        self.commands.append(cmd)

class SSPES_Game:
    def __init__(self):
        self.init()
        
    def init(self):
        pass
        
    def start(self):
        self.play()
        
    def play(self):
        playing = True
        test = ["Schere", "Stein", "Papier", "Echse", "Spock"]
        while(playing):          
            a = input("Input a number of your choosing (1-5): ")
            obj = self.input_handler(a)
            #print(obj.get_name)

            res = obj.get_relation(random.choice(test))
            print(self.check_result(res))
            self.print_game_stats()
        
        
    def input_handler(self, input_player): 
        match int(input_player):
            case 1:
                stats["Schere"] += 1
                return Schere()
            case 2:
                stats["Stein"] += 1
                return Stein()
            case 3:
                stats["Papier"] += 1
                return Papier()
            case 4:
                stats["Echse"] += 1
                return Echse()
            case 5:
                stats["Spock"] += 1
                return Spock()
            case other:
                return Game_Item()
                
    def check_result(self, outcome):
        match outcome:
            case -1:
                stats["loss"] += 1
                #save_event(1, "lose")
                return "You lost!"
            case 0:
                stats["draw"] += 1
                #save_event(1, "draw")
                return "It's a draw!"
            case 1:
                stats["win"] += 1
                #save_event(1, "win")
                return "You won!"

    def print_game_stats():
        print(stats)

    def print_game_help():
        pass
    
    def set_difficulty():
        pass                            
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
                
class Schere(Game_Item):
    
    def __init__(self):
        self.name = "Schere"
        self.relation = {"Schere" : 0, "Stein" : -1, "Papier" : 1, "Echse" : 1, "Spock" : -1}
        
class Stein(Game_Item):
    
    def __init__(self):
        self.name = "Stein"
        self.relation = {"Schere" : 1, "Stein" : 0, "Papier" : -1, "Echse" : 1, "Spock" : -1}

class Papier(Game_Item):
    
    def __init__(self):
        self.name = "Papier"
        self.relation = {"Schere" : -1, "Stein" : 1, "Papier" : 0, "Echse" : -1, "Spock" : 1}
     
class Echse(Game_Item):
    
    def __init__(self):
        self.name = "Echse"
        self.relation = {"Schere" : -1, "Stein" : -1, "Papier" : 1, "Echse" : 0, "Spock" : 1}
        
class Spock(Game_Item):
    
    def __init__(self):
        self.name = "Spock"
        self.relation = {"Schere" : 1, "Stein" : 1, "Papier" : -1, "Echse" : -1, "Spock" : 0}
        
#Dictionary einbauern

def create_computer_options():
    return ["Schere", "Stein", "Papier", "Echse", "Spock"]

def create_game():
    pass

def save_event(user_id, event):
    with open("save.txt", "r") as rd:
        events = json.load(rd)
        
    events[user_id][event] +=1
    
    with open("save.txt", "w") as wd:
        wd.write(json.dumps(events))
          
def create_statistic():
    return {"Schere" : 0, "Stein" : 0, "Papier" : 0, "Echse" : 0, "Spock" : 0, "win":0, "draw" : 0, "loss": 0}

def main():
    #dict = create_dict()
    game = SSPES_Game()
    game.start()

if __name__ == "__main__":
    stats = create_statistic()
    main()