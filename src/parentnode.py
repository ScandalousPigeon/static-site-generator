from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children is None or children == []:
            raise ValueError("ParentNode must have non-empty children")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        
        copy = self.children.copy()
        collected = ""
        
        for child in copy:
            collected += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{collected}</{self.tag}>"


            
        
        