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
is_same_layer=0 # checks if the layer is already declared
layer_color=1 # assigns color to each layer, increments with every new layer
first_line=True
update_ref=False
description=False
shift_fac_count=0
Xref_orig=Xref
Yref_orig=Yref


# Main loop start from here

for line in lines:
    line=line.strip("\n")
    if line=="":
        # New layer starts
        shift_fac_count+=1
        index+=1
        first_line=True
        update_ref=True
        continue

    # Picks up the words like group of numbers or characters
    line_data = line.split(col_delm)
    # Checks the first word in a line
    for value in line_data:
        # Checks if there is any description in first line
        if first_line==True:
            if is_numeric(value)==False:
                description=True
                break
        else:
            # Checks if there isn't any character in first word in lines 
            # execpt first line of each paragraph
            if is_numeric(value)==False:
                print "Error in input file: point co-ordinates are not numeric"
                exit(1)             
    
    # Used for checking if layer is same
    is_same_layer=0
    
    # Store variables specific to line under processing
    if first_line==True:
        first_line=False
        
        # Declare another list inside the list
        data.append({})
        points.append([])
        
        # if description is given
        if description==True:
            data[index]['type']=line_data[0]
            data[index]['text']=line_data[1]
            data[index]['show_line']=line_data[2]
            data[index]['layer']=line_data[3]
            
            #checking if layer is already declared
            for layer in dwg.layers:
                if layer.dxf.name == data[index]['layer']:
                    is_same_layer = 1
            
            #declaring new layer
            if is_same_layer == 0:
                dwg.layers.new(name=data[index]['layer'], dxfattribs={
                    'linetype': 'CONTINUOUS', 'color': layer_color})
                layer_color = layer_color + 1
            description=False
            continue    
        
        # if description is not given
        elif description==False:
            # takes line as default
            data[index]['type']="L"
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
    
    # Saves coordinates of line
    if data[index]['type']=="L":
        points[index].append((x,y))
    
    # Saves coordinates of Circle
    elif data[index]['type']=="C":
        r=float(line_data[r_col])
        points[index].append((x,y,r))
    
    # Saves coordinates of Arc
    elif data[index]['type']=="A":
        sa=float(line_data[s_col])
        ea=float(line_data[e_col])
        r=float(line_data[r_col])
        points[index].append((x,y,r,sa,ea))

    # Saves coordinates of Polyline
    elif data[index]['type']=="P":
        sw = float(line_data[sw_col])
        ew = float(line_data[ew_col])
        bulge = float(line_data[bulge_col])
        points[index].append((x,y,sw,ew,bulge))

    # Saves coordinates of Polyline for Hatch
    elif data[index]['type']=="H":
        bulge = float(line_data[hatch_bulge_col])
        points[index].append((x,y,bulge))


# End of main loop

# Following loop draws lines if L is the type or circles if C is the type

