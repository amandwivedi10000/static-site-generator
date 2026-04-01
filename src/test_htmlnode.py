import unittest

from htmlnode import HTMLNode


class TestNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a text node")
        node2 = HTMLNode()
        print(node2.props_to_html())
        node3 = HTMLNode("This is a HTML node")
        print(node3.props_to_html())
        node4 = HTMLNode("This is a text node", "I don't know the value")
        print(node4.props_to_html())


if __name__ == "__main__":
    unittest.main()
