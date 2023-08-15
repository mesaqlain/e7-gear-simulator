import sys
import os

def set_directory():
    """Function to add parent directory to the path to load modules"""
    
    # Get the path of the directory containing this script or notebook
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Calculate the parent directory's path
    parent_dir = os.path.dirname(current_dir)

    # Add the parent directory to the path
    sys.path.insert(0, parent_dir)