# TODO: make something decent
import json
import random
from classes import game_item, schere, stein, papier, echse, spock

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
            print(self.print_game_stats())          
          
    #possible changes:
    # add object to constructor, change ctor to (self, input_player, player_obj)          
    # change case to return player_obj = schere.Schere()
    # then other cases can be added
     
    def input_handler(self, input_player): 
        match int(input_player):
            case 1:
                stats["Schere"] += 1
                return schere.Schere()
            case 2:
                stats["Stein"] += 1
                return stein.Stein()
            case 3:
                stats["Papier"] += 1
                return papier.Papier()
            case 4:
                stats["Echse"] += 1
                return echse.Echse()
            case 5:
                stats["Spock"] += 1
                return spock.Spock()
            case other:
                return schere.Schere()
                
    def check_result(self, outcome):
        match outcome:
            case -1:
                stats["loss"] += 1
                #save_event(0, "lose")
                return "You lost!"
            case 0:
                stats["draw"] += 1
                #save_event(0, "draw")
                return "It's a draw!"
            case 1:
                #stats["win"] += 1
                save_event(0, "win")
                return "You won!"

    def print_game_stats(self):
        return stats

    def print_game_help():
        pass
    
    def set_difficulty():
        pass                            

def create_computer_options():
    return ["Schere", "Stein", "Papier", "Echse", "Spock"]

def save_event(user_id, event):
    with open("save.txt", "r") as rd:
        saves = json.load(rd)
        
    saves[user_id][event] +=1
    
    with open("save.txt", "w") as wd:
        wd.write(json.dumps(saves))
          
def create_statistic():
    return {"Schere" : 0, "Stein" : 0, "Papier" : 0, "Echse" : 0, "Spock" : 0, "win":0, "draw" : 0, "loss": 0}

def main():
    game = SSPES_Game()
    game.start()

if __name__ == "__main__":
    stats = create_statistic()
    main()