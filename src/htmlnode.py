from textnode import *

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = ''
        
        if self.props is None:
            return None 
        
        for prop in self.props:
            val = self.props[prop]
            html_string +=  ' ' + prop + '=' + '"'+ val + '"' 

        return html_string

    def __repr__(self):
        return f'tag- {self.tag} value- {self.value} children- {self.children} props- {self.props}'

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        
        super().__init__(tag=tag, value=value,children=None, props=props)
        

    def to_html(self):

        if self.value is None:
            raise ValueError

        if self.tag is None:
            return self.value

        else:
            if self.props is None:

                return f'<{self.tag}>{self.value}</{self.tag}>'

            else:
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):

    def __init__(self, tag, children,props = None):

        super().__init__(tag=tag, children = children, props=props, value=None)


    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag")
            
        if self.children is None:
            raise ValueError("No children")
            
        result_string = ""
        for child in self.children:
            print("\n\n\n\n")
            print(child)
            print("im the child --------------")
            result = child.to_html()
            result_string += result
        
        result_string = f'<{self.tag}>{result_string}</{self.tag}>'
            
        return result_string


def text_node_to_html_node(text_node):
    if isinstance(text_node, TextNode):
        if text_node.text_type not in TextType:
            raise Exception("This is not a valid text type")
        

        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)

        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)

        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)

        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)

        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text,{"href": text_node.url})

        elif text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "",{"src":text_node.url, "alt": text_node.text})
        
    raise Exception("NOT A TEXT NODE")


