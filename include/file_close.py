#########################################################################
# This file contains code to close various opened files used in the     #
# script.                                                               #
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

from file_open import *

# Write footer file to output file	

out_file.write(foot_data)

# Closes all opened files

out_file.close()
in_file.close()
hd_file.close()
ft_file.close()	
