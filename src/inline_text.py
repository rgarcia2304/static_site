from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    #do initial loop to find where delims start and end 
    
    modified_string_node_list = []
    for node in old_nodes:

        #modify the strings of each of the old nodes and save the strings 
        modified_string = ""
        for text in node.text:
            if text == delimiter:
                modified_string += text + "#"
            else:
                modified_string += text

        modified_string_node_list.append(modified_string)

    print(modified_string_node_list)

    #Now we have a string of nodes we will potentially make into new nodes
    
    new_nodes_list = []
    for string_node in modified_string_node_list:
        #split the string_node by the delimeter
        after_split_string = string_node.split(delimiter)
        new_nodes_list.append(after_split_string)
    
    print(new_nodes_list)

    #Now we have the full list of split nodes
    final_nodes_list = []
    delim = False
    agg = ""

    for node in new_nodes_list:
        for word in node:
            print(word[0])
            if '#' == word[0] and delim == False:
                delim = True
                new_added_node = TextNode(word.strip("#"), text_type)
                final_nodes_list.append(new_added_node)
            else:
                delim = False
                new_added_node = TextNode(word.strip("#"), TextType.TEXT)
                final_nodes_list.append(new_added_node)


    print(final_nodes_list)

    return final_nodes_list




def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
main()
