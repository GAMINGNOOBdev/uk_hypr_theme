#!/bin/bash

yay -Sy hyprland hyprpolkitagent xdg-desktop-portal-hyprland
sudo pacman -Sy hyprpaper waybar fastfetch swaync kservice blueman wl-clipboard kitty dolphin spotify-launcher playerctl
sudo systemctl enable --now bluetooth
