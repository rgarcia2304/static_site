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
    
    def test_paragraphs(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = block_to_html(markdown)
        self.assertEqual(
            node,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = block_to_html(md)
        self.assertEqual(
            node,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

    def test_quoteblock(self):
        md = """
>Hi my name is Rodrigo
>
>I like to Eat Pizza
"""
    result = block_to_html(md)
    self.assertEqual(
            result,
            "<div><quote>Hi my name is Rodrigo I like to Eat Pizza 
if __name__ == "__main__":
    unittest.main()
