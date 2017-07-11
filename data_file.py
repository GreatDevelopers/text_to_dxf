#########################################################################
# This is the data file of the program. Change the variables below to   #
# change the functioning of script. Read comments at R.H.S of the       #
# various variables to know about the meaning of the variables.         #                       
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


col_delm=','             # Column delimiter used in input file
                         # (E.g- '\t' for TAB, ',' for comma etc.)

scaleX=1                 # Value by which X coordinate is scaled

scaleY=1                 # Value by which Y coordinate is scaled

txt_sp=5                 # Spacing between lower point and 1st text line

x_col=0                  # X co-ordinate position in input file (starting from 0)
y_col=1                  # Y co-ordinate position in input file (starting from 0)
r_col=2                  # position of radius in input file (if C or A is the type)
s_col=3                  # position of start angle (if A is the type)
e_col=4                  # position of end angle (if A is the type)
sw_col=2				 # position of start width (if P is the type)
ew_col=3				 # position of end width (if P is the type)
bulge_col=4				 # position of bulge (if P is the type)

mode=1                   # 0 to draw figures by taking the co-ordinates values in 
                         # the input file as absolute co-ordinates.
                         # 1 to draw figures relative to each other  

# Following variables are used only if mode=1

Xref=100                 # X coordinate of reference point
Yref=100                 # Y coordinate of reference point

shiftX=100               # Value by which Xref coordinate is translated
                         # after drawing one figure.

shiftY=-100              # Value by which Yref coordinate is translated 
                         # after drawing one figure.
                         
shift_direction=0        # 0 to draw figures row-wise  
                         # 1 to draw figures columnwise
                         
shift_factor=3           # Denotes the number of figures drawn in one
                         # horizontal or vertical segment (must be positive)  

