import subprocess
import getpass
import os

HOME = subprocess.getoutput("echo $HOME")
CONFIG = f"{HOME}/.config"
WALLPAPER_PATH = f"{HOME}/Wallpapers"
FASTFETCH_PATH = f"{CONFIG}/fastfetch"
HYPRLAND_PATH = f"{CONFIG}/hypr"
WAYBAR_PATH = f"{CONFIG}/waybar"

PATHS = [
    CONFIG,
    WALLPAPER_PATH,
    FASTFETCH_PATH,
    HYPRLAND_PATH,
    WAYBAR_PATH,
]

packages = [
    "hyprpaper", "waybar", "fastfetch", "swaync"
]

def install_packages():
    getSUDO()
    packageinstallcmd = "sudo pacman -Sy "
    for package in packages:
        packageinstallcmd += package + " "
    print(f"Running package install command '{packageinstallcmd}'")
    # just run the command and let the user install it
    subprocess.Popen(packageinstallcmd, text=True, shell=True)

def copy_file(inputpath, outputpath):
    print(f"'copying {inputpath}' --> '{outputpath}'")
    with open(outputpath, "wb+") as outfile:
        with open(inputpath, "rb") as infile:
            outfile.write(infile.readall())

def init_directories():
    for directory in PATHS:
        try:
            dir(directory)
        except:
            os.mkdir(directory)

def copy_config_files(inputdir, outputdir):
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
    install_packages()
    init_directories()
    copy_file("p-2.png", f"{WALLPAPER_PATH}/p-2.png")
    copy_config_files("hypr", HYPRLAND_PATH)
    copy_config_files("waybar", WAYBAR_PATH)
    copy_config_files("fastfetch", FASTFETCH_PATH)
    modify_bashrc()

if __name__ == "__main__":
    main()
