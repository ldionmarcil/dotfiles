#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# © 2012 Valentin Haenel <valentin.haenel@gmx.de>
#
# This program is free software. It comes without any warranty, to the extent
# permitted by applicable law. You can redistribute it and/or modify it under
# the terms of the Do What The Fuck You Want To Public License (WTFPL), Version
# 2, as published by Sam Hocevar. See http://sam.zoy.org/wtfpl/COPYING for more
# details.

import os
import sys
import json
from time import time
from requests import get

def get_irc_activity():
    """ Get IRC activity, implying that irc-activity is filled with data from Circe. """
    try:
        with open('/tmp/irc-activity') as fp:
            lines = fp.readlines()
            if len(lines) > 0:
                return lines[0].strip().replace("[", "").replace("]", "").replace(",", " ")
            else:
                return "-"
    except IOError:
        return None


def get_load_data(duration):
    """Returns the load + color associated with the range"""
    OK_COLOR = "#8af2ea"
    HIGH_COLOR = "#ff0000"
    HIGH_THRESHOLD = 1 # if higher than this, load is HIGH
    time_keys = {1:0, 5:1, 15:2}
    load = os.getloadavg()[time_keys[duration]]
    return ("%s" % format(load, '.2f'), OK_COLOR if load < HIGH_THRESHOLD else HIGH_COLOR)

def formatLoad(duration):
    load, color = get_load_data(duration)
    return {"name":"load1", "text": load, "text_color": "%s" % color, "label":"%s:" % duration}

def formatNetwork(networkNodeList):
    node = networkNodeList[0]
    full_text = node["full_text"]
    if full_text != "": # only process displayed interfaces
        tokenized_text = full_text.split(":")
        interface_type = tokenized_text[0]
        interface_details = " ".join(tokenized_text[-1:])
        return {"name":"network", "text": interface_details, "label":"%s:" % interface_type}
    return None

def print_line(message):
    # print(message)
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()

def add_node(j, name, text, text_color="#8af2ea", label="", label_color="#1793D0", position=0, separator_width=2):
    j.insert(position, {'full_text' : text, 'color' : text_color, 'name' : name})
    if label != "": # need to insert label
        j.insert(position, {'full_text' : "%s" %label, 'color' : label_color, 'name' : '%s_label' % name, 'separator': False, 'separator_block_width': separator_width})
    return j

def processNodes(j):
    irc_activity = get_irc_activity()
    nodes = [{"label":"irc:", "name":"irc", "text": irc_activity} if irc_activity else None,
             formatLoad(1),
             formatLoad(5),
             formatLoad(15),
             formatNetwork([networkNode for networkNode in j if networkNode["name"] == "wireless"]),
             formatNetwork([networkNode for networkNode in j if networkNode["name"] == "ethernet"])]

    for node in reversed(nodes): # process each node as they are defined
        if node:
            j = add_node(j, **node)

    #clean post-processed nodes

    return [node for node in j if node["name"] != "wireless" and node["name"] != "ethernet"]

if __name__ == '__main__':
    # Skip the first line which contains the version header.
    print_line(read_line())
    # # The second line contains the start of the infinite array.
    print_line(read_line())

    #predefine this to fill the bar
    ip = "Obtaining"
    changed = False

    while True:
        line, prefix = read_line(), ''
        # ignore comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)

        j = processNodes(j)

        # j.insert(0, {'full_text' : 'test', 'color' : '#8af2ea', 'name' : 'irc'})
        # j.insert(0, {'full_text' : 'this is a', 'color' : '#8af2ea', 'name' : 'irc', 'separator' : False})

        # # j.insert(0, {'full_text' : '%s' % get_now_playing(), 'color' : '#8af2ea', 'name' : 'mpd'})
        # j.insert(0, {'full_text' : '%s' % get_irc_activity(), 'color' : '#8af2ea', 'name' : 'irc'})


        # j.insert(-2, {'full_text' : '1:%s' % get_load(1), 'color' : '#8af2ea', 'name' : 'irc'})
        # j.insert(-2, {'full_text' : '5:%s' % get_load(5), 'color' : '#8af2ea', 'name' : 'irc'})
        # j.insert(-2, {'full_text' : '15:%s' % get_load(15), 'color' : '#8af2ea', 'name' : 'irc'})


        # and echo back new encoded jsonp
        print_line(prefix+json.dumps(j))
