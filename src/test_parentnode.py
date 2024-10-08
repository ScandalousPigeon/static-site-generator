import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestHTMLNodes(unittest.TestCase):
    def setUp(self):
        """Sets up node objects for testing"""
        self.leaf_node1 = LeafNode("b", "Bold text")
        self.leaf_node2 = LeafNode(None, "Normal text")
        self.leaf_node3 = LeafNode("i", "italic text")
        self.leaf_node4 = LeafNode(None, "Normal text")
        
        self.parent_node = ParentNode(
            "p",
            [
                self.leaf_node1,
                self.leaf_node2,
                self.leaf_node3,
                self.leaf_node4,
            ],
        )

    def test_to_html_no_tag(self):
        
        with self.assertRaises(ValueError):
            invalid_node = ParentNode(
            None,
            [
                self.leaf_node1,
                self.leaf_node2,
            ],
            )
            invalid_node.to_html()

    def test_to_html_no_children(self):
        
        with self.assertRaises(ValueError) as context:
            invalid_node = ParentNode("p", [])
            invalid_node.to_html()
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    

if __name__ == "__main__":
    unittest.main()