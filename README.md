Dotfiles
=========

This is my dotfile configuration for effortless desktop switching.

The setup currently contains
- i3wm with i3status
- xinit
- zsh
- xterm

Gotchas
----
- Different network interfaces on machines

Simple fix is to add a [rule to udev](https://wiki.archlinux.org/index.php/Network_configuration#Change_device_name), as such;

```
# /etc/udev/rules.d/10-network.rules
SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="bc:ae:c5:62:df:20", NAME="enp5s0"
```

- Different sources of input for CPU temperature

Create a symlink under ~/.config/temp_monitor that points to whichever source you use;

```sh
ln -s /sys/class/hwmon/hwmon0/temp1_input ~/.config/temp_monitor
```