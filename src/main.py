from textnode import *
import os 
import shutil
import re

def copy_to_public():
    #code to create the public directory 
    curr_dir = os.listdir
    current_directory = os.getcwd()
    parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
    print(parent_directory)
    public_directory = os.path.join(parent_directory,"public/")
    print(public_directory)
    print(os.listdir(public_directory))
    shutil.rmtree(public_directory)
    os.makedirs(public_directory)
    print(os.listdir(public_directory))
    #get static directory 
    static_directory = os.path.join(parent_directory, "static/")

    #code to transfer all info from static to public
    explore_file_tree(static_directory, public_directory)

def explore_file_tree(curr_dir, target_dir):
    view = os.listdir(curr_dir)
    print(view)
    if view == []:
        return 

    for content in view:
        print(content)
        current_path = os.path.join(curr_dir,content)
        print(current_path)
        if os.path.isfile(current_path):
            shutil.copy(current_path, target_dir)
        else:
            #create new path for new directory to copy
            new_target_path = os.path.join(target_dir, content)
            print(new_target_path)
            new_dir = os.mkdir(new_target_path)
            #recurse through the tree
            explore_file_tree(current_path, new_target_path)

def extract_title(markdown):
    
    result = re.findall("^#\s(.+)$", markdown)
    if result == []:
        raise Exception("No header")
    else:
        result = "".join(result)
        print(result)
        result = result.removeprefix("#")
        result = result.strip()
        print(result)
        return result


            
