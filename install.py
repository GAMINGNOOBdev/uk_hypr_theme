#!/usr/bin/env python3

#################
###           ###
###   SETUP   ###
###           ###
#################

import urllib.request

def download(url: str, filename: str):
    print("Downloading '" + filename + "' from '" + url + "'")
    urllib.request.urlretrieve(url, filename)

import os
import os.path
if not os.path.isfile("simple_term_menu.py"):
    print("Could not find terminal library!")
    download("https://raw.githubusercontent.com/IngoMeyer441/simple-term-menu/refs/heads/develop/simple_term_menu.py", "simple_term_menu.py")

import simple_term_menu as stm
import subprocess
import getpass
import shutil

HOME = subprocess.getoutput("echo $HOME")
CONFIG = f"{HOME}/.config"
WALLPAPER_PATH = f"{HOME}/Wallpapers"
FASTFETCH_PATH = f"{CONFIG}/fastfetch"
HYPRLAND_PATH = f"{CONFIG}/hypr"
SCRIPTS_PATH = f"{CONFIG}/Scripts"
WAYBAR_PATH = f"{CONFIG}/waybar"

PATHS = [
    CONFIG,
    WALLPAPER_PATH,
    FASTFETCH_PATH,
    HYPRLAND_PATH,
    SCRIPTS_PATH,
    WAYBAR_PATH,
]

def init_directories():
    for directory in PATHS:
        if not os.path.isdir(directory):
            print(f"Making directory '{directory}'")
            os.mkdir(directory)

def copy_file(inputpath, outputpath):
    print(f"'copying {inputpath}' --> '{outputpath}'")
    shutil.copy(inputpath, outputpath)

def copy_files(inputdir, outputdir):
    try:
        files = subprocess.getoutput(f"ls {inputdir}").split('\n')
        for file in files:
            installpath = f"{outputdir}/{file}"
            originalpath = f"{inputdir}/{file}"
            copy_file(originalpath, installpath)
    except e:
        print(e)

def modify_bashrc():
    with open(f"{HOME}/.bashrc", "a") as file:
        file.write("\n#ADDED BY P2 HYPRLAND THEME INSTALLER\nalias neofetch='fastfetch'\n")

def main():
    print("Select a theme to install")
    themes = ["P-2 Blood Red Darkness", "FRAUDULENCE Golden Valley of Fools", "Cancel"]
    option = stm.TerminalMenu(themes).show()
    themeFolder = None
    if option == 0:
        themeFolder = "p2theme"
    elif option == 1:
        themeFolder = "fraudtheme"

    if themeFolder == None:
        print("Goodbye!")
        exit(0)

    init_directories()
    copy_files(f"{themeFolder}/Wallpapers", WALLPAPER_PATH)
    copy_files(f"{themeFolder}/hypr", HYPRLAND_PATH)
    copy_files(f"{themeFolder}/waybar", WAYBAR_PATH)
    copy_files(f"{themeFolder}/Scripts", SCRIPTS_PATH)
    copy_files(f"{themeFolder}/fastfetch", FASTFETCH_PATH)
    modify_bashrc()

    os.system("clear")

    print(f"Successfully installed '{themes[option]}'")
    stm.TerminalMenu(["ok"]).show()

    main()

if __name__ == "__main__":
    main()
