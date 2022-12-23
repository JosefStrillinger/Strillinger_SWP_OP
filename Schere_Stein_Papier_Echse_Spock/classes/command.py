
class Command(): # look into it
    def __init__(self, method, command):
        self.id = 0
        self.method = method
        self.command = command
    
    def run_cmd(self):
        self.method()
        
    def __str__(self):
        print("Description: {0} \nCommand: {1}\n".format(self.command))