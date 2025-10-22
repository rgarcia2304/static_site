import unittest


from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        dict2 = {
    "href": "https://www.google.com",
    "target": "_blank",
}
        
        
        node = HTMLNode(props=dict2)
        txt = node.props_to_html()
        
        expected2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected2, txt)
        
        node5 = HTMLNode(props=dict2)
        txt5 = node5.props_to_html()
        
        expected2 = ' href="https://www.google.com"  target="_blank"'
        self.assertNotEqual(expected2, txt5)
        
        node2 = HTMLNode(tag="p", value="hello", children=None, props=dict2)
        props2 = repr(node2.props)

        expected_txt = (
    f'tag- p value- hello children- None props- {props2}'
)

        self.assertEqual(repr(node2), expected_txt)
        
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()
