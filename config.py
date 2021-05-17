import io
import json

class BackupConfig():
    def __init__(self):
        try:
            with open("config.json", "r") as file:
                config = json.load(file)
                self.cycle = config['backup_cycle']
                self.input = config['input']
                self.output = config['output']
        except:
                print("Could not init configuration. config.json file not found")

    def getCycle(self):
        return self.cycle



