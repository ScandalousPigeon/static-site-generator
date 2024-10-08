import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):

    def setUp(self):
        self.node1 = HTMLNode("p", "Hello, World!")
        self.node2 = HTMLNode("a", "Link", None, {"href": "https://example.com"})
        self.node3 = HTMLNode("div", None, [self.node1, self.node2], {"class": "container"})
        self.empty_node = HTMLNode()

    def test_initialization(self):
        """Tests if the object initialised correctly"""
        self.assertEqual(self.node1.tag, "p")
        self.assertEqual(self.node1.value, "Hello, World!")
        self.assertIsNone(self.node1.children)
        self.assertIsNone(self.node1.props)

        self.assertEqual(self.node2.props, {"href": "https://example.com"})
        self.assertIsInstance(self.node3.children, list)
        self.assertEqual(self.node3.props, {"class": "container"})

    def test_not_eq(self):
        """Tests if the __eq__ method is working as intended, with non-equal objects"""
        self.assertNotEqual(self.node2, self.node3)
    
    def test_repr(self):
        """Tests if the __repr__ method is working as intended"""
        expected_repr_node1 = "HTMLNode('p', 'Hello, World!', None, None)"
        expected_repr_node2 = "HTMLNode('a', 'Link', None, {'href': 'https://example.com'})"
        expected_repr_node3 = "HTMLNode('div', 'None', [HTMLNode('p', 'Hello, World!', None, None), HTMLNode('a', 'Link', None, {'href': 'https://example.com'})], {'class': 'container'})"
        self.assertEqual(repr(self.node1), expected_repr_node1)
        self.assertEqual(repr(self.node2), expected_repr_node2)
        self.assertEqual(repr(self.node3), expected_repr_node3)


if __name__ == "__main__":
    unittest.main()