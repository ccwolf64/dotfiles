#!/usr/bin/env python

# Keeps track of all workspaces and outputs information for yabar to read
# TODO: Make one subscription and have all yabar scripts read that output
import i3
import sys
import codecs

# Necessary to print unicode on yabar
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

# Array of primary workspace information. Each entry is an array of two elements,
# the workspace name and argb color associated with the workspace
wsinfo = [
    [u'\uf120','FF2CBFA2'],   # ws1
    [u'\uf0ac','FFA22CBF'],   # ws2
    [u'\uf121','FF9E8276'],   # ws3
    [u'\uf001','FFFFC236'],   # ws4
    [u'\uf085','FFFD432A']    # ws5
]

#Hex value for argb color shown on visible workspace
highlight = 'EE565656'

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    wsn = int(sys.argv[1])
else:
    print 'This program takes exactly one integer arguement'
    sys.exit(1)

# Given a list of workspace information, returns if workspace is visible
def parse_workspaces(wss, num):
    info = []
    for ws in wss:
        if (num <= len(wsinfo) and ws['num'] == num) or (num > len(wsinfo) and ws['num'] > len(wsinfo)):
            info.append((ws['num'], ws['visible']))
    if num <= len(wsinfo) and len(info) == 0:
        info = [(num, False)]

    return info

# Puts workspace information in format readible by yabar
def parse_info(info):
    s = ''
    if len(info) > 0:
        if info[0][0] <= len(wsinfo):
            if info[0][1] == True:
                s += '!YBG0x' + highlight + 'U0x' + wsinfo[info[0][0] - 1][1] + 'Y!'
            s += wsinfo[info[0][0] - 1][0]
        else:
            s += ' '
            for i in info:
                if i[1] == True:
                    s = '!YBG0x' + highlight + 'Y!' + s
                    s += '(' + str(i[0]) + ') | '
                else:
                    s += str(i[0]) + ' | '
            s = s[:-3]
            s += ' '
    return s

def workspace(event, data, subscription):
    print parse_info(parse_workspaces(data, wsn))
    sys.stdout.flush()

print parse_info(parse_workspaces(i3.get_workspaces(), wsn))
sys.stdout.flush()
subscription = i3.Subscription(workspace, 'workspace')
