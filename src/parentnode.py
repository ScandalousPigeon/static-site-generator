from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children is None or children == []:
            raise ValueError("ParentNode must have non-empty children")
        super().__init__(tag, children, props)
    
    def to_html(self, collected=""):
        if not self.tag:
            raise ValueError("node has no tag")
        if not self.children:
            raise ValueError("node has no children")
        
        copy = self.children.copy()
        
        for child in copy:
            if isinstance(child, LeafNode):
                collected += child.to_html()
            else:
                collected += child.to_html(collected)

        return f"<{self.tag}>" + collected + f"</{self.tag}>"


            
        
        