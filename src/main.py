import sys
from textnode import *
import os 
import shutil
import re
from blocks import *

def copy_to_public():
    #code to create the public directory 
    curr_dir = os.listdir
    current_directory = os.getcwd()
    #parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
    #print(parent_directory)
    public_directory = os.path.join(current_directory,"docs")
    #print("THIS IS THE PUBLIC -----")
    #print(public_directory)
    #print(os.listdir(public_directory))
    shutil.rmtree(public_directory)
    os.makedirs(public_directory)
    #print(os.listdir(public_directory))
    #get static directory 
    static_directory = os.path.join(current_directory, "static")

    #code to transfer all info from static to public
    explore_file_tree(static_directory, public_directory)

def explore_file_tree(curr_dir, target_dir):
    view = os.listdir(curr_dir)
    #print(view)
    if view == []:
        return 

    for content in view:
        #print(content)
        current_path = os.path.join(curr_dir,content)
        #print(current_path)
        if os.path.isfile(current_path):
            shutil.copy(current_path, target_dir)
        else:
            #create new path for new directory to copy
            new_target_path = os.path.join(target_dir, content)
            #print(new_target_path)
            new_dir = os.mkdir(new_target_path)
            #recurse through the tree
            explore_file_tree(current_path, new_target_path)

def extract_title(markdown):
  
    match = re.search(r'(?m)^\s*# (.+)$', markdown)
    
    if not match:
        raise Exception("No header")

    return match.group(1).strip()


def generate_page(from_path, template_path, dest_path, base_path):

    print(f'generating page from {from_path} to {dest_path} using {template_path}')
    
    #read all the lines from the markdown file 

    with open(from_path, "r") as file:
        from_line = file.readlines()
    
    with open(template_path, "r") as file:
        template_line = file.read()
    print("-------------------") 
    "".join(from_line)
    md = "".join(from_line)
    print("-----MARKDOWN")
    print("----")
    html_string = block_to_html(md)
    print(html_string)

    #grab the title of the page 
    title = extract_title(md)
    #print("---------")
    #print(md)
    #print("-------")
    print(title)
    
    #now we have to get the template_lines and replace them with 
    template_line = template_line.replace('{{ Title }}', title)
    template_line = template_line.replace('{{ Content }}', html_string)
    template_line = template_line.replace('href="/', f'href="{base_path}')
    template_line = template_line.replace('src="/', f'src="{base_path}')

    with open(dest_path, 'w') as file:
        file.write(template_line)

    print("hello")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):

    #list out items in directory 
    lst_dir = os.listdir(dir_path_content)
    
    if lst_dir == []:
        return 
    
    for item in lst_dir:
        current_path_of_item = os.path.join(dir_path_content, item)
        print("_-------CURRENT PATH of ITEM", current_path_of_item)
        current_dest_path = os.path.join(dest_dir_path, item)
        print("--------CURRENT DESTINATION PATH-----------", current_dest_path)
        if os.path.isfile(current_path_of_item):
            # do the processing of making the file in the target directory
            
            #cut the index.md prefix and make it .html
            current_dest_path = current_dest_path.replace("/index.md","/index.html")
            
            print("CURRENT PATHHH TO WRITE INTO", current_dest_path) 
            generate_page(current_path_of_item, template_path, current_dest_path, base_path)

        else:
            #make new directory at destination
            os.makedirs(current_dest_path)

            #now recursively crawl this 
            generate_pages_recursive(current_path_of_item, template_path, current_dest_path, base_path)


def main():
    
    set_base = ""
    if len(sys.argv) < 2:
        set_base = "/"
    else:
        set_base = sys.argv[1]

    current_directory = os.getcwd()
    copy_to_public()
    content_directory = os.path.join(current_directory,"content")
    
    template_path = os.path.join(current_directory, "template.html")

    #path to write to 
    write_path = os.path.join(current_directory, "docs")

    generate_pages_recursive(content_directory, template_path, write_path, set_base)
main()
