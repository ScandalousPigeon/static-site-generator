from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        """Initialise a LeafNode object, inherits from HTMLNode"""
        if value is None or value == "":
            raise ValueError("LeafNode must have a non-empty value")
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if not self.value:
            raise ValueError
        if self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return self.value