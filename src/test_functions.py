import unittest
from textnode import TextNode
from functions import *

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

class TextExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

class TestSplitNodesImage(unittest.TestCase):
    def test_single_image(self):
        node = TextNode("This is an image ![alt text](https://example.com/image.png) in text", "text")
        expected = [
            TextNode("This is an image ", "text"),
            TextNode("alt text", "image", "https://example.com/image.png"),
            TextNode(" in text", "text")
        ]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_multiple_images(self):
        node = TextNode("Before the first image ![first](https://example.com/first.png) middle text ![second](https://example.com/second.png) end text", "text")
        expected = [
            TextNode("Before the first image ", "text"),
            TextNode("first", "image", "https://example.com/first.png"),
            TextNode(" middle text ", "text"),
            TextNode("second", "image", "https://example.com/second.png"),
            TextNode(" end text", "text")
        ]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_no_images(self):
        node = TextNode("This text has no images.", "text")
        expected = [TextNode("This text has no images.", "text")]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

class TestSplitNodesLink(unittest.TestCase):
    def test_single_link(self):
        node = TextNode("This is a link [link text](https://example.com) in text", "text")
        expected = [
            TextNode("This is a link ", "text"),
            TextNode("link text", "link", "https://example.com"),
            TextNode(" in text", "text")
        ]
        result = split_nodes_link([node])
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        node = TextNode("Before the first link [first](https://realwebsite.com/first.png) middle text [second](https://realersite.com/second.png) end text", "text")
        expected = [
            TextNode("Before the first link ", "text"),
            TextNode("first", "link", "https://realwebsite.com/first.png"),
            TextNode(" middle text ", "text"),
            TextNode("second", "link", "https://realersite.com/second.png"),
            TextNode(" end text", "text")
        ]
        result = split_nodes_link([node])
        self.assertEqual(result, expected)

    def test_no_links(self):
        node = TextNode("This text has no links.", "text")
        expected = [TextNode("This text has no links.", "text")]
        result = split_nodes_link([node])
        self.assertEqual(result, expected)

    def test_link_markdown_at_start(self):
        node = TextNode("[start](https://chess.com/magnumdongsen.png) followed by some text", "text")
        expected = [
            TextNode("start", "link", "https://chess.com/magnumdongsen.png"),
            TextNode(" followed by some text", "text")
        ]
        result = split_nodes_link([node])
        self.assertEqual(expected, result)

    def test_link_markdown_at_end(self):
        node = TextNode("Text before the link [end](https://example.com/end.png)", "text")

    def test_multiple_nodes(self):
        node_one = "lmao"

if __name__ == "__main__":
    unittest.main()