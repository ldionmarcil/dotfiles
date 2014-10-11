#!/bin/bash

######### i3 #########
mkdir -p ~/.i3/
mkdir -p ~/.config/i3status/
ln -b -s ~/.config/dotfiles/i3/config ~/.i3/
ln -b -s ~/.config/dotfiles/i3/i3status/config ~/.config/i3status/config
ln -b -s ~/.config/dotfiles/i3/i3status/wrapper.py ~/.config/i3status/wrapper.py
ln -b -s ~/.config/dotfiles/i3/dmenu_geoip ~/.i3/
(
    cd ~/.config/dotfiles/i3/dmenu_geoip/;
    curl -O "http://download.maxmind.com/download/geoip/database/{asnum/GeoIPASNum.dat.gz,GeoLiteCity.dat.gz}";
    gunzip {GeoLiteCity,GeoIPASNum}.dat.gz;
)
ln -b -s ~/.config/dotfiles/i3/dmenu_hex2ascii ~/.i3/

######### xterm #########
ln -b -s ~/.config/dotfiles/xterm/.Xdefaults ~/.Xdefaults

######### xorg #########
ln -b -s ~/.config/dotfiles/x/.xinitrc ~/.xinitrc

######### zsh #########
ln -b -s ~/.config/dotfiles/zsh/.zshrc ~/.zshrc
ln -b -s ~/.config/dotfiles/zsh/.zshenv ~/.zshenv
ln -b -s ~/.config/dotfiles/zsh/.zprofile ~/.zprofile


