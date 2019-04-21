import os
import glob
import re
import os.path
#from shutil import copyfile
from django.shortcuts import render

DEBUG = True


#
# Generate files names with '.html' suffix
#
# Input:
#   odir: A directory added to a prefix to create a base file path
#   prefixes: a word which is prefixed by odir and '.html' appended
#
# Ouptuts:
#   a dictionary. The key is a 'prefix' and the value is a html file name
#
# Note: Prior to Templating, this method require output_dir be prefixed to each filename
#       However, with Templating, test confirmed output_dir was not required
#
def getFileNames(content_dir):
    outputs={} # key = page prefix value = filename
    
    if DEBUG: 
        print("DEBUG: utils.py.getFilenames()")
        print("DEBUG: utils.py.getFilenames.content_dir()", content_dir)        

    # Get Content Files
    content_files=getContentFiles(content_dir)
    
    if DEBUG: 
        print("DEBUG: utils.py.getPath().content_files=", content_files)
    
    # Get list of unique content filename prefixes => filename upto '_'
    prefixes=getPrefixes(content_files)
        
    if DEBUG: 
        print("DEBUG: utils.py.getPath().prefixes=", prefixes)
    
    # Remove the base templatefile
    prefixes.remove('base')
    
    # Create the final prefix.
    for prefix in prefixes:
        outputs[prefix]= "/" + prefix + "/"
        
    if DEBUG:
        print("DEBUG: utils.py.getPath().outputs:", outputs)
        
    return outputs


#
# Return files in specified directory
#
# Input: Directory to be searched for files
#
# Return:  
#   A list if file names
#
def getContentFiles(content_dir):
    content_files=[]
    
    # get all html files
    glob_dir = "".join(content_dir) + "*.html"
    content_files=glob.glob(glob_dir)
    if DEBUG:
        print("DEBUG: utils.py.getContentFiles().content files=", content_files)
        print("DEBUG: utils.py.getContentFiles().content_dir=", content_dir)        

    return content_files
    
    
#
#   Get the prefix of a string. where the prefix is seperated by '_'
#
#   Input:
#       List of files
#
#   Return:
#       List of prefixes       
#
def getPrefixes(strings):
    prefixes=[]   #  file name prefixes help group content files by page
    
    #  list of unique filenam prefixes => filename upto '_'
    for file_path in strings:
        if DEBUG:
            print("DEBUG: utils.py.getPrefixes().filepath=", file_path)        
        
        file_path= os.path.basename(file_path)
        file_prefix,ext=  os.path.splitext(file_path)
        
        if DEBUG:
            print("DEBUG: utils.py.getPrefixes().file_prefix=", file_prefix)
            
        # if there is no '_' do nothing
        try:
            if file_prefix not in prefixes:
                prefixes.append(file_prefix)
                if DEBUG:
                    print("DEBUG: utils.py.getPrefixes().prefixes=", prefixes)
        except ValueError:
            pass
    return prefixes
