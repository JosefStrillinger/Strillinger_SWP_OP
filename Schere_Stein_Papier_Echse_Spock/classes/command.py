
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