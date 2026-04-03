from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str):
    lines = block.split("\n")
    heading = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(heading):
        return BlockType.HEADING
    elif len(lines) > 1 and lines[0] == "```" and lines[-1] == "```":
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
