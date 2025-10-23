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

        node_2 = LeafNode("p", "a car?")
        self.assertNotEqual(node_2.to_html(), "<p> a car?</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()

        
        self.assertEqual(node, '<a href="https://www.google.com">Click me!</a>')
    

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>",)
    
    def test_to_html_with_many_grandchilden(self):
        grandchild_node1 = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("b", "grandchild")
        grandchild_node3 = LeafNode("b", "grandchild")
        child_node_1 = ParentNode("span", [grandchild_node1, grandchild_node2, grandchild_node3])
        parent_node = ParentNode("div", [child_node_1])
        html_str = "<div><span><b>grandchild</b><b>grandchild</b><b>grandchild</b></span></div>"
        self.assertEqual(parent_node.to_html(), html_str)


    def test_to_html_with_many_children(self):
        child_node = LeafNode("span", "child")
        child2_node = LeafNode("p", "child1")
        child3_node = LeafNode("p", "child2")
        parent_node = ParentNode("div", [child_node, child2_node, child3_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><p>child1</p><p>child2</p></div>")
    
    def test_parent_with_no_children(self):
        parent_node = ParentNode("span", [])
        self.assertEqual(parent_node.to_html(), "<span></span>")

    def test_generations_with_children(self):
        child_node = LeafNode("h1", "hello")
        g1 = ParentNode("p", [child_node])
        g2 = ParentNode("p", [g1])
        g3 = ParentNode("p", [g2])
        g4 = ParentNode("p", [g3])
        b_node = ParentNode("div", [])
        c_node = ParentNode("h1", [])
        daddy_node = ParentNode("div",[g4, b_node, c_node])
        expected_html = "<div><p><p><p><p><h1>hello</h1></p></p></p></p><div></div><h1></h1></div>"
        self.assertEqual(daddy_node.to_html(), expected_html)

    def test_many_children_with_no_children(self):
        child1 = ParentNode("p", [])
        child2 = ParentNode("div",[])
        parent = ParentNode("div",[child1,child2])
        expected_html = "<div><p></p><div></div></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
