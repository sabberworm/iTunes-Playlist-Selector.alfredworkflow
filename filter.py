#!/usr/bin/env python

# encoding: utf-8

from subprocess import check_output
import xml.etree.ElementTree as ET
import re
from sys import argv

root = ET.Element('items')
def add_item(name, uuid, icon):
    item = ET.SubElement(root, 'item')
    item.attrib["uid"] = uuid
    item.attrib["arg"] = uuid
    ET.SubElement(item, "title").text = name
    ET.SubElement(item, "icon").text = icon

def check_filter(filter, name):
    if filter:
        for f in filter:
            if not f in name:
                return False
    return True

def add_items(lists, filter):
    for playlist in lists:
        playlist_info = name_id_pattern.search(playlist)
        name = playlist_info.group(2)
        if not playlist_info:
            continue
        if not check_filter(filter, name):
            continue
        add_item(name, playlist_info.group(1), "icon.png")

def add_reload():
    add_item('Reload Playlists', 'reload', 'reload.png')

name_id_pattern = re.compile(r'^([0-9A-F]+):(.*)$')
try:
    file = open('./playlists.txt', 'r')
    out = unicode(file.read(), 'utf-8')
    lists = out.splitlines()
except IOError:
    lists = list()

filter = "{query}"

# For debugging
if filter == "{qu" + "ery}":
    if len(argv) > 1:
        filter = unicode(argv[1], 'utf-8')
    else:
        filter = ''

if filter == '':
    filter = None
else:
    filter = filter.split()

if filter:
    add_items(lists, filter)
else:
    # Add Reload item
    add_reload()

print '<?xml version="1.0"?>'
print ET.tostring(root, 'utf-8')
