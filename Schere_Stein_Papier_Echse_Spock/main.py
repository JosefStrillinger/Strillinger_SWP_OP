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
        self.player = "player"
        self.play_statistic = self.create_statistic()
        
    def start(self):
        self.game_menu()
        
    def play(self):
        playing = True
        comp_options = self.create_computer_options()
        while(playing):          
            a = input("Input a number of your choosing (1-5): ")
            if str(a).lower() == "-m":
                self.input_menu_command()
                 
            while not a.isnumeric() or int(a) not in range(1, 5+1):
                if str(a).lower() == "-m":
                    self.input_menu_command()
                print("Please enter a valid number")
                a = input("Input a number of your choosing (1-5): ")
                
            obj = self.play_input_handler(a)
            print(obj.get_weak_to())
            player_percent_stats = self.get_statistic_percentage(self.get_plays_statistic(self.player))
            
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
    
    def game_menu(self):
        print("Welcome the SSPES - Game developed by Josef Strillinger")
        self.get_commands()
        self.input_menu_command()
    
    def get_commands(self):
        print("----------------------------------------------------------")
        print("Commands: ")
        print("End Game: \t\t-e")
        print("Restart: \t\t-r")
        print("Play Game: \t\t-p")
        print("Change Player: \t\t-pl")
        print("Change Difficulty: \t-d")
        print("----------------------------------------------------------")
           
    def input_menu_command(self):
        start_input = input("Please input a command: ")
        self.command_input_handler(start_input)
    
    def command_input_handler(self, input_command):
        match str(input_command).lower():
            case "-e":
                self.end_game()
            case "-r":
                self.start()
            case "-p":
                self.play()
            case "-pl":
                self.input_player()
                self.input_menu_command()
            case "-d":
                self.input_difficulty()
                self.input_menu_command()
            case other:
                self.input_menu_command()
                
    def play_input_handler(self, input_player): 
        match int(input_player):
            case 1:
                self.play_statistic["Schere"] += 1
                self.save_player_event(self.player, "Schere")
                print("Player: Schere")
                return schere.Schere()
            case 2:
                self.play_statisticats["Stein"] += 1
                self.save_player_event(self.player, "Stein")
                print("Player: Stein")
                return stein.Stein()
            case 3:
                self.play_statistic["Papier"] += 1
                self.save_player_event(self.player, "Papier")
                print("Player: Papier")
                return papier.Papier()
            case 4:
                self.play_statistic["Echse"] += 1
                self.save_player_event(self.player, "Echse")
                print("Player: Echse")
                return echse.Echse()
            case 5:
                self.play_statistic["Spock"] += 1
                self.save_player_event(self.player,"Spock")
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
                self.play_statistic["loss"] += 1
                self.save_player_event(self.player,"loss")
                return "You lost!"
            case 0:
                self.play_statistic["draw"] += 1
                self.save_player_event(self.player, "draw")
                return "It's a draw!"
            case 1:
                self.play_statistic["win"] += 1
                self.save_player_event(self.player, "win")
                return "You won!"

    def print_game_stats(self):
        return self.statistics

    def print_game_help():
        pass
    
    def input_difficulty(self):
        valid_inputs = ["normal", "hard", "impossible"]
        di = input("Enter Difficulty (normal, hard or impossible): ")
        while str(di).lower() not in valid_inputs:
            print("Please enter a valid Difficulty")
            di = input("Enter Difficulty (normal, hard or impossible): ")          
        self.set_difficulty(di)
        print(self.difficulty)       
       
    def set_difficulty(self, diff_in):
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
    
    def input_player(self):
        pi = input("Enter Player: ")
        self.set_player(pi)
    
    def set_player(self, player_name):
        self.player = str(player_name).lower()
    
    def end_game(self):
        print("Thank you for playing")
        exit()
            
        
    def get_plays_statistic(self, name):
        with open("player_save.txt", "r") as rd:
            saves = json.load(rd)     
        return saves[name]

    def get_statistic_percentage(self, stat):
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

    def create_computer_options(self):
        return ["Schere", "Stein", "Papier", "Echse", "Spock"]

    def save_player_event(self, name, event):
        with open("player_save.txt", "r") as rd:
            saves = json.load(rd)

        saves[name][event] +=1

        with open("player_save.txt", "w") as wd:
            wd.write(json.dumps(saves))

    def create_statistic(self):
        return {"Schere" : 0, "Stein" : 0, "Papier" : 0, "Echse" : 0, "Spock" : 0, "win":0, "draw" : 0, "loss": 0}

def main():
    game = SSPES_Game()
    game.start()
    #with open("player_save.txt", "r") as wd:
    #    saves = json.load(wd)
        
    #print(saves["player"]["loss"])

if __name__ == "__main__":
    
    main()