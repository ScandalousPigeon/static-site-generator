from htmlnode import *

import unittest

class TestHTMLNodes(unittest.TestCase):
    """
    Unit tests for the node_to_html_node function.
    """
    def setUp(self):
        """Sets up node objects for testing"""
        self.text_type_text = TextNode(text="What, you egg?", text_type="text")
        self.text_type_bold = TextNode(text="Stop right there criminal scum!", text_type="bold")
        self.text_type_italic = TextNode(text='"The vastness of the internet devours us." - Gerd von Rundstedt, 1942', text_type="italic")
        self.text_type_code = TextNode(text="enigma cipher", text_type="code")
        self.text_type_link = TextNode(text="Click here if you hate grass", text_type="link", url="https://www.bluedit.com")
        self.text_type_image = TextNode(text="An image of an egg.", text_type="image", url="https://www.egg.com")
    
    def test_invalid(self):
        """Tests if an Exception is raised correctly if an invalid type is passed"""
        with self.assertRaises(Exception):
            invalid_node = TextNode(text="lmao", text_type="goofy-ah type")
            text_node_to_html_node(invalid_node)

    def test_correct_output(self):
        """Tests each possible type of tag"""
        self.assertEqual(text_node_to_html_node(self.text_type_text), LeafNode(tag=None, value="What, you egg?"))
        self.assertEqual(text_node_to_html_node(self.text_type_bold), LeafNode(tag="b", value="Stop right there criminal scum!"))
        self.assertEqual(text_node_to_html_node(self.text_type_italic), LeafNode(tag="i", value='"The vastness of the internet devours us." - Gerd von Rundstedt, 1942'))
        self.assertEqual(text_node_to_html_node(self.text_type_code), LeafNode(tag="code", value="enigma cipher"))
        self.assertEqual(text_node_to_html_node(self.text_type_link), LeafNode(tag="a", value="Click here if you hate grass", props={"href": "https://www.bluedit.com"}))
        self.assertEqual(text_node_to_html_node(self.text_type_image), LeafNode(tag="img", value=None, props={"src": "https://www.egg.com", "alt": "An image of an egg."}))



if __name__ == "__main__":
    unittest.main()