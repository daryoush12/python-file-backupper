from config import BackupConfig
import asyncio
import logging
from distutils.dir_util import copy_tree
from datetime import date
import os
from time import time
from distutils.errors import DistutilsFileError


path = os.getcwd()
settings = BackupConfig()
today = date.today()

#TODO: Test for missing config options and bad filepaths.
async def main():
    try:
        print("Backupper has started. Running cycle.")
        while True:   
            newPath = f"{settings.output}/{today.__str__()}_{time()}"
            copy_tree(settings.input, newPath)
            print(f"Backupping from {settings.input} to {newPath}")
            await asyncio.sleep(settings.cycle)
    except DistutilsFileError:
        print("Provided folder or file not found. Check your configurations.")
        
    
asyncio.run(main())