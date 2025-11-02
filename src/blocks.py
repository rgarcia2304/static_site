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
        return BlockType.HEADER

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
    test_unordered_list = re.findall(r'^[-+*]\s+.+', markdown)
    if test_unordered_list:
        return BlockType.UNORDERED_LIST

    # ordered list (one or more digits, dot, space, then text)
    test_ordered_list = re.findall(r'^\s*\d+\.\s+(.+)$', markdown)
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
    if block_type == BlockType.PARAGRAPH:
        return 'p'
    if block_type == BlockType.HEADING:
        #count the number of #'s
        return count_header_size(block)
    
    if block_type == BlockType.QUOTE:
        return 'quote'

    if block_type == BlockType.UNORDERED_LIST:
        return 'ul'

    if block_type == BlockType.ORDERED_LIST:
        return 'ol'
        

    return lst_html_nodes

def convert_listblock_to_nodes(block,parent_node):

    #first things first split the block by new line
    new_list_block = block.split("\n")

    #now with this block convert each of these into html_nodes
    lst_of_html_nodes = []
    for entry in new_list_block:
        new_list_leaf_node = LeafNode("li", entry)
        lst_of_html_nodes.append(new_list_leaf_node)
    
    return lst_of_html_nodes
    
def count_header_size(block):
    
    count = 0
    while char in block == "#":
        count += 1 

    return f"h{count}" 
    

def block_to_html(markdown):

    #split the markdown into blocks
    converted_blocks = markdown_to_blocks(markdown)

    lst_of_parent_nodes = []
    #loop throught the converted blocks 
    for block in converted_blocks:
        

        #get the block information,will eventually have this become the parent node 
        block_type = block_to_block_type(block)
        #convert this block into block_tag
        block_tag = block_type_to_tag(block_type, block)

        if block_tag == BlockType.ORDERED_LIST:
            #going to need to convert the block of the list into text nodes 
            list_nodes = list_block_to_nodes(block)
            parent_node = ParentNode(block_tag, list_nodes, None)
            lst_of_parent_nodes.append(parent_node)

        elif block_tag != BlockType.CODE:
            
            #convert the block into text nodes 
            block_to_text_nodes = text_to_textnodes(block)
            
            children = block_text_to_html_nodes(block_to_text_nodes)
            #ok so now we have the children so set the dad 
            parent_node = ParentNode(block_tag, children)
            lst_of_parent_nodes.append(parent_node)
        
        else:
            new_child_node = TextNode(block, TextType.CODE)
            new_html_node = text_node_to_html_node(new_child_node)
            parent_to_html_single = ParentNode('pre', [new_html_node], None)
            the_father_node_for_code = ParentNode('div', [parent_to_html_single], None)
            return the_father_node_for_code

    #ok so now we the parent nodes
    the_father_node = ParentNode('div', lst_of_parent_nodes, None)
    final_representation = the_father_node.to_html()

    print(final_representation) 
    return the_father_node


def main():
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = block_to_html(md)
    
main()
