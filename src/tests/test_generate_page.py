from unittest.mock import patch, mock_open
import unittest
from generate_page import extract_title, generate_page


class GeneratePageTitle(unittest.TestCase):
    # Exraction Of Heading Tests
    def test_single_line_heading(self):
        md = "# Hello World"
        self.assertEqual(extract_title(md), "Hello World")

    def test_heading_with_extra_spaces(self):
        md = "#    Hello World   "
        self.assertEqual(extract_title(md), "Hello World")

    def test_heading_not_first_line(self):
        md = "Some intro text\n# Title Here\nMore text"
        self.assertEqual(extract_title(md), "Title Here")

    def test_multiple_headings_returns_first(self):
        md = "# First Title\n# Second Title"
        self.assertEqual(extract_title(md), "First Title")

    def test_ignores_non_h1_headings(self):
        md = "## Not this one\n### Nor this\n# Actual Title"
        self.assertEqual(extract_title(md), "Actual Title")

    def test_no_heading_raises_exception(self):
        md = "Just some text\nAnother line"
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "It doesn't have a heading")

    def test_empty_string_raises_exception(self):
        with self.assertRaises(Exception):
            extract_title("")

    def test_heading_with_only_hash_and_space(self):
        md = "# \n# Valid Title"
        self.assertEqual(extract_title(md), "")


if __name__ == "__main__":
    unittest.main()
