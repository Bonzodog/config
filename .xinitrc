#!/bin/sh
# $Xorg: xinitrc.cpp,v 1.3 2000/08/17 19:54:30 cpqbld Exp $

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    /usr/bin/xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    /usr/bin/xmodmap $sysmodmap
fi

if [ -f $userresources ]; then
    /usr/bin/xrdb -merge $userresources
fi

if [ -f $usermodmap ]; then
    /usr/bin/xmodmap $usermodmap
fi

# Create default user directory & populate it if not already existent
if [ ! -d $HOME/.config/openbox ]; then
  mkdir -p $HOME/.config/openbox
  for FILE in menu.xml rc.xml;
  do cat /etc/xdg/openbox/$FILE > $HOME/.config/openbox/$FILE;
  done
fi

DEFAULT_SESSION=awesome
case $1 in
  awesome) exec awesome ;;
  openbox) exec openbox-session ;;
  *) exec $DEFAULT_SESSION ;;
esac

