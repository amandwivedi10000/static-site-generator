from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            result.append(old_node)
            continue
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid Markdown: delimiter not closed")
        for index, part in enumerate(parts):
            if part == "":
                continue
            if index % 2 == 0:
                result.append(TextNode(part, TextType.TEXT))
            else:
                result.append(TextNode(part, text_type))
    return result
