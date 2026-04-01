from textnode import TextNode, TextType

def main():
    print("hello world")

    node1 = TextNode("text", TextType.LINK, "https://something.com") 
    node2= TextNode("text", TextType.BOLD)
    print(node1)
    print(node2)
    print()

if __name__ == "__main__":
    main()
