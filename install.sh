#!/bin/bash

######### i3 #########
mkdir -p ~/.i3/
mkdir -p ~/.config/i3status/
ln -b -s ~/.config/dotfiles/i3/config ~/.i3/
ln -b -s ~/.config/dotfiles/i3/i3status/config ~/.config/i3status/config
ln -b -s ~/.config/dotfiles/i3/i3status/wrapper.py ~/.config/i3status/wrapper.py


######### xterm #########
ln -b -s ~/.config/dotfiles/xterm/.Xdefaults ~/.Xdefaults


######### xorg #########
ln -b -s ~/.config/dotfiles/x/.xinitrc ~/.xinitrc


######### zsh #########
ln -b -s ~/.config/dotfiles/zsh/.zshrc ~/.zshrc
ln -b -s ~/.config/dotfiles/zsh/.zshenv ~/.zshenv
ln -b -s ~/.config/dotfiles/zsh/.zprofile ~/.zprofile


