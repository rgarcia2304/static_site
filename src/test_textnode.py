import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("txtn3", TextType.ITALIC, TextType.BOLD)
        node4 = TextNode("txt4", TextType.ITALIC, TextType.ITALIC)
        self.assertNotEqual(node3, node4)
        

        node5 = TextNode("txtn3", TextType.ITALIC, TextType.BOLD)
        node6 = TextNode("txtn3", TextType.ITALIC, TextType.BOLD)
        self.assertEqual(node5, node6)

        node7 = TextNode("txtn3", TextType.ITALIC, "phub.com")
        node8 = TextNode("txtn3", TextType.ITALIC, "phub.com")
        self.assertEqual(node7, node8)



if __name__ == "__main__":
    unittest.main()

