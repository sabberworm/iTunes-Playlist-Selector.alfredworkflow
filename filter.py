#!/usr/bin/env python

# encoding: utf-8

from subprocess import check_output
import xml.etree.ElementTree as ET
import re
from sys import argv

NAME_ID_PATTERN = re.compile(r'^([0-9A-F]+):([slfSugrc]+):(.*)$')

root = ET.Element('items')
def add_item(name, uuid, icon):
    item = ET.SubElement(root, 'item')
    item.attrib["uid"] = uuid
    item.attrib["arg"] = uuid
    ET.SubElement(item, "title").text = name
    ET.SubElement(item, "icon").text = icon

def check_filter(filter, name):
    name = name.lower()
    if filter:
        for f in filter:
            if not f.lower() in name:
                return False
    return True

def add_items(lists, filter, flag_filter):
    for playlist in lists:
        playlist_info = NAME_ID_PATTERN.search(playlist)
        name = playlist_info.group(3)
        flags = playlist_info.group(2)
        if playlist_info == None:
            continue
        if not check_filter(filter, name):
            continue
        flag_filter_matches = True
        for flag in flag_filter:
          if flags.find(flag) == -1:
            flag_filter_matches = False
            break
        icon = 'icon.png'
        if(flags.find('s') > -1):
          icon = 'smart.png'
        if(flags.find('l') > -1):
          icon = 'library.png'
        if(flags.find('f') > -1):
          icon = 'folder.png'
        if(flags.find('S') > -1):
          icon = 'subscription.png'
        if(flags.find('c') > -1):
          icon = 'cd.png'
        if(flags.find('r') > -1):
          icon = 'radio.png'
        add_item(name, playlist_info.group(1), icon)

def add_reload():
    add_item('Reload Playlists', 'reload', 'reload.png')

try:
    file = open('./playlists.txt', 'r')
    out = unicode(file.read(), 'utf-8')
    lists = out.splitlines()
except IOError:
    lists = list()

filter = unicode(argv[1], 'utf-8')
disable_reload = len(argv) > 2 and argv[2] == 'false'
flag_filter = argv[3] if len(argv) > 3 else ''

if filter == '':
    filter = None
else:
    filter = filter.split()

if filter or disable_reload:
    add_items(lists, filter, flag_filter)
else:
    # Add Reload item
    add_reload()

print '<?xml version="1.0"?>'
print ET.tostring(root, 'utf-8')
