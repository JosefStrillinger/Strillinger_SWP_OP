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
        comp_options = create_computer_options()
        while(playing):          
            a = input("Input a number of your choosing (1-5): ")
            self.command_input_handler(a)
                 
            while not a.isnumeric() or int(a) not in range(1, 5+1):
                self.command_input_handler(a)
                print("Please enter a valid number")
                a = input("Input a number of your choosing (1-5): ")
                
            obj = self.play_input_handler(a)
            print(obj.get_weak_to())
            player_percent_stats = get_statistic_percentage(get_plays_statistic("player"))
            
            if self.difficulty == Difficulty.normal:
                comp_turn = random.choice(comp_options)
                print("Computer: " + comp_turn)
                res = obj.get_relation(comp_turn)
                print(self.check_result(res))
                print(self.print_game_stats())
            
            if self.difficulty == Difficulty.hard:
                most_used_player_turn = max(player_percent_stats)
                comp_turns_possible = self.get_comp_options(most_used_player_turn)
                print(comp_turns_possible)
                comp_turn = random.choice(comp_turns_possible)
                print("Computer: " + comp_turn)
                res = obj.get_relation(comp_turn)
                print(self.check_result(res))
                print(self.print_game_stats())
                
            if self.difficulty == Difficulty.impossible:
                comp_turns_possible = obj.get_weak_to()
                comp_turn = random.choice(comp_turns_possible)
                print("Computer: " + comp_turn)
                res = obj.get_relation(comp_turn)
                print(self.check_result(res))
                print(self.print_game_stats())      
          
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
                save_player_event("player", "Schere")
                print("Player: Schere")
                return schere.Schere()
            case 2:
                stats["Stein"] += 1
                save_player_event("player", "Stein")
                print("Player: Stein")
                return stein.Stein()
            case 3:
                stats["Papier"] += 1
                save_player_event("player", "Papier")
                print("Player: Papier")
                return papier.Papier()
            case 4:
                stats["Echse"] += 1
                save_player_event("player", "Echse")
                print("Player: Echse")
                return echse.Echse()
            case 5:
                stats["Spock"] += 1
                save_player_event("player","Spock")
                print("Player: Spock")
                return spock.Spock()
    
    def get_comp_options(self, input_comp):
        match str(input_comp):
            case "Schere":           
                help_obj = schere.Schere()  
                print(help_obj.get_weak_to())
                return help_obj.get_weak_to()
            case "Stein":
                help_obj = stein.Stein()
                print(help_obj.get_weak_to())
                return help_obj.get_weak_to()
            case "Papier":
                help_obj = papier.Papier()
                print(help_obj.get_weak_to())
                return help_obj.get_weak_to()
            case "Echse":
                help_obj = echse.Echse()
                print(help_obj.get_weak_to())
                return help_obj.get_weak_to()
            case "Spock":
                help_obj = spock.Spock()
                print(help_obj.get_weak_to())
                return help_obj.get_weak_to()
         
    def check_result(self, outcome):
        match outcome:
            case -1:
                stats["loss"] += 1
                save_player_event("player","loss")
                return "You lost!"
            case 0:
                stats["draw"] += 1
                save_player_event("player", "draw")
                return "It's a draw!"
            case 1:
                stats["win"] += 1
                save_player_event("player", "win")
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
            
        
def get_plays_statistic(name):
    with open("player_save.txt", "r") as rd:
        saves = json.load(rd)     
    return saves[name]

def get_statistic_percentage(stat):
    needed_dict = {"Schere": 0, "Stein": 0, "Papier": 0, "Echse": 0, "Spock": 0}
    for i in stat.keys():
        if i in needed_dict.keys():
            needed_dict[i] = stat[i]
    
    plays = sum(needed_dict.values())
    
    percentages = []
    for j in needed_dict.values():
        percentages.append(j/plays*100)
        
    dict_with_percentages = {"Schere": 0, "Stein": 0, "Papier": 0, "Echse": 0, "Spock": 0}
    
    x = 0
    for i in needed_dict:
        print(i+": "+str(round(percentages[x], 5))+" % " + str(needed_dict[i])+" mal")
        dict_with_percentages[i] = percentages[x]
        x += 1
        
    return dict_with_percentages

def create_computer_options():
    return ["Schere", "Stein", "Papier", "Echse", "Spock"]

def save_player_event(name, event):
    name = "player"
    with open("player_save.txt", "r") as rd:
        saves = json.load(rd)
        
    saves[name][event] +=1
    
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
    main()