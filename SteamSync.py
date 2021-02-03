#!/usr/bin/env python3
import shutil
import subprocess
from pathlib import Path
from time import sleep
import os
import time
import psutil

BASE_PATH = Path("C:/Users/haeus/workspace")
SOURCE_FILE_PATH = BASE_PATH / "Testordner1" / "Datei.txt"
TARGET_FILE_PATH = BASE_PATH / "Testordner2" / "Datei.txt"

PROGRAM_NAME = "OUTLOOK.EXE"

def source_is_newer(SOURCE_FILE_PATH, TARGET_FILE_PATH):
    statinfo_source = os.stat(SOURCE_FILE_PATH)
    statinfo_target = os.stat(TARGET_FILE_PATH)
    seconds_since_source_modification = int(time.time()) -int(statinfo_source.st_mtime)
    seconds_since_target_modification = int(time.time()) -int(statinfo_target.st_mtime)

    if seconds_since_target_modification >= seconds_since_source_modification:
        return True
    else:
        return False

def is_running(search_term):
    for proc in psutil.process_iter(['pid', 'name']):
        process_name = proc.info["name"]

        if process_name == search_term:
            return True

def main():
    while True:
        if is_running(PROGRAM_NAME):
            print("Programm läuft")

            while is_running(PROGRAM_NAME):
                print("Warte auf Beendigung")
                sleep(0.1)


            if source_is_newer(SOURCE_FILE_PATH, TARGET_FILE_PATH):
                print('Quelldatei ist neuer')
                shutil.copy(SOURCE_FILE_PATH, TARGET_FILE_PATH)
                print("Datei wurde kopiert")
            else:
                print('Quelldatei ist älter oder auf dem gleichen Stand')
                print('Datei wurde nicht kopiert')
            
        else:
            print("Programm läuft nicht")

        sleep(0.1)   

if __name__ == "__main__":
    main()