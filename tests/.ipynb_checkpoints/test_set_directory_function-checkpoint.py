from set_directory_function import * 
import sys

 # Get the first directory in sys.path
parent_dir = sys.path[0] 

if parent_dir in sys.path:
    print("Directory has been added to the path.")
else:
    print("Directory has not been added to the path.")
