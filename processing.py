#!/usr/bin/env python

#########################################################################
# This file contains code to draw lines from points given in input file.#
# You can directly execute this file or run with the python interpretor #
# (Eg: python processing.py).                                           #
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

# Importing required files/modules

from data_file import *
from include.functions import *
from include.file_open import *
from math import *
# Defining common used variables.

points=[]
data=[]
object_id=48
index=0
first_line=True
update_ref=False
description=False
shift_fac_count=0
Xref_orig=Xref
Yref_orig=Yref

# Main loop start from here

for line in lines:    
    line=line.strip("\n")
    if line=="":        # If line is empty then skip the line
        shift_fac_count+=1
        index+=1
        first_line=True
        update_ref=True
        continue
    line_data = line.split(col_delm)
    for value in line_data:
        if first_line==True: # Check if there is any description in first line or not
            if is_numeric(value)==False:
                description=True
                break
        else:
            if is_numeric(value)==False:
                print "Error in input file: point co-ordinates are not numeric"
                exit(1)             
    
    # Store variables specific to line under processing    
    if first_line==True and description==True: # if description is given
        first_line=False
        data.append({})
        points.append([])
        data[index]['type']=line_data[0]
        data[index]['text']=line_data[1]
        data[index]['show_line']=line_data[2]
        data[index]['layer']=line_data[3]
        description=False
        continue
    elif first_line==True and description==False: # if description is not given
        first_line=False
        data.append({})
        points.append([])
        data[index]['type']="L"  # take line as default
        data[index]['text']="No TEXT"
        data[index]['show_line']="1"
        data[index]['layer']="0"
    
    # Update ref variables if required
    if mode==1 and update_ref==True:
        update_ref=False
        if shift_fac_count==shift_factor:
            if shift_direction==0:
                Xref=Xref_orig
                Yref+=shiftY
                shift_fac_count=0
            else:
                Yref=Yref_orig
                Xref+=shiftX
                shift_fac_count=0
        else:
            if shift_direction==0:
                Xref+=shiftX
            else:
                Yref+=shiftY
    
    # Store line points in list
    if mode==0:
        x=float(line_data[x_col])*scaleX
        y=float(line_data[y_col])*scaleY
    else:
        x=(Xref+float(line_data[x_col]))*scaleX
        y=(Yref+float(line_data[y_col]))*scaleY
    
    if data[index]['type']=="L":
        points[index].append([x,y])
    elif data[index]['type']=="C":
        r=float(line_data[r_col])
        points[index].append([x,y,r])
    elif data[index]['type']=="A":
        sa=float(line_data[s_col])
        ea=float(line_data[e_col])
        r=float(line_data[r_col])
        points[index].append([x,y,r,sa,ea])
    
# End of main loop

# Following loop draws lines if L is the type or circles if C is the type

index=0
for line_points in points:
    i=0
    if data[index]['type']=="L":
        while i<(len(line_points)-1):
            x1=line_points[i][0]
            y1=line_points[i][1]
            x2=line_points[i+1][0]
            y2=line_points[i+1][1]
            if data[index]['show_line']=="1":
                draw_line(object_id,[x1,y1],[x2,y2],data[index]['layer'],out_file)
                object_id+=1
            i+=1 
    elif data[index]['type']=="C":
        while i<len(line_points):
            x=line_points[i][0]
            y=line_points[i][1]
            r=line_points[i][2]
            if data[index]['show_line']=="1":
                draw_circle(object_id,[x,y],r,data[index]['layer'],out_file)
                object_id+=1
            i+=1

    elif data[index]['type']=="A":
        while i<len(line_points):
            x=line_points[i][0]
            y=line_points[i][1]
            r=line_points[i][2]
            s=line_points[i][3]
            e=line_points[i][4]
            if data[index]['show_line']=="1":
                draw_arc(object_id,[x,y],r,s,e,data[index]['layer'],out_file)
                object_id+=1
            i+=1
    index+=1  

