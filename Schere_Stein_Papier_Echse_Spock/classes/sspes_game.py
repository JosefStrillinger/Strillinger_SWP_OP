import json
import random
from enum import Enum
from classes.schere import Schere
from classes.stein import Stein
from classes.papier import Papier
from classes.echse import Echse
from classes.spock import Spock
from classes.player import Player
from classes.difficulty import Difficulty
from classes.command import Command
from classes.command_manager import Command_Manager

class SSPES_Game:
    def __init__(self):
        self.init()
        
    def init(self):
        self.difficulty = Difficulty.normal
        self.player = Player("player")
        self.player.init_player()
        self.play_statistic = self.create_statistic()
        self.command_manager = Command_Manager()
        exit = Command(self.end_game, "-e")
        play = Command(self.play, "-p")
        reset = Command(self.start, "-r")
        player = Command(self.input_player, "-pl")
        difficulty = Command(self.input_difficulty, "-d")
        menu = Command(self.input_menu_command, "-m")
        commands = [exit, play, reset, player, difficulty, menu]
        for i in range(len(commands)):
            self.command_manager.add_cmd(commands[i])
        #print(self.command_manager.commands)
        # TODO:
        # finish command manager and make it work
        # --> asap
           
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
                if str(a).lower() == "-e":
                    self.end_game()
                print("Please enter a valid number")
                a = input("Input a number of your choosing (1-5): ")
                
            
            #print(obj.get_weak_to())
            print("\nGlobal stats for player: ")
            player_percent_stats = self.get_statistic_percentage(self.get_plays_statistic(self.player))
            
            print("")
            obj = self.play_input_handler(a)
            
            if self.difficulty == Difficulty.normal:
                comp_turn = random.choice(comp_options)
                print("Computer: " + comp_turn)
                res = obj.get_relation(comp_turn)
                print("\nResult: "+self.check_result(res))
                print(self.print_game_stats())
            
            if self.difficulty == Difficulty.hard:
                most_used_player_turn = max(player_percent_stats)
                comp_turns_possible = self.get_comp_options(most_used_player_turn)
                #print(comp_turns_possible)
                comp_turn = random.choice(comp_turns_possible)
                print("Computer: " + comp_turn)
                res = obj.get_relation(comp_turn)
                print("\nResult: "+self.check_result(res))
                print(self.print_game_stats())
                
            if self.difficulty == Difficulty.impossible:
                comp_turns_possible = obj.get_weak_to()
                comp_turn = random.choice(comp_turns_possible)
                print("Computer: " + comp_turn)
                res = obj.get_relation(comp_turn)
                print("\nResult: "+self.check_result(res))
                print(self.print_game_stats())      
          
    #possible changes:
    # add object to constructor, change ctor to (self, input_player, player_obj)          
    # change case to return player_obj = schere.Schere()
    # then other cases can be added
    
    def game_menu(self):
        print("\nWelcome the SSPES - Game developed by Josef Strillinger")
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
                #self.command_manager.run_cmd("-e")
            case "-r":
                self.start()
                #self.command_manager.run_cmd("-r")
            case "-p":
                self.play()
                #self.command_manager.run_cmd("-p")
            case "-pl":
                self.input_player()
                #self.command_manager.run_cmd("-pl")
                self.input_menu_command()
            case "-d":
                self.input_difficulty()
                #self.command_manager.run_cmd("-d")
                self.input_menu_command()
            case other:
                self.input_menu_command()
                
    def play_input_handler(self, input_player): 
        match int(input_player):
            case 1:
                self.play_statistic["Schere"] += 1
                self.save_player_event("Schere")
                print("Player: Schere")
                return Schere()
            case 2:
                self.play_statistic["Stein"] += 1
                self.save_player_event("Stein")
                print("Player: Stein")
                return Stein()
            case 3:
                self.play_statistic["Papier"] += 1
                self.save_player_event("Papier")
                print("Player: Papier")
                return Papier()
            case 4:
                self.play_statistic["Echse"] += 1
                self.save_player_event("Echse")
                print("Player: Echse")
                return Echse()
            case 5:
                self.play_statistic["Spock"] += 1
                self.save_player_event("Spock")
                print("Player: Spock")
                return Spock()
    
    def get_comp_options(self, input_comp):
        match str(input_comp):
            case "Schere":           
                help_obj = Schere()  
                #print(help_obj.get_weak_to())
                return help_obj.get_weak_to()
            case "Stein":
                help_obj = Stein()
                #print(help_obj.get_weak_to())
                return help_obj.get_weak_to()
            case "Papier":
                help_obj = Papier()
                #print(help_obj.get_weak_to())
                return help_obj.get_weak_to()
            case "Echse":
                help_obj = Echse()
                #print(help_obj.get_weak_to())
                return help_obj.get_weak_to()
            case "Spock":
                help_obj = Spock()
                #print(help_obj.get_weak_to())
                return help_obj.get_weak_to()
         
    def check_result(self, outcome):
        match outcome:
            case -1:
                self.play_statistic["loss"] += 1
                self.save_player_event("loss")
                return "You lost!"
            case 0:
                self.play_statistic["draw"] += 1
                self.save_player_event("draw")
                return "It's a draw!"
            case 1:
                self.play_statistic["win"] += 1
                self.save_player_event("win")
                return "You won!"

    def print_game_stats(self):
        return self.play_statistic

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
        self.player.set_name(str(player_name).lower())
        self.player.init_player()
    
    def end_game(self):
        print("Thank you for playing")
        exit()
              
    def get_plays_statistic(self, player):
        name = player.get_name()
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
            print(i+": "+str(round(percentages[x], 5))+" % \t" + str(needed_dict[i])+" mal")
            dict_with_percentages[i] = percentages[x]
            x += 1

        return dict_with_percentages

    def create_computer_options(self):
        return ["Schere", "Stein", "Papier", "Echse", "Spock"]

    def save_player_event(self, event):
        name = self.player.get_name()
        with open("player_save.txt", "r") as rd:
            saves = json.load(rd)

        saves[name][event] +=1

        with open("player_save.txt", "w") as wd:
            wd.write(json.dumps(saves))

    def create_statistic(self):
        return {"Schere" : 0, "Stein" : 0, "Papier" : 0, "Echse" : 0, "Spock" : 0, "win":0, "draw" : 0, "loss": 0}