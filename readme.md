# python-filebackupper

#### Author farsimadan.daryoush@gmail.com

# How to use

1. install needed packages as so:

```
pip install -r requirements.txt

```

2. And then run with

```
python main.py

```

Config structure:

```
{
  "input": "D:\\New folder",
  "output": "D:\\backupps",
  "backup_cycle": 10,
  "cleanup_cycle": 86400
}
```

input: path to folder that you want to backup
output: path to folder where you want data to be saved.
backup_cycle: How oftens should data be backed up? (in milliseconds)
cleanup_cycle: How often should backup folders be cleaned up? (in milliseconds)
