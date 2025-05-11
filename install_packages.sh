#!/bin/bash

yay -Sy hyprland hyprpolkitagent xdg-desktop-portal-hyprland hyprshot qt6ct-kde
sudo pacman -Sy hyprpaper waybar fastfetch rofi swaync kservice blueman wl-clipboard kitty dolphin spotify-launcher playerctl pavucontrol poppler-glib
sudo systemctl enable --now bluetooth
