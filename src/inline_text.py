from textnode import *
import re 
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    #do initial loop to find where delims start and end 
    new_nodes_text_nodes = []
    
    for node in old_nodes:
        
        if node.text_type != TextType.TEXT:
            new_nodes_text_nodes.append(node)
            break

        #split node text in to seperate strings
        split_string_node = node.text.split(delimiter)
        individual_list = []
        for i in range(len(split_string_node)):
            if split_string_node[i] == '' or "" or None:
                pass

            elif i % 2 == 0:
                individual_list.append(TextNode(split_string_node[i], TextType.TEXT))
            else:
                individual_list.append(TextNode(split_string_node[i], text_type))
        
        new_nodes_text_nodes.extend(individual_list)
    return new_nodes_text_nodes

def extract_markdown_images(text):
    expr = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)    
    return expr

def extract_markdown_links(text):
    expr = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return expr
        

def main():
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    print(matches)
main()

