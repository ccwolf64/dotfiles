#!/usr/bin/env python

# Keeps track of all workspaces and outputs information for yabar to read
# TODO: Make one subscription and have all yabar scripts read that output
import i3
import sys
import codecs

# Necessary to print unicode on yabar
#UTF8Writer = codecs.getwriter('utf8')
#sys.stdout = UTF8Writer(sys.stdout)

# Array of primary workspace information. Each entry is an array of two elements,
# the workspace name and argb color associated with the workspace
wsinfo = {
    1: [u'\uf120','FF2CBFA2'],   # ws1
    2: [u'\uf0ac','FFA22CBF'],   # ws2
    3: [u'\uf121','FF9E8276'],   # ws3
    4: [u'\uf001','FFFFC236'],   # ws4
    5: [u'\uf085','FFFD432A']    # ws5
}

#Hex value for argb color shown on visible workspace
fg_standard = 'EEFFFFFF'
fg_faded = 'EE818181'

bg_standard = 'EE2D2D2D'
bg_highlight = 'EE565656'

u_standard = 'EEFFFFFF'
u_off = 'EE2D2D2D'

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    wsn = int(sys.argv[1])
else:
    print('This program takes exactly one integer arguement')
    sys.exit(1)

# Given a list of workspace information, returns if workspace is visible
#[
#   {'num': 1, 
#   'name': '1', 
#   'rect': {
#       'height': 1032, 
#       'width': 1920, 
#       'y': 24, 
#       'x': 0
#   }, 
#   'output': 'HDMI-1', 
#   'focused': True, 
#   'urgent': False, 
#   'visible': True
#   },
#   ...
#]
def parse_workspaces(wss):
    info = {}
    for ws in wss:
        info[ws['num']] = ws['visible']
    return info

# Puts workspace information in format readible by yabar
def parse_info(info, wsn):
    current_ws = info.get(wsn, False)
    has_open_program = wsn in info

    fg = fg_standard
    bg = bg_standard
    u = u_standard

    if current_ws:
        bg = bg_highlight 
        u =  wsinfo[wsn][1]
    elif has_open_program:
        pass
    else:
        fg = fg_faded
        u = u_off
    return '!Y FG 0x' + fg + ' BG 0x' + bg + ' U 0x' + u + ' Y! ' + wsinfo[wsn][0]

def workspace(event, data, subscription):
    print(parse_info(parse_workspaces(data), wsn))
    sys.stdout.flush()

print(parse_info(parse_workspaces(i3.get_workspaces()), wsn))
sys.stdout.flush()
subscription = i3.Subscription(workspace, 'workspace')
