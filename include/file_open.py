#########################################################################
# This file contains code to open various files used in the script.     #
#                                                                       #
# This program is free software; you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation; either version 2 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program; if not, write to the Free Software           #
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.             #
#########################################################################

import sys, os.path

# Checking for validity of commandline arguments

if len(sys.argv)!=3:
    print "Usage: python text_to_dxf.py input_file output_file"
    exit(1)
if os.path.exists(sys.argv[1])==False:
    print "Error: Input file does not exist"
    exit(1)
if  os.path.exists(sys.argv[2])==True:
    print "Warning: Output file already exists. Do you want to overwrite it?"
    choice=raw_input("Enter your choice (Y/N)")
    if choice=="N" or choice=="n":
        print "Good Bye!"
        exit(1)            

input_file=sys.argv[1]
output_file=sys.argv[2]

head_file="include/head"      #header file used internally (not to be changed) 
foot_file="include/foot"      #footer file used internally (not to be changed)

# Opens various required files

in_file=open(input_file, 'r')		
out_file=open(output_file, 'w')
hd_file=open(head_file, 'r')
ft_file=open(foot_file,'r')
head_data=hd_file.read()
foot_data=ft_file.read()

# Writing header file to output file

out_file.write(head_data)

lines = in_file.readlines()
print 'Total lines:'
print lines