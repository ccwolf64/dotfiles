#!/bin/bash

case $1 in
    -v|--volume)
        volume=`volume -g`
        echo "  $volume% "

        while true; do
            new_volume=`volume -g`
            if [ "$new_volume" -ne "$volume" ]; then
                volume=$new_volume
                echo "  $volume% "
            fi
        done
        ;;
    -m|--music)
        stat=$(dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'PlaybackStatus'|egrep -A 1 "string"|cut -b 26-|cut -d '"' -f 1|egrep -v ^$)
        if [ "$stat" == "Playing" ]; then
            echo ""
        else
            echo ""
        fi
        while true; do
            new_stat=$(dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'PlaybackStatus'|egrep -A 1 "string"|cut -b 26-|cut -d '"' -f 1|egrep -v ^$)
            if [ "$new_stat" != "$stat" ]; then
                stat=$new_stat
                if [ "$stat" == "Playing" ]; then
                    echo ""
                else
                    echo ""
                fi
            fi
        done
        ;;
esac
