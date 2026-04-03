import sys
from generate_page import generate_page, generate_pages_recursive
from copystatic import copy_static_to_public
from textnode import TextNode, TextType


def main():
    copy_static_to_public("static", "docs")
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
