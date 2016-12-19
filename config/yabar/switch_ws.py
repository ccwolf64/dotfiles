#!/usr/bin/env python

# Keeps track of all workspaces and outputs information for yabar to read
# TODO: Make one subscription and have all yabar scripts read that output
import i3
import sys
import codecs


# Given a list of workspace information, returns if workspace is visible
def parse_workspaces(wss):
    for ws in wss:
        sys.stdout.flush()
        if ws['visible']:
            return ws['num']

    return 0


ws = parse_workspaces(i3.get_workspaces())
if len(sys.argv) == 2 and sys.argv[1] == 'l':
    new_ws = str(ws-1) if ws-1 != 0 else '5'
elif len(sys.argv) == 2 and sys.argv[1] == 'r':
    new_ws = str(ws+1) if ws+1 != 6 else '1'

i3.command('workspace ', new_ws)
