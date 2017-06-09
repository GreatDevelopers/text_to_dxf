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
a=200
b=100
print "L,Eclipse,1,3"
temp=(end_angle - start_angle)/num_parts
for i in range(0,num_parts+1):
    x=a*cos(radians(start_angle + i*temp))
    y=b*sin(radians(start_angle + i*temp))
    #print "(",x,",",y,")"
    print x,",",y
