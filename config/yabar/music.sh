#!/bin/bash

old_track_id="-"

while true; do
    output=`sp eval`
    if [ $? -ne 0 ]; then
        track_id=""
        if [ "$old_track_id" != "$track_id" ]; then
            old_track_id=$track_id
            echo ""
        fi
    else
        regex='SPOTIFY_TRACKNUMBER="([^"]+)"'
        [[ $output =~ $regex ]]
        track_number=${BASH_REMATCH[1]}

        regex='SPOTIFY_TRACKID="([^"]+)"'
        [[ $output =~ $regex ]]
        track_id=${BASH_REMATCH[1]}

        regex='SPOTIFY_TITLE="([^"]+)"'
        [[ $output =~ $regex ]]
        title=${BASH_REMATCH[1]}

        regex='SPOTIFY_ARTIST="([^"]+)"'
        [[ $output =~ $regex ]]
        artist=${BASH_REMATCH[1]}

        regex='SPOTIFY_ALBUM="([^"]+)"'
        [[ $output =~ $regex ]]
        album=${BASH_REMATCH[1]}

        regex='SPOTIFY_ALBUMARTIST="([^"]+)"'
        [[ $output =~ $regex ]]
        album_artist=${BASH_REMATCH[1]}

        if [ "$old_track_id" != "$track_id" ]; then
            old_track_id=$track_id
            echo "$artist - $title"
        fi
    fi
done
