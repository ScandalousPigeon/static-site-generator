import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):

    def setUp(self):
        self.node1 = TextNode("This is a text node", "bold")
        self.node2 = TextNode("This is a text node", "bold")
        self.node3 = TextNode("Testing...", "italics", "https://google.com")
        self.node4 = TextNode("Testing...", "italics", "https://google.com")
        self.node5 = TextNode("Hello world", "underline", "https://fakewebsite.org")

    def test_initialization(self):
        """Tests if the object initialised correctly"""
        self.assertEqual(self.node4.text, "Testing...")
        self.assertEqual(self.node4.text_type, "italics")
        self.assertEqual(self.node4.url, "https://google.com")

    def test_eq(self):
        """Tests if the __eq__ method is working as intended, with equal objects"""
        self.assertEqual(self.node1, self.node2)

    def test_not_eq(self):
        """Tests if the __eq__ method is working as intended, with non-equal objects"""
        self.assertNotEqual(self.node2, self.node3)

    def test_eq_with_url(self):
        """Tests __eq__ if url arg is not defaulted to None"""
        self.assertEqual(self.node3, self.node4)
    
    def test_repr(self):
        """Tests if the __repr__ method is working as intended"""
        expected_repr = "TextNode(Hello world, underline, https://fakewebsite.org)"
        result = self.node5.__repr__()
        self.assertEqual(result, expected_repr)
    
    def test_default_url(self):
        """Tests if the url is defaulted correctly on initialization"""
        self.assertIsNone(self.node1.url)


if __name__ == "__main__":
    unittest.main()