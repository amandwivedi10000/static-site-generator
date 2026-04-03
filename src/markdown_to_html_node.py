from textnode import TextNode, TextType
from parentnode import ParentNode
from textnode_to_htmlnode import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from htmlnode import HTMLNode
from block_to_block_type import block_to_block_type, BlockType
from markdown_to_blocks import markdown_to_blocks


def markdown_to_html_node(markdown):
    markdown_blocks: list[str] = markdown_to_blocks(markdown)
    return block_to_html_node(markdown_blocks)


def block_to_html_node(markdown_blocks: list[str]):
    children = []
    for markdown_block in markdown_blocks:
        block_type = block_to_block_type(markdown_block)
        if block_type == BlockType.PARAGRAPH:
            new_html_node = paragraph_to_html_node(markdown_block)
            children.append(new_html_node)
        elif block_type == BlockType.HEADING:
            new_html_node = heading_to_htmlnode(markdown_block)
            children.append(new_html_node)
        elif block_type == BlockType.CODE:
            new_html_node = code_to_htmlnode(markdown_block)
            children.append(new_html_node)
        elif block_type == BlockType.QUOTE:
            new_html_node = quote_to_htmlnode(markdown_block)
            children.append(new_html_node)
        elif block_type == BlockType.UNORDERED_LIST:
            new_html_node = unordered_list_to_htmlnode(markdown_block)
            children.append(new_html_node)
        elif block_type == BlockType.ORDERED_LIST:
            new_html_node = ordered_list_to_htmlnode(markdown_block)
            children.append(new_html_node)
    return ParentNode("div", children)


def text_to_children(text: str):
    nodes = text_to_textnodes(text)
    result = []
    for node in nodes:
        result.append(text_node_to_html_node(node))
    return result


def paragraph_to_html_node(block: str):
    lines = block.split("\n")
    paragraph = " ".join(line.strip() for line in lines)
    children_list = text_to_children(paragraph)
    return ParentNode("p", children_list)


def heading_to_htmlnode(block: str):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_htmlnode(block: str):
    text = block[4:-3]
    lines = text.split("\n")
    text = "\n".join(line.lstrip() for line in lines)
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def quote_to_htmlnode(block: str):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)


def unordered_list_to_htmlnode(block: str):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        children = text_to_children(line[2:])
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ul", li_nodes)


def ordered_list_to_htmlnode(block: str):
    lines = block.split("\n")
    ol_nodes = []
    for line in lines:
        text = line.split(". ", 1)[1]
        children = text_to_children(text)
        ol_nodes.append(ParentNode("li", children))
    return ParentNode("ol", ol_nodes)
