import unittest

from blocks import *

class TestBlocks(unittest.TestCase):
    def test_simple(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_simple_2(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
Hello still here

- This is a list
"""
        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\nHello still here",
                "- This is a list",
            ],
        )




    def test_simple_blocks_to_block_type_paragraph(self):
        text = "hello"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))
    
    
    def test_code_block_to_block_type(self):
        text= "```hello```"
        self.assertEqual(BlockType.CODE, block_to_block_type(text))

    def test_quote_block_to_block_type(self):
        text = "> my name is Rodrigo"
        self.assertEqual(BlockType.QUOTE, block_to_block_type(text))

    def test_unoredered_list(self):
        text = "- hello my name is Joe"
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(text))

    def test_ordered_list(self):
        text = "1. my name is Joe"
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(text))

if __name__ == "__main__":
    unittest.main()
