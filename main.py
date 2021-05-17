from config import BackupConfig
import asyncio
import logging
from distutils.dir_util import copy_tree
from datetime import date
import os
from time import time


path = os.getcwd()
settings = BackupConfig()
today = date.today()

#TODO: Test for missing config options and bad filepaths.
async def main():
    print("Backupper has started. Running cycle.")
    while True:   
        await asyncio.sleep(settings.cycle)
        newPath = f"{settings.output}/{today.__str__()}_{time()}"
        copy_tree(settings.input, newPath)
        print(f"Backupping from {settings.input} to {newPath}")
    
asyncio.run(main())