import textnode
from leafnode import LeafNode
from textnode import TextType


def text_node_to_html_node(text_node):
    text = text_node.text
    text_type = text_node.text_type
    url = text_node.url

    if text_type == TextType.TEXT:
        return LeafNode(None, text)

    elif text_type == TextType.BOLD:
        return LeafNode("b", text)

    elif text_type == TextType.ITALIC:
        return LeafNode("i", text)

    elif text_type == TextType.CODE:
        return LeafNode("code", text)

    elif text_type == TextType.LINK:
        return LeafNode("a", text, props={"href": url})

    elif text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": url, "alt": text})

    else:
        raise Exception("text_node is not of TextType")
