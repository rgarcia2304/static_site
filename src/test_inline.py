import unittest

from inline_text import *

class TestInline(unittest.TestCase):
    def test_simple(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                         ]
        self.assertEqual(expected, new_nodes)

    def test_delimiter_non_TextType_Text(self):
        node = TextNode("This is blah blah", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
                TextNode("This is blah blah", TextType.BOLD),
                ]
        self.assertEqual(expected, new_nodes)
    def test_multiple(self):
        node4 = TextNode("This is text with a **code block** word", TextType.TEXT)
        node5 = TextNode("Haha ha **ha** ha **ha**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node4,node5], "**", TextType.BOLD)
        expected = [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
                TextNode("Haha ha ", TextType.TEXT),
                TextNode("ha", TextType.BOLD),
                TextNode(" ha ", TextType.TEXT),
                TextNode("ha", TextType.BOLD),
                         ]
        self.assertEqual(expected, new_nodes)


if __name__ == "__main__":
    unittest.main()

