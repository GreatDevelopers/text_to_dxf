text_to_dxf README:
--------------------------

This software converts the specifications to draw lines into .dxf format.
You just need to specify co-ordinates of points of figures. Program will
automatically join all the points (with lines) to draw figure.
You can use combination of points to draw many type of figures such as 
triangle, quadrilateral, polygon etc. Also you can draw as many figures 
you want using only one input file. 
Please see section "Input File Format" below for input file specification. 
If you export spreadsheet as input file then use "Enter" (Newline) as line
separator. Lines in input file which do not have valid (numeric) data at 
required columns would be skipped while processing.   

NOTE:   Data is required at all columns. But you can skip the figure 
        description rows.



REQUIREMENTS:
----------------------------

This software is totally written in Python. So Python interpretor should be
installed correctly in your system. Also be sure that python binary is in your
system path (to be accessed easily). To test the output of this software any
CAD software compatible with dxf format should be installed such as AutoCAD,
QCAD etc.



INPUT FILE FORMAT:
----------------------------

Your input text file should be written in following way. Optional lines are 
surrounded by square brackets ([]). Also here comma (,) is taken as column 
delimiter for demonstration. In practice you can use any column delimiter
of your choice.

############### Start of file ###############
[Figure-1 description,show figure code,layer name]
point-1 co-ordinates
point-2 co-ordinates
point-3 co-ordinates
.
.
.
point-n co-ordinates

[Figure-2 description,show figure code,layer name]
point-1 co-ordinates
point-2 co-ordinates
point-3 co-ordinates
.
.
.
point-n co-ordinates

-
-
-
-

[Figure-n description,show figure code,layer name]
point-1 co-ordinates
point-2 co-ordinates
point-3 co-ordinates
.
.
.
point-n co-ordinates
############### End of File ###############

Details:

Here, 
Figure description - text shown at botton of figure. Text drawn is bottom
centric to the point whose x co-ordinate is mean of largest and smallest
x co-ordinates and y co-ordinate is the smallest y co-ordinate - txt_sp 
(defined in data file) of points constituting the figure.

show figure code - 1 to show (draw) figure and optional text   
                   0 to hide (don't draw) figure and optional text
                 
layer name - Name of layer on which figure and its optional text is
             drawn. Currently 5 layers are defined inside the program.
             So, you can use any value between 0-5.

point co-ordinates - co-ordinates of point separated by column delimiter
                     (comma in above case). You can specify co-ordinates
                     in any order i.e x,y,z or y,x,z etc. But sequence should
                     be same for all figures. Also you need to mention 
                     the co-ordinates order in the data_file.py. Please
                     note that z co-ordinate is not used in the program
                     so you can give only x and y co-ordinates

Note:   Figure specifications need to be separated by Empty line.

Note:   See samples folder for sample files. You will find python
        scripts to generate coordinates, text files containing co-ordinates
        and dxf files showing output of these samples. Redirect output of python
        script to file and use that file as input to this program.  



UASGE:
----------------------------

Extract the package files then cd to extracted directory. Then to run 
the script you can use any one of following commands:

              #python text_to_dxf.py <inputfile> <outputfile>
                       OR
              #./text_to_dxf.py <inputfile> <outputfile>

Here, <inputfile> is the source .csv file (text file) and <outputfile> is 
resultant .dxf file to be generated. Change the values of various variables
defined in data_file.py file according to your requirement.


NOTE:    Be sure that you must have write permission in the directory
         where outputfile is to be generated.

Enjoy.......Have Fun.!!



AUTHORS:
----------------------------

Vikas Mahajan
Website: http://vikasmahajan.wordpress.com
Email: vikas.mahajan12@gmail.com

