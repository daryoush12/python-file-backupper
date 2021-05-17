import io
import json

default_config = {
  "input": None,
  "output": None,
  "backup_cycle": 60
}

class BackupConfig():
    def __init__(self):
        try:
            with open("config.json", "r") as file:
                config = json.load(file)
                self.cycle = config['backup_cycle']
                self.input = config['input']
                self.output = config['output']                   
        except:
                print("Config.json file not found. Creating one with defaults..")
                in_path = input("Enter path into backuppable folder:")
                out_path = input("Enter output path:")
                cycle = input("How often should we backup the files? (in seconds):")

                default_config = {"input":in_path, "output":out_path, "backup_cycle":int(cycle)}
                
                with open("config.json", "w") as write_file:
                    json.dump(default_config, write_file)

                self.cycle = default_config['backup_cycle']
                self.input = default_config['input']
                self.output = default_config['output']




    def getCycle(self):
        return self.cycle



