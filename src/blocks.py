from textnode import *


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

        clean_block = split_blocks[block].strip(" ")
        cleaned_blocks.append(clean_block)


    final_blocks = []

    for block in cleaned_blocks:
        if block != "":
            final_blocks.append(block)
    
    return final_blocks


def main():
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

    blocks = markdown_to_blocks(md)
    print(blocks)

main()
