#!/usr/bin/env python

#########################################################################
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

from math import *
start_angle=0
end_angle=360
num_parts=360
r=80
temp=(end_angle - start_angle)/num_parts
print "L,Sine Curve,1,2"
for i in range(0,num_parts):
    current_angle=start_angle + i*temp
    y=r*sin(radians(current_angle))
    if(i==0):
        y1=y
    #print "(",x,",",y,")"
    print current_angle,",",y

print end_angle,",",y1

print "\nL,Cosine Curve,1,3"
#start_angle=-520
#end_angle=-160
temp=(end_angle - start_angle)/num_parts
for i in range(0,num_parts):
    current_angle=start_angle + i*temp
    y=r*cos(radians(current_angle))
    if(i==0):
        y1=y
    #print "(",x,",",y,")"
    print current_angle,",",y

print end_angle,",",y1