index=0
for line_points in points:
    i=0
    if data[index]['type']=="L":
        while i<(len(line_points)-1):
            if data[index]['show_line']=="1":
                msp.add_line(line_points[i], line_points[i+1], 
                    dxfattribs={'layer': data[index]['layer']})
                object_id+=1
            i+=1 
    
    elif data[index]['type']=="C":
        while i<len(line_points):
            x=line_points[i][0]
            y=line_points[i][1]
            r=line_points[i][2]
            if data[index]['show_line']=="1":
                msp.add_circle((x,y),r , 
                    dxfattribs={'layer': data[index]['layer']})                
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
                msp.add_arc((x,y), r, s, e, 
                    dxfattribs={'layer': data[index]['layer']})                
                object_id+=1
            i+=1
    
    elif data[index]['type']=="P":
        if data[index]['show_line']=="1":
            msp.add_lwpolyline(line_points, 
                dxfattribs={'layer': data[index]['layer']})
            object_id+=1

    elif data[index]['type']=="H":
        if data[index]['show_line']=="1":
            hatch = msp.add_hatch(color= hatch_color, 
                dxfattribs={'layer': data[index]['layer']})
            # edit boundary path (context manager)
            with hatch.edit_boundary() as boundary: 
                # every boundary path is always a 2D element
                # vertex format for the polyline path is: (x, y[, bulge])
                # bulge value 1 = an arc with diameter=10 (= distance to next vertex * bulge value)
                # bulge value > 0 ... arc is right of line
                # bulge value < 0 ... arc is left of line
                boundary.add_polyline_path(line_points, is_closed=1)

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
        
        # text for Lines
        if data[index]['type']=="L": 
            for point in  points[index]:
                x_values.append(float(point[0]))
                y_values.append(float(point[1]))
        
        # text for Circles
        elif data[index]['type']=="C": 
            for point in  points[index]:
                x_values.append(float(point[0])-float(point[2]))
                x_values.append(float(point[0])+float(point[2]))
                y_values.append(float(point[1])-float(point[2]))
        
        # text for Arcs
        elif data[index]['type']=="A": 
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

                if(st_angle > end_angle):
                    if((0<=st_angle<=90 and 0<=end_angle<=90) or
                       (90<=st_angle<=180 and 90<=end_angle<=180) or
                       (180<=st_angle<=270 and 180<=end_angle<=270) or
                       (270<=st_angle<=360 and 270<=end_angle<=360)):
                        x_values.append(x+radius)
                        x_values.append(x-radius)
                        y_values.append(y-radius)
                    elif(90<=st_angle<=180 and 0<=end_angle<=90):
                        x_values.append(x+radius)
                        x_values.append(x-radius)
                        y_values.append(y-radius)
                    elif(180<=st_angle<=270 and 90<=end_angle<=180):
                        x_values.append(x1)
                        x_values.append(x2)
                        x_values.append(x+radius)
                        y_values.append(y-radius)
                    elif(270<=st_angle<=360 and 180<=end_angle<=270):
                        x_values.append(x+radius)
                        x_values.append(x-radius)
                        y_values.append(y1)
                        y_values.append(y2)
                    elif(270<=st_angle<=360 and 0<=end_angle<=90):
                        x_values.append(x+radius)
                        x_values.append(x1)
                        x_values.append(x2)
                        y_values.append(y1)
                    elif(180<=st_angle<=270 and 0<=end_angle<=90):
                        x_values.append(x+radius)
                        x_values.append(x1)
                        y_values.append(y-radius)
                    elif(270<=st_angle<=360 and 90<=end_angle<=180):
                        x_values.append(x+radius)
                        x_values.append(x2)
                        y_values.append(y1)
                else:
                    if((0<=st_angle<=90 and 0<=end_angle<=90) or
                       (90<=st_angle<=180 and 90<=end_angle<=180) or
                       (180<=st_angle<=270 and 180<=end_angle<=270) or
                       (270<=st_angle<=360 and 270<=end_angle<=360)):
                        x_values.append(x1)
                        x_values.append(x2)
                        y_values.append(y1)
                        y_values.append(y2)
                    elif(90<=end_angle<=180 and 0<=st_angle<=90):
                        x_values.append(x1)
                        x_values.append(x2)
                        y_values.append(y1)
                        y_values.append(y2)
                    elif(180<=end_angle<=270 and 90<=st_angle<=180):
                        x_values.append(x1)
                        x_values.append(x2)
                        x_values.append(x-radius)
                        y_values.append(y2)
                    elif(270<=end_angle<=360 and 180<=st_angle<=270):
                        x_values.append(x2)
                        x_values.append(x1)
                        y_values.append(y-radius)
                    elif(270<=end_angle<=360 and 0<=st_angle<=90):
                        x_values.append(x2)
                        x_values.append(x1)
                        x_values.append(x-radius)
                        y_values.append(y-radius)
                    elif(180<=end_angle<=270 and 0<=st_angle<=90):
                        x_values.append(x1)
                        x_values.append(x-radius)
                        y_values.append(y2)
                    elif(270<=end_angle<=360 and 90<=st_angle<=180):
                        x_values.append(x2)
                        x_values.append(x-radius)
                        y_values.append(y-radius)

        # text for Polyline
        # elif data[index]['type']=="P": 
        #     for point in  points[index]:


        # Calculates the position of text
        if x_values!=[] and y_values!=[]:
            minX=min(x_values)
            maxX=max(x_values)
            meanX=(minX+maxX)/2.0
            minY=min(y_values)
            Xtxt=meanX
            Ytxt=minY - txt_sp
            msp.add_text(line_data['text'], dxfattribs={'layer': 
                line_data['layer']}).set_pos((Xtxt,Ytxt), align= 'TOP_CENTER')
            object_id+=1
            index+=1
        
if sys.argv[0]=="processing.py":
    from include.file_close import *
    
