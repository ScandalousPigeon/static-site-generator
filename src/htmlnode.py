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