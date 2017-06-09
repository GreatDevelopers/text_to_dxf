#!/usr/bin/env python

#########################################################################
# This is the main processing file. Run this file to generate output    #
# dxf file. You can directly execute this file or run with the python   #
# interpretor (Eg: python text_to_dxf.py).                              #
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

# Open various required files

from include.file_open import *

# Import data from data file

from data_file import *

# Import definitions of functions

from include.functions import *

# Writing text to output file to draw lines and corresponding text

from processing import *

# Finally closes all open files 

from include.file_close import *

	
