import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):

    def setUp(self):
        self.node1 = LeafNode("p", "Hello, World!")
        self.node2 = LeafNode("a", "Link", None, {"href": "https://example.com"})
        self.node3 = LeafNode("div", "Goodbye, World!", [self.node1, self.node2], {"class": "container"})
        self.empty_node = HTMLNode()

    def test_initialization(self):
        """Tests if the object initialised correctly"""
        self.assertEqual(self.node1.tag, "p")
        self.assertEqual(self.node1.value, "Hello, World!")
        self.assertIsNone(self.node1.children)
        self.assertIsNone(self.node1.props)

        self.assertEqual(self.node2.props, {"href": "https://example.com"})
        

    def test_not_eq(self):
        """Tests if the __eq__ method is working as intended, with non-equal objects"""
        self.assertNotEqual(self.node2, self.node3)
    
    def test_empty_value(self):
        """Tests if the exception is called correctly"""
        with self.assertRaises(ValueError):
                    self.node3 = LeafNode("p", None, [self.node1], {"class": "container"})

    


if __name__ == "__main__":
    unittest.main()