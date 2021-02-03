#!/usr/bin/env python3
import shutil
import subprocess
from pathlib import Path
from time import sleep
import os
import time

BASE_PATH = Path("C:/Users/haeus/workspace")
SOURCE_FILE_PATH = BASE_PATH / "Testordner1" / "Datei.txt"
TARGET_FILE_PATH = BASE_PATH / "Testordner2" / "Datei.txt"

PROGRAM_NAME = "OUTLOOK.EXE"


def is_running(search_term):
    result = subprocess.run(
        ["tasklist"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return search_term in result.stdout


def main2():
    while True:
        if is_running(PROGRAM_NAME):
            print("Programm läuft")

            while is_running(PROGRAM_NAME):
                print("Warte auf Beendigung")
                sleep(0.1)

            shutil.copy(SOURCE_FILE_PATH, TARGET_FILE_PATH)
            print("Datei wurde kopiert")
        else:
            print("Programm läuft nicht")

        sleep(0.1)

def source_is_newer(SOURCE_FILE_PATH, TARGET_FILE_PATH):
    statinfo_source = os.stat(SOURCE_FILE_PATH)
    statinfo_target = os.stat(TARGET_FILE_PATH)
    seconds_since_source_modification = int(time.time()) -int(statinfo_source.st_mtime)
    seconds_since_target_modification = int(time.time()) -int(statinfo_target.st_mtime)

    if seconds_since_target_modification >= seconds_since_source_modification:
        return True
    else:
        return False

def main():
    if source_is_newer(SOURCE_FILE_PATH, TARGET_FILE_PATH):
        print('Quelldatei ist neuer')
    else:
        print('Quelldatei ist älter')

if __name__ == "__main__":
    main()