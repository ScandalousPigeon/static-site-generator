from textnode import TextNode

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initialise a HTMLNode instance.

        Args:
            tag (string): string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
            value (string): string representing the value of the HTML tag
            children (list): list of HTMLNode objects representing the children of this node
            props (dictionary): dictionary of key-value pairs representing the attributes of the HTML tag
        All args are optional and defaults to None
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        """
        String representation of the current HTMLNode instance
        """
        return f"HTMLNode('{self.tag}', '{self.value}', {self.children}, {self.props})"

    def __eq__(self, other):
        if self.tag == other.tag:
            if self.value == other.value:
                if self.children == other.children:
                    if self.props == other.props:
                        return True
        return False

    def to_html(self):
        """
        To be overridden by child classes; they will render themselves as html
        """
        raise NotImplementedError
    
    def props_to_html(self):
        """
        Returns a string that represents the HTML attributes of the node
        """
        if self.props:
            new_dict = [f'{entry}="{props[entry]}"' for entry in props]
            return " " + " ".join(new)
        return ""

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        """Initialise a LeafNode object, inherits from HTMLNode"""
        if value == "":
            raise ValueError("LeafNode must have a non-empty value")
        super().__init__(tag, value, None, props)

    def __eq__(self, other):
        if self.tag == other.tag:
            if self.value == other.value:
                if self.props == other.props:
                    return True
        return False
        
    def to_html(self):
        if self.value == "":
            raise ValueError
        if self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return self.value

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

def text_node_to_html_node(text_node: TextNode):
    """
    Function to convert a TextNode into a LeafNode.
    
    Args:
        text_node (TextNode): a TextNode object

    Returns:
        a LeafNode object
    """
    if text_node.text_type == "text":
        return LeafNode(tag=None, value=text_node.text)
    if text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    if text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == "link":
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    if text_node.text_type == "image":
        return LeafNode(tag="img", value=None, props={"src": text_node.url, "alt": text_node.text})

    raise Exception("TextNode has an invalid type")