import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_basic_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)

        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected)

    def test_no_delimiter(self):
        node = TextNode("This is plain text", TextType.TEXT)

        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [node]

        self.assertEqual(new_nodes, expected)

    def test_multiple_code_blocks(self):
        node = TextNode("This `one` and `two` blocks", TextType.TEXT)

        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("one", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("two", TextType.CODE),
            TextNode(" blocks", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("This is `broken text", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_non_text_node(self):
        node = TextNode("code block", TextType.CODE)

        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [node]

        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()
