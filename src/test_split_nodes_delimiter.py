import unittest
from textnode import TextNode
from delimiter import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode("This is text with a `code block` word", "text")
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text")
        ]
        result = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        node = TextNode("This is a text without delimiters", "text")
        expected = [TextNode("This is a text without delimiters", "text")]
        result = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        node = TextNode("`code1` and `code2` are here", "text")
        expected = [
            TextNode("code1", "code"),
            TextNode(" and ", "text"),
            TextNode("code2", "code"),
            TextNode(" are here", "text")
        ]
        result = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(result, expected)

    def test_empty_text(self):
        node = TextNode("", "text")
        expected = [TextNode("", "text")]
        result = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(result, expected)

    def test_non_text_node(self):
        node = TextNode("Non-text node", "non-text")
        expected = [TextNode("Non-text node", "non-text")]
        result = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()