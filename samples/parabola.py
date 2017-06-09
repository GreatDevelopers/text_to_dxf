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
start_x=0
end_x=500
a=10
print "L,,1,2"
for x in range(start_x,end_x+1):
    y=sqrt(4*a*x)
    print x,",",y

print "\nL,Parabolic Curve,1,2"
for x in range(start_x,end_x+1):
    y=copysign(sqrt(4*a*x),-1);
    print x,",",y
