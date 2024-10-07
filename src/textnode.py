class TextNode:
    
    def __init__(self, text: str, text_type: str, url=None):
        """
        Initialise a TextNode instance.

        Args:
            text (string): text content of the node
            text_type (string): type of text this node contains
            url (string, optional): url of the link or image, defaults to None
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Only True if all properties are True.
        Properties are:
            self.text
            self.text_type
            self.url
        """
        if self.text == other.text:
            if self.text_type == other.text_type:
                if self.url == other.url:
                    return True
        return False

    def __repr__(self):
        """
        String representation of the current TextNode instance
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    