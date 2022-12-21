
class Command_Manager():
    def __init__(self):
        self.commands = []
        
    def run_cmd(self, cmd):
        if len(cmd) > 0:
            pass
         
    def add_cmd(self, cmd):
        cmd.id = len(self.commands)
        self.commands.append(cmd)