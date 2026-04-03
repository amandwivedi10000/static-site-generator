import unittest
from block_to_block_type import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    # --- HEADING TESTS ---
    def test_heading_single_hash(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_multiple_hashes(self):
        block = "### Heading 3"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_max_hash(self):
        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_invalid_no_space(self):
        block = "#Invalid heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # --- CODE BLOCK TESTS ---
    def test_code_block_simple(self):
        block = "```\ncode here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_multiline(self):
        block = "```\ndef hello():\n    pass\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_not_closed(self):
        block = "```\ncode here"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block_not_opened(self):
        block = "code here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block_single_line(self):
        block = "```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # --- QUOTE TESTS ---
    def test_quote_single_line(self):
        block = "> this is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_multiline(self):
        block = "> line 1\n> line 2\n> line 3"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_mixed_invalid(self):
        block = "> line 1\nnot a quote"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_empty_line(self):
        block = "> line 1\n>\n> line 3"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    # --- UNORDERED LIST TESTS ---
    def test_unordered_list_simple(self):
        block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_single_item(self):
        block = "- item 1"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_invalid_missing_space(self):
        block = "-item 1\n-item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_mixed(self):
        block = "- item 1\nnot a list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # --- ORDERED LIST TESTS ---
    def test_ordered_list_simple(self):
        block = "1. item 1\n2. item 2\n3. item 3"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_single_item(self):
        block = "1. item 1"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_order(self):
        block = "1. item 1\n3. item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_not_starting_at_one(self):
        block = "2. item 1\n3. item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_mixed(self):
        block = "1. item 1\nnot a list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # --- PARAGRAPH TESTS ---
    def test_paragraph_simple(self):
        block = "This is just a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_multiline(self):
        block = "This is line one\nThis is line two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_empty_string(self):
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_random_symbols(self):
        block = "@@@ ### $$$"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
