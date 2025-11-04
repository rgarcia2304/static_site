from textnode import *
import re 
from htmlnode import *
from inline_text import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    #split blocks based on new_lines
    split_blocks = markdown.split("\n\n")
    
    #print(split_blocks)

    cleaned_blocks = []

    for block in range(len(split_blocks)):
        if block == 0:
            #print(split_blocks[block])
            prefix_to_remove = "\n"
            #print(split_blocks)
            split_blocks[block] = split_blocks[block].removeprefix(prefix_to_remove)
            #print(split_blocks)

    
        #also remove trailing backspaces for last
        if block == len(split_blocks)-1:
            suffix_to_remove = "\n"
            split_blocks[block] = split_blocks[block].removesuffix(suffix_to_remove)

        clean_block = split_blocks[block].strip()
        cleaned_blocks.append(clean_block)
        


    final_blocks = []

    for block in cleaned_blocks:
        if block != "":
            final_blocks.append(block)
    
    return final_blocks 

def block_to_block_type(markdown):
    # header
    test_header = re.findall(r'^#{1,6}(?:\s+.+|$)', markdown)
    if test_header:
        return BlockType.HEADING

    # code fence (opening or closing ``` with optional language)
    test_code = re.findall(r'^```', markdown,flags=re.MULTILINE)
    if test_code:
        return BlockType.CODE

    #case where code can be found in one line
    if re.match(r'^```.*```$', markdown):
        return BlockType.CODE

    # blockquote
    test_quote = re.findall(r'^>\s?.*', markdown)
    if test_quote:  # FIX: was inverted before
        return BlockType.QUOTE

    # unordered list (-, +, or * followed by space and text)
    test_unordered_list = re.findall(r'^[-+*]\s+.+', markdown,flags = re.MULTILINE)
    if test_unordered_list:
        return BlockType.UNORDERED_LIST

    # ordered list (one or more digits, dot, space, then text)
    test_ordered_list = re.findall(r'^\s*\d+\.\s+(.+)$', markdown, flags = re.MULTILINE)
    print("------------")
    print(test_ordered_list)
    print("-------------")

    if test_ordered_list:
        return BlockType.ORDERED_LIST

    # default
    return BlockType.PARAGRAPH 

def block_text_to_html_nodes(text_nodes):
    lst_html_nodes = []
    
    "THIS IS THE TEXT NODE CURRENTLLY"
    for block_node in text_nodes:

        lst_html_nodes.append(text_node_to_html_node(block_node))
    
    return lst_html_nodes

def block_type_to_tag(block_type, block):
    print(block_type)

    if block_type == BlockType.PARAGRAPH:
        return "p"
    elif block_type == BlockType.HEADING:
        #count the number of #'s
        return count_header_size(block)
    
    elif block_type == BlockType.QUOTE:
        return "blockquote"

    elif block_type == BlockType.UNORDERED_LIST:
        return "ul"

    elif block_type == BlockType.ORDERED_LIST:
        return "ol"
    
    elif block_type == BlockType.CODE:
        return "code"
        

def list_block_to_nodes(block, block_type):

    #first things first split the block by new line
    new_list_block = block.split("\n")

    #now with this block convert each of these into html_nodes
    lst_of_html_nodes = []
    
    if block_type == BlockType.UNORDERED_LIST:

        for entry in new_list_block:    
            entry = entry.strip("-")
            entry = entry.strip()
            new_list_leaf_node = LeafNode("li", entry)
            lst_of_html_nodes.append(new_list_leaf_node)

    else: # case for ordered list
        print("HELLLO")
        for entry in new_list_block:
            print(entry)
            entry = re.sub("(?m)^\s*\d+[.)]\s*", "", entry)
            print(entry)
            entry = entry.strip()
            new_list_leaf_node = LeafNode("li", entry)
            lst_of_html_nodes.append(new_list_leaf_node)

    print(lst_of_html_nodes)
    return lst_of_html_nodes
    
def count_header_size(block):
    
    count = 0
    
    for char in block:
        if char == "#":
            count += 1

        if char != "#":
            break

    
    return f"h{count}" 
    

def block_to_html(markdown):

    #split the markdown into blocks
    converted_blocks = markdown_to_blocks(markdown)
    print(converted_blocks)
    lst_of_parent_nodes = []
    #loop throught the converted blocks 
    for block in converted_blocks:
        

        #get the block information,will eventually have this become the parent node 
        #print("------------")
        #print("THIS IS THE BLOCK TYPE")
        
        block_type = block_to_block_type(block)
        #print(block_type)
        #print("-------------")
        #convert this block into block_tag
        block_tag = block_type_to_tag(block_type, block)
        #print("THIS IS THE BLOCK TAG")
        #print(block_tag)
        #print("---------------------")
        #print(block_tag == BlockType.CODE)
        #print(BlockType.CODE)
        if block_type == BlockType.ORDERED_LIST or block_type == BlockType.UNORDERED_LIST:
            #going to need to convert the block of the list into text nodes 
            
            print("I AM A LIST")
            list_nodes = list_block_to_nodes(block, block_type)
            parent_node = ParentNode(block_tag, list_nodes, None)
            lst_of_parent_nodes.append(parent_node)

        elif block_type != BlockType.CODE:
        
            # Normalize hard line breaks inside a paragraph to spaces
            if block_type == BlockType.PARAGRAPH:
                block = " ".join(block.splitlines())

                block_to_text_nodes = text_to_textnodes(block)
                children = block_text_to_html_nodes(block_to_text_nodes)
                parent_node = ParentNode(block_tag, children)
                lst_of_parent_nodes.append(parent_node) 

            elif block_type == BlockType.QUOTE:
                block = block.strip(">")
                block= block.replace("\n>","\n")
                block_to_text_nodes = text_to_textnodes(block)
                children = block_text_to_html_nodes(block_to_text_nodes)
                parent_node = ParentNode(block_tag, children)
                lst_of_parent_nodes.append(parent_node)
            
            else:
                # this is the case for the heading 
                #strip the beggining headings
                print(block)
                print(count_header_size(block))
                prefix_to_remove = count_header_size(block)[-1]
                pf = "#" * int(prefix_to_remove)
                block = block.strip(pf)
                block = block.strip()
                block_to_text_nodes = text_to_textnodes(block)
                children = block_text_to_html_nodes(block_to_text_nodes)
                parent_node = ParentNode(block_tag, children)
                lst_of_parent_nodes.append(parent_node)
                    
        elif block_type == BlockType.CODE:
            #print("HELLO WE ARE CODE")
            block = block.strip("```")
            #also strip the beggining and ending new lines
            prefix_to_remove = "\n"
            block = block.removeprefix(prefix_to_remove)
            new_child_node = TextNode(block, TextType.CODE)
            new_html_node = text_node_to_html_node(new_child_node)
            #print('_----------_')
            #print(new_html_node)
            #print("----------")
            parent_to_html_single = ParentNode('pre', [new_html_node], None)
            the_father_node_for_code = ParentNode('div', [parent_to_html_single], None)
            return the_father_node_for_code.to_html()

    #ok so now we the parent nodes
    the_father_node = ParentNode('div', lst_of_parent_nodes, None)
    final_representation = the_father_node.to_html()
    print(final_representation)
    return final_representation


def main():
    md = """
>Hi my name is Rodrigo
>
>I like to Eat Pizza
"""
    r = block_to_html(md)

main()
