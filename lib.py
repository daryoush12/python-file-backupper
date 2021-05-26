import os
from datetime import date
from time import time

today = date.today().isoformat()

# returns removable folders by current date. Should always leave newest backup alive.
def getRemovablesByDate(output_path):
    try:
        path = os.walk(output_path, topdown=False)
        result = getDirectoryFolders(output_path)
    
        res_iterable = filter(filter_folders, result)
        filtered_ds = [res for res in res_iterable]
        length_filtered = len(filtered_ds)
        # Some cool sorting + splitting magic out of my ass
        removables = sorted(result, key=lambda x:x['creationDate'])[1:length_filtered]
        return removables
    except:
        print("No viable backups for removal found.")
        return []
        
def getDateObjectFromString(name):
    parts = str.split(name, '_')
    test = float(parts[1])
    dictionary = {"path": name, "creationDate": test}
    return dictionary

def filter_folders(folder):    
    created = date.fromtimestamp(int(folder['creationDate'])).isoformat()
    return today == created

def getDirectoryFolders(path):
    path = os.walk(path, topdown=False)
    result = []
    for dirs in path:
        backups = [name for name in dirs]
    
    for folder_name in backups[1]:
        val = getDateObjectFromString(folder_name)
        result = [*result, val]

    return result