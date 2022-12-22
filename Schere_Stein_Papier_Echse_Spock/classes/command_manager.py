
class Command_Manager():
    def __init__(self):
        self.commands = []
        
    def run_cmd(self, cmd):
        #if len(cmd) > 0:
        for i in range(len(self.commands)):
            if cmd == self.commands[i].command:
                self.commands[i].run_cmd()
         
    def add_cmd(self, cmd):
        cmd.id = len(self.commands)
        self.commands.append(cmd)