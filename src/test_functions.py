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

class TestTextToTextNodes(unittest.TestCase):
    def test_given_example(self):
        input = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
        ]
        result = text_to_textnodes(input)
        self.assertEqual(expected, result)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_given_example(self):
        input = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertEqual(markdown_to_blocks(input), expected)
        
class TestBlockToBlockType(unittest.TestCase):
    import unittest

class TestBlockToBlockType(unittest.TestCase):
    
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading level 1"), "heading")
        self.assertEqual(block_to_block_type("###### Heading level 6"), "heading")
        self.assertNotEqual(block_to_block_type("####### Invalid heading"), "heading")
    
    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), "code")
        self.assertNotEqual(block_to_block_type("```\ncode block"), "code")
    
    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote\n> Spanning multiple lines"), "quote")
        self.assertNotEqual(block_to_block_type("This is not a quote"), "quote")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), "unordered_list")
        self.assertNotEqual(block_to_block_type("+ Item 1\n+ Item 2"), "unordered_list")  # Not supported as per current function logic

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. Item 1\n2. Item 2"), "ordered_list")
        self.assertEqual(block_to_block_type("9. Item 1\n10. Item 2"), "ordered_list")
        self.assertNotEqual(block_to_block_type("No ordered list here"), "ordered_list")

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph with some text."), "paragraph")
        self.assertEqual(block_to_block_type("Another paragraph, spanning multiple lines.\nStill part of the same paragraph."), "paragraph")
        self.assertNotEqual(block_to_block_type("> Not a paragraph"), "paragraph")

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_empty_input(self):
        with self.assertRaises(Exception) as context:
            markdown_to_html_node("")
        self.assertEqual(str(context.exception), "input cannot be empty")

    def test_heading(self):
        markdown = "### Heading Text"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="h3", children=parse_raw_text("Heading Text"))
        ])
        self.assertEqual(result, expected)

    def test_code_block(self):
        markdown = "```\ncode example\n```"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="pre", children=[
                HTMLNode(tag="code", value="code example")
            ])
        ])
        self.assertEqual(result, expected)

    def test_blockquote(self):
        markdown = "> Quote text\n> More quote text"
        result = markdown_to_html_node(markdown)
        stripped_block = "Quote text\nMore quote text"
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="blockquote", children=parse_raw_text(stripped_block))
        ])
        self.assertEqual(result, expected)

    def test_unordered_list(self):
        markdown = "- Item 1\n- Item 2"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="ul", children=[
                HTMLNode(tag="li", children=parse_raw_text("Item 1")),
                HTMLNode(tag="li", children=parse_raw_text("Item 2"))
            ])
        ])
        self.assertEqual(result, expected)

    def test_ordered_list(self):
        markdown = "1. Item 1\n2. Item 2"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="ol", children=[
                HTMLNode(tag="li", children=parse_raw_text("Item 1")),
                HTMLNode(tag="li", children=parse_raw_text("Item 2"))
            ])
        ])
        self.assertEqual(result, expected)

    def test_paragraph(self):
        markdown = "This is a paragraph."
        result = markdown_to_html_node(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="p", children=parse_raw_text("This is a paragraph."))
        ])
        self.assertEqual(result, expected)

    def test_mixed_blocks(self):
        markdown = "### Heading\n\nThis is a paragraph.\n\n- Item 1\n- Item 2\n\n1. Ordered item 1\n2. Ordered item 2"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="h3", children=parse_raw_text("Heading")),
            HTMLNode(tag="p", children=parse_raw_text("This is a paragraph.")),
            HTMLNode(tag="ul", children=[
                HTMLNode(tag="li", children=parse_raw_text("Item 1")),
                HTMLNode(tag="li", children=parse_raw_text("Item 2"))
            ]),
            HTMLNode(tag="ol", children=[
                HTMLNode(tag="li", children=parse_raw_text("Ordered item 1")),
                HTMLNode(tag="li", children=parse_raw_text("Ordered item 2"))
            ])
        ])
        self.assertEqual(result, expected)

    def test_heading_and_code(self):
        markdown = "# Heading\n\n```\ncode example\n```"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="h1", children=parse_raw_text("Heading")),
            HTMLNode(tag="pre", children=[
                HTMLNode(tag="code", value="code example")
            ])
        ])
        self.assertEqual(result, expected)

    def test_quote_and_list(self):
        markdown = "> Quote text\n\n- List item 1\n- List item 2"
        result = markdown_to_html_node(markdown)
        stripped_block = "Quote text"
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="blockquote", children=parse_raw_text(stripped_block)),
            HTMLNode(tag="ul", children=[
                HTMLNode(tag="li", children=parse_raw_text("List item 1")),
                HTMLNode(tag="li", children=parse_raw_text("List item 2"))
            ])
        ])
        self.assertEqual(result, expected)

    def test_multiple_headings(self):
        markdown = "# Heading 1\n## Heading 2\n### Heading 3"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="h1", children=parse_raw_text("Heading 1")),
            HTMLNode(tag="h2", children=parse_raw_text("Heading 2")),
            HTMLNode(tag="h3", children=parse_raw_text("Heading 3"))
        ])
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()