
# D-bus
if which dbus-launch >/dev/null && test -z "$DBUS_SESSION_BUS_ADDRESS"; then
       eval `dbus-launch --sh-syntax --exit-with-session`
fi

eval `cat ~/.fehbg` & 
/usr/local/bin/peksystray &
pidgin &
conky &
