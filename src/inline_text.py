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
    print(expr)
    return expr

def extract_markdown_links(text):
    expr = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return expr
        

def split_nodes_image(old_nodes):
    lst_nodes = []
    for node in old_nodes:
        #extract the regex from it
        values_to_split_by = extract_markdown_images(node.text)
        print("HELLO")
        print(f"these are the vals to split by {values_to_split_by}")
        if values_to_split_by is None:
            new_node = TextNode(node.text, TextType.TEXT)
            lst_nodes.append(new_node)
            return lst_nodes
        
        curr_text = node.text
        
        for val in values_to_split_by:
            img = val[0]
            img_link = val[1]
            print(img)
            working_split = curr_text.split(f"![{img}]({img_link})")
            print("ABOVE IS VAL")
            if working_split[0] != None or working_split!= "" or working_split!= '':
                new_node = TextNode(working_split[0], TextType.TEXT)
                lst_nodes.append(new_node)
                new_node_link = TextNode(img, TextType.IMAGE, img_link)
                lst_nodes.append(new_node_link)
                curr_text = working_split[1]

        return lst_nodes

def split_nodes_links(old_nodes):
    lst_nodes = []
    for node in old_nodes:
        #extract the regex from it
        values_to_split_by = extract_markdown_links(node.text)
        print("HELLO")
        print(f"these are the vals to split by {values_to_split_by}")
        if values_to_split_by is None:
            new_node = TextNode(node.text, TextType.TEXT)
            lst_nodes.append(new_node)
            return lst_nodes
        
        curr_text = node.text
        
        for val in values_to_split_by:
            txt = val[0]
            link = val[1]
            working_split = curr_text.split(f"[{txt}]({link})")
            if working_split[0] != None or working_split!= "" or working_split!= '':
                new_node = TextNode(working_split[0], TextType.TEXT)
                lst_nodes.append(new_node)
                new_node_link = TextNode(txt, TextType.LINK, link)
                lst_nodes.append(new_node_link)
                curr_text = working_split[1]

        return lst_nodes

def main():
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    node = TextNode(
        text,
        TextType.TEXT,
    )
    new_nodes = split_nodes_links([node])
    print(new_nodes)

main()

    

