from typing import Text
from textnode import TextType, TextNode
from extract_markdown_images_and_links import (
    extract_markdown_images,
    extract_markdown_links,
)


def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        images_list = extract_markdown_images(old_node.text)
        if not images_list:
            result.append(old_node)
            continue
        remaining_text = old_node.text
        for alt, url in images_list:
            sections = remaining_text.split(f"![{alt}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(alt, TextType.IMAGE, url))
            remaining_text = sections[1]
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    return result


def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        link_list = extract_markdown_links(old_node.text)
        if not link_list:
            result.append(old_node)
            continue
        remaining_text = old_node.text
        for word, url in link_list:
            sections = remaining_text.split(f"[{word}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, url section not closed")
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(word, TextType.LINK, url))
            remaining_text = sections[1]
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    return result
