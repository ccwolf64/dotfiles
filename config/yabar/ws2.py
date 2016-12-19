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
wsinfo = [
    [u'\uf120','2CBFA2'],   # ws1
    [u'\uf0ac','A22CBF'],   # ws2
    [u'\uf121','9E8276'],   # ws3
    [u'\uf001','FFC236'],   # ws4
    [u'\uf085','FD432A']    # ws5
]

#Hex value for argb color shown on visible workspace
highlight = '565656'

# Given a list of workspace information, returns if workspace is visible
def parse_workspaces(wss):
    for ws in wss:
        #print(ws)
        sys.stdout.flush()
        if ws['visible']:
            return ws['num']

    return 0

# Puts workspace information in format readible by yabar
def parse_info(num):
    s = ''
    for i, ws in enumerate(wsinfo):
        if i == num-1:
            s += '<span size="xx-large" foreground="#' + ws[1] + '" background="#' + highlight+ '">  ' + ws[0] + '  </span>' 
        else:
            s += '<span size="xx-large">  ' + ws[0] + '  </span>' 
        s += '  '
    return s[:-2]

def workspace(event, data, subscription):
    print(parse_info(parse_workspaces(data)))
    sys.stdout.flush()

print(parse_info(parse_workspaces(i3.get_workspaces())))
sys.stdout.flush()
subscription = i3.Subscription(workspace, 'workspace')
