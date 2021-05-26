from config import BackupConfig
import asyncio
import logging
from distutils.dir_util import copy_tree, remove_tree
from datetime import date
import os
from time import time
from distutils.errors import DistutilsFileError
from multiprocessing import Process
from lib import getRemovablesByDate, getDateObjectFromString

path = os.getcwd()
settings = BackupConfig()
today = time()

def backup():
    newPath = f"{settings.output}/backup_{today.__str__()}"
    copy_tree(settings.input, newPath)
    print(f"Backupping from {settings.input} to {newPath}")

def clean(): 
    print("Cleaning up backup folder")
    removables = getRemovablesByDate(settings.output)

    for removable in removables:
        p = f"{settings.output}\{removable['path']}"
        remove_tree(p)
    
    print("Clean up done.")
    
#TODO: Test for missing config options and bad filepaths.
async def backup_process():
    try:
        print("Backupper has started. Running cycle.")
        while True:   
            backup()
            await asyncio.sleep(settings.cycle)
    except DistutilsFileError:
        print("Provided folder or file not found. Check your configurations.")
    except: 
        print("Unknown error please contact author for help.")
        
async def cleanup_process():
    try:
        await asyncio.sleep(settings.cleanup)
        clean()
    except DistutilsFileError:
        print("Provided folder or file not found. Check your configurations.")

async def main():
    l = await asyncio.gather(
        backup_process(),
        cleanup_process())
    print(l)

asyncio.run(main())