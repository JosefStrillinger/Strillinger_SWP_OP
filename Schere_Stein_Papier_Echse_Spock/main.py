# TODO: make something decent
import json
import random
from enum import Enum
from classes import game_item, schere, stein, papier, echse, spock

class Difficulty(Enum):
    normal = 1
    hard = 2
    impossible = 3

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
        self.difficulty = Difficulty.normal
        
    def start(self):
        self.set_difficulty()
        self.play()
        
    def play(self):
        playing = True
        test = ["Schere", "Stein", "Papier", "Echse", "Spock"]
        while(playing):          
            a = input("Input a number of your choosing (1-5): ")
            self.command_input_handler(a)
                 
            while not a.isnumeric() and int(a) not in range(1, 5+1):
                print("Please enter a valid number")
                a = input("Input a number of your choosing (1-5): ")
            obj = self.play_input_handler(a)

            if self.difficulty == Difficulty.normal:
                comp_turn = random.choice(test)
                print("Computer: " + comp_turn)
                res = obj.get_relation(comp_turn)
                print(self.check_result(res))
                print(self.print_game_stats())
            
            if self.difficulty == Difficulty.hard:
                pass
            
            if self.difficulty == Difficulty.impossible:
                pass        
          
    #possible changes:
    # add object to constructor, change ctor to (self, input_player, player_obj)          
    # change case to return player_obj = schere.Schere()
    # then other cases can be added
    
    def command_input_handler(self, input_command):
        match str(input_command):
            case "exit":
                self.end_game()
            case "restart":
                self.start()
                
    def play_input_handler(self, input_player): 
        match int(input_player):
            case 1:
                stats["Schere"] += 1
                save_player_event("Schere")
                print("Player: Schere")
                return schere.Schere()
            case 2:
                stats["Stein"] += 1
                save_player_event("Stein")
                print("Player: Stein")
                return stein.Stein()
            case 3:
                stats["Papier"] += 1
                save_player_event("Papier")
                print("Player: Papier")
                return papier.Papier()
            case 4:
                stats["Echse"] += 1
                save_player_event("Echse")
                print("Player: Echse")
                return echse.Echse()
            case 5:
                stats["Spock"] += 1
                save_player_event("Spock")
                print("Player: Spock")
                return spock.Spock()
                
    def check_result(self, outcome):
        match outcome:
            case -1:
                stats["loss"] += 1
                save_player_event("loss")
                return "You lost!"
            case 0:
                stats["draw"] += 1
                save_player_event("draw")
                return "It's a draw!"
            case 1:
                stats["win"] += 1
                save_player_event("win")
                return "You won!"

    def print_game_stats(self):
        return stats

    def print_game_help():
        pass
    
    def set_difficulty(self):
        valid_inputs = ["normal", "hard", "impossible"]
        di = input("Enter Difficulty (normal, hard or impossible): ")
        while str(di) not in valid_inputs:
            print("Please enter a valid Difficulty")
            di = input("Enter Difficulty (normal, hard or impossible): ")          
        self.difficulty_input(di)
        print(self.difficulty)       
        
    def difficulty_input(self, diff_in):
        match str(diff_in):
            case "normal":
                self.difficulty = Difficulty.normal
                return
            case "hard":
                self.difficulty = Difficulty.hard
                return
            case "impossible":
                self.difficulty = Difficulty.impossible
                return
    
    def end_game(self):
        print("Thank you for playing")
        exit()
            
        
                   

def create_computer_options():
    return ["Schere", "Stein", "Papier", "Echse", "Spock"]

def save_player_event(event):
    with open("player_save.txt", "r") as rd:
        saves = json.load(rd)
        
    saves["player"][event] +=1
    
    with open("player_save.txt", "w") as wd:
        wd.write(json.dumps(saves))
          
def create_statistic():
    return {"Schere" : 0, "Stein" : 0, "Papier" : 0, "Echse" : 0, "Spock" : 0, "win":0, "draw" : 0, "loss": 0}

def main():
    game = SSPES_Game()
    game.start()
    #with open("player_save.txt", "r") as wd:
    #    saves = json.load(wd)
        
    #print(saves["player"]["loss"])

if __name__ == "__main__":
    stats = create_statistic()
    stats2 = {"player":{"Schere" : 0, "Stein" : 0, "Papier" : 0, "Echse" : 0, "Spock" : 0, "win":0, "draw" : 0, "loss": 0}}
    main()