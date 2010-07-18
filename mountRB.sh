
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

cd /home/$(whoami)/mountRB/
python mountRB.py

echo Drives Mounted
echo starting RythmBox .................................
rhythmbox &
echo RhythmBox started
