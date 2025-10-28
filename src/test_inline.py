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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_images_large(self):
        text = "Hi ![image](https://www.google.com) hello ![image](https://www.toyota.com) hallo![image](https://www.techcrunch.com) bonjour"
        node = TextNode(
                text,
                TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Hi ",TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://www.google.com"),
                TextNode(" hello ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://www.toyota.com"),
                TextNode(" hallo", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://www.techcrunch.com"),
                TextNode(" bonjour", TextType.TEXT),

            ],
            new_nodes
        )

    def test_no_images(self):
        text = "Hi (https://www.google.com) hello (https://www.toyota.com) hallo[image](https://www.techcrunch.com) bonjour"
        node = TextNode(
            text,
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("Hi (https://www.google.com) hello (https://www.toyota.com) hallo[image](https://www.techcrunch.com) bonjour",TextType.TEXT)],
            new_nodes
        )

    def test_multi_split_images(self):
        text = "Hi ![image](https://burgerking.com) whopper"
        text2 = "hi ![image](https://mcdonalds.com) bigmac"
        node = TextNode(
                text,
                TextType.TEXT,
        )

        node2 = TextNode(
                text2,
                TextType.TEXT,
        )

        new_nodes = split_nodes_image([node, node2])

        self.assertListEqual(
            [
                TextNode("Hi ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://burgerking.com"),
                TextNode(" whopper", TextType.TEXT),
                TextNode("hi ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://mcdonalds.com"),
                TextNode(" bigmac", TextType.TEXT),

            ],
            new_nodes
        )


    def test_no_links(self):
        text = "Hi (https://www.google.com) hello (https://www.toyota.com) hallo(image](https://www.techcrunch.com) bonjour"
        node = TextNode(
            text,
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [TextNode("Hi (https://www.google.com) hello (https://www.toyota.com) hallo(image](https://www.techcrunch.com) bonjour",TextType.TEXT)],
            new_nodes
        )

    def test_split_links_large(self):
        text = "Hi [link1](https://www.google.com) hello [link2](https://www.toyota.com) hallo[link3](https://www.techcrunch.com) bonjour"
        node = TextNode(
                text,
                TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("Hi ",TextType.TEXT),
                TextNode("link1", TextType.LINK, "https://www.google.com"),
                TextNode(" hello ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "https://www.toyota.com"),
                TextNode(" hallo", TextType.TEXT),
                TextNode("link3", TextType.LINK, "https://www.techcrunch.com"),
                TextNode(" bonjour", TextType.TEXT),

            ],
            new_nodes
        )
    def test_multi_split_links(self):
        text = "Hi [link2](https://burgerking.com) whopper"
        text2 = "hi [link1](https://mcdonalds.com) bigmac"
        node = TextNode(
                text,
                TextType.TEXT,
        )

        node2 = TextNode(
                text2,
                TextType.TEXT,
        )

        new_nodes = split_nodes_links([node, node2])

        self.assertListEqual(
            [
                TextNode("Hi ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "https://burgerking.com"),
                TextNode(" whopper", TextType.TEXT),
                TextNode("hi ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "https://mcdonalds.com"),
                TextNode(" bigmac", TextType.TEXT),

            ],
            new_nodes
        )



    def test_split_links(self):
        node = TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
                [
                    TextNode("This is text with a link ", TextType.TEXT),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()

