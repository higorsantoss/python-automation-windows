# %% [markdown]
# Automation Windows, Open Microsoft Edge and download a txt file

# %%
import pyperclip
import time
import pyautogui
import shutil
import os
import logging
import logging

from os.path import exists, abspath
from pathlib import Path

def set_up_log(root_name: str) -> None: 
    logging.root = logging.getLogger(root_name)
    logging.basicConfig(level = logging.INFO)


#If we want show a log in display
set_up_log('AutomatizationWindows')

# Wait 1 second between each command pyautogui
pyautogui.PAUSE = 1  

# Open browser Windows https://file-examples.com/index.php/sample-documents-download/sample-xls-download/

pyautogui.hotkey('win')
pyautogui.write('edge')
pyautogui.press('enter')

pyperclip.copy('https://filesamples.com/formats/txt')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Wait 5 seconds until get position x and y of mouse after that you can decrease the time to 2 seconds
time.sleep(3)

# print a position of mouse after time.sleep(3)
#pyautogui.position()

# if you want 2 or mores clicks add the parameter clicks=2
pyautogui.click(x=3746, y=607, clicks=1) 

# %%
# Get path or directory windows 
downloads_path = str(Path.home() / "Downloads")
downloads_path += "\\"

# Get classpath of project 
project_root_dir = abspath(os.curdir)

file = "sample3.txt"
file_complet = downloads_path + file

# Verify if the file exists in the directory
file_exists_downloads = exists(file_complet)
file_exists_project_root = exists(project_root_dir+ "\\" + file)

if(file_exists_project_root):
    logging.info('file already copied to the project directory')  
elif(file_exists_downloads):
    # Copy file to another directory
    shutil.copy(file_complet, project_root_dir)
    logging.info('File copied successfully')  
else:
    logging.error('Could not copy the file. File not found.')


