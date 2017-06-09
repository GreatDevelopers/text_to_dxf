#########################################################################
# This file contains definitions of functions used in the script.       #
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


def is_numeric(var):
    try:
        float(var)
        return True
    except ValueError:
        return False

def draw_text(ob_id,point,txt_hght,text,layer,w_file):
    w_file.write("MTEXT\n5\n" + str(ob_id) + "\n100\nAcDbEntity\n100\n")
    w_file.write("AcDbMText\n8\n"+layer+"\n62\n256\n370\n-1\n6\nByLayer\n10\n")
    w_file.write(str(point[0]) + "\n20\n" + str(point[1]) + "\n30\n0.0\n") 
    w_file.write("40\n" + str(txt_hght) + "\n41\n100.0\n71\n8\n72\n0\n1\n")
    w_file.write(text + "\n7\nnormallatin1\n50\n0.0\n73\n1\n44\n1.0\n0\n")

def draw_line(ob_id,point1,point2,layer,w_file):
    w_file.write("LINE\n5\n" + str(ob_id) + "\n100\nAcDbEntity\n100\n")
    w_file.write("AcDbLine\n8\n"+layer+"\n62\n256\n370\n-1\n6\nByLayer\n10\n")
    w_file.write(str(point1[0]) + "\n20\n" +str(point1[1]) + "\n30\n0.0\n11\n")
    w_file.write(str(point2[0]) + "\n21\n" +str(point2[1]) + "\n31\n0.0\n0\n")
		
def draw_circle(ob_id,point,radius,layer,w_file):
    w_file.write("CIRCLE\n5\n" + str(ob_id) + "\n100\nAcDbEntity\n100\n")
    w_file.write("AcDbCircle\n8\n"+layer+"\n62\n256\n370\n-1\n6\nByLayer\n10\n")
    w_file.write(str(point[0]) + "\n20\n" +str(point[1]) + "\n40\n" +str(radius)+ "\n0\n")