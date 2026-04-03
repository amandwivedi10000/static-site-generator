def markdown_to_blocks(markdown: str):
    blocks = markdown.strip().split("\n\n")
    return [block.strip() for block in blocks if block.strip() != ""]
