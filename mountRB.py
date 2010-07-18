#!/usr/bin/env python

#**** BEGIN LICENSE BLOCK *****
# Version: GPL 3.0
# 
# The Original Code is mountRB code.
# 
# The Initial Developer of the Original Code is Jayakrishnan B Nair
# Portions created by the Initial Developer are Copyright (C) 2009-2010.
# All Rights Reserved.
# 
#
# Script to mount drives from the Rhythmbox library  
#    Copyright (C) 2010 Jayakrishnan B Nair <jayakrishnan.bk.nair@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#**** END LICENSE BLOCK *****

import os
import commands
import xml.parsers.expat

path  = "/home/"+commands.getoutput('whoami')+"/.local/share/rhythmbox/rhythmdb.xml"
flag = 0 
f = []
def start_element(name,attrs):
    global flag
    if name == "mountpoint":
        flag = 1
    else:
        flag = 0

def char_data(data):
    global flag
    if flag == 1:
        data = str(data)
        if data.find("file:///media/") <> -1 :
            data = data.replace("file:///media/","")
            if not(data in f):
                f.append(data)
            flag = 0

def end_element(name):
    global flag
    if name == "mountpoint":
        flag = 0


p = xml.parsers.expat.ParserCreate()

p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

p.ParseFile(open(path))
j  =  commands.getoutput("ls /dev/disk/by-label/").split("\n")


s = commands.getoutput("ls /dev/disk/by-label -lG")
for i in range(len(f)):
    if f[i] in j:
        label = f[i]
        x=s.find(label)
        if x <> -1:
            y=s.find('\n',x)
            if y <> -1:
                t = s[x:y].split('/')
            else:
                t = s[x:].split('/')
            mnted=os.listdir("/media/")
            if not(label in mnted):
                print "label : "+label+" devid : "+t[len(t)-1]
                g = commands.getoutput('gvfs-mount -d /dev/'+t[len(t)-1])
