from htmlnode import TextNode, LeafNode

import unittest

class TestHTMLNodes(unittest.TestCase):
    """
    Unit tests for the node_to_html_node function.
    """
    def setUp(self):
        """Sets up node objects for testing"""
        text_type_text = TextNode(text="What, you egg?", text_type="text")
        text_type_bold = TextNode(text="Stop right there criminal scum!", text_type="bold")
        text_type_italic = TextNode(text='"The vastness of the internet devours us." - Gerd von Rundstedt, 1942', text_type="italics")
        text_type_code = TextNode(text="enigma cipher", text_type="code")
        text_type_link = TextNode(text="Click here if you hate grass", text_type="link", url="https://www.bluedit.com")
        test_type_image = TextNode(text="An image of an egg.", text_type="image", url="https://www.egg.com")
    
    def test_invalid(self):
        with self.assertRaises(Exception):
            invalid_node = TextNode(text="lmao", text_type="goofy-ah type")

if __name__ == "__main__":
    unittest.main()