# Following loop draws text if given by user in first line    
index=0
for line_data in data:
    if line_data['text']=="NO TEXT" or line_data['show_line']=="0":
        index+=1
        continue
    else:
        x_values=[]
        y_values=[]
        
        if data[index]['type']=="L": # text for Lines
            for point in  points[index]:
                x_values.append(float(point[0]))
                y_values.append(float(point[1]))
        
        elif data[index]['type']=="C": # text for Circles
            for point in  points[index]:
                x_values.append(float(point[0]))
                y_values.append(float(point[1])-float(point[2]))
        
        elif data[index]['type']=="A": # text for Arcs
            for point in  points[index]:
                x=float(point[0])
                y=float(point[1])
                radius=float(point[2])
                st_angle=float(point[3])
                x1=radius*cos(radians(st_angle)) + x
                y1=radius*sin(radians(st_angle)) + y
                end_angle=float(point[4])
                x2=radius*cos(radians(end_angle)) + x
                y2=radius*sin(radians(end_angle)) + y
                print "\n",x,y,radius,st_angle,x1,y1,end_angle,x2,y2

                if(st_angle > end_angle):
                    print "s>e"
                    if((0<=st_angle<=90 and 0<=end_angle<=90) or
                       (90<=st_angle<=180 and 90<=end_angle<=180) or
                       (180<=st_angle<=270 and 180<=end_angle<=270) or
                       (270<=st_angle<=360 and 270<=end_angle<=360)):
                        finalX = x
                        finalY = y-radius
                        print "cond1-4"
                    elif(90<=st_angle<=180 and 0<=end_angle<=90):
                        finalX = x
                        finalY = y-radius
                        print "cond5"
                    elif(180<=st_angle<=270 and 90<=end_angle<=180):
                        finalX = (min([x1,x2])+(x+radius))/2
                        finalY = y-radius
                        print "cond6"
                    elif(270<=st_angle<=360 and 180<=end_angle<=270):
                        finalX = x
                        finalY = min([y1,y2])
                        print "cond7"
                    elif(270<=st_angle<=360 and 0<=end_angle<=90):
                        finalX = (min([x1,x2])+(x+radius))/2
                        finalY = y1
                        print "cond8"
                    elif(180<=st_angle<=270 and 0<=end_angle<=90):
                        finalX = (x1+(x+radius))/2
                        print "y:",y," r:",radius
                        finalY = y-radius
                        print "cond9"
                    elif(270<=st_angle<=360 and 90<=end_angle<=180):
                        finalX = ((x+radius)+x2)/2
                        finalY = y1
                        print "cond10"
                else:
                    print "s<=e"
                    if((0<=st_angle<=90 and 0<=end_angle<=90) or
                       (90<=st_angle<=180 and 90<=end_angle<=180) or
                       (180<=st_angle<=270 and 180<=end_angle<=270) or
                       (270<=st_angle<=360 and 270<=end_angle<=360)):
                        finalX = (x1+x2)/2
                        finalY = min([y1,y2])
                        print "cond1-4"
                    elif(90<=end_angle<=180 and 0<=st_angle<=90):
                        finalX = (x1+x2)/2
                        finalY = min([y1,y2])
                        print "cond5"
                    elif(180<=end_angle<=270 and 90<=st_angle<=180):
                        finalX = (max([x1,x2])+(x-radius))/2
                        finalY = y2
                        print "cond6"
                    elif(270<=end_angle<=360 and 180<=st_angle<=270):
                        finalX = (x1+x2)/2
                        finalY = y-radius
                        print "cond7"
                    elif(270<=end_angle<=360 and 0<=st_angle<=90):
                        finalX = (max([x1,x2])+(x-radius))/2
                        finalY = y-radius
                        print "cond8"
                    elif(180<=end_angle<=270 and 0<=st_angle<=90):
                        finalX = (x1+(x-radius))/2
                        finalY = y2
                        print "cond9"
                    elif(270<=end_angle<=360 and 90<=st_angle<=180):
                        finalX = ((x-radius)+x2)/2
                        finalY = y-radius
                        print "cond10"
                print(finalX, finalY)
                x_values.append(finalX)
                y_values.append(finalY)

        print "x_values:",x_values
        print "y_values:",y_values
        minX=min(x_values)
        maxX=max(x_values)
        meanX=(minX+maxX)/2.0
        minY=min(y_values)
        Xtxt=meanX
        Ytxt=minY - txt_sp
        draw_text(object_id,[Xtxt,Ytxt],txt_hght,line_data['text'],line_data['layer'],out_file)
        object_id+=1
        index+=1
        
if sys.argv[0]=="processing.py":
    from include.file_close import *
    
