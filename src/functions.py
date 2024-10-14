from htmlnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits text according to delimiter.
    
    Takes a list of TextNodes and splits the text into parts,
    depending on what delimiter was specified. The text between
    the delimiters will be of the specified text_type, and the
    text outside will be of text_type "text".
    
    Args:
        old_nodes (list): a list of TextNode objects to be processed.
        delimiter (string): what delimiter to split the text to.
        text_type (string): what text_type the parts between delimiters should be.
    
    Returns:
        list: a list of new TextNode objects.
    """
    delimited_nodes = []
    for node in old_nodes:
        if node.text_type == "text":
            if node.text:
                new_text = node.text.split(delimiter)
                for index, part in enumerate(new_text):
                    if part:
                        if index % 2 == 0:
                            delimited_nodes.append(TextNode(part, "text"))
                        else:
                            delimited_nodes.append(TextNode(part, text_type))
            else:
                delimited_nodes.append(node)
        else:
            delimited_nodes.append(node)
    return delimited_nodes

def extract_markdown_images(text):
    """
    Matches a pattern ![some text](image)
    returns list of tuples containing (some text, image)
    """
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    """
    Matches a pattern [some text](link)
    returns list of tuples containing (some text, link)
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    """
    Splits lists of nodes [node1, node2, ...] into new nodes.

    Takes a list of TextNode objects, splits them according to a 
    pattern ![alt text](image), and returns a list of new TextNode 
    objects. TextNodes will be TextNode("content", text_type="text")
    if outside matched segments, and the matched patterns will become
    TextNode("alt text", text_type="image", "image").
    """
    new_nodes = []
    
    # Pattern to match markdown images
    pattern = r"(!\[[^\[\]]*\]\([^\(\)]*\))"
    
    for old_node in old_nodes:
        split_parts = re.split(pattern, old_node.text)
        
        part_index = 0
        for part in split_parts:
            if part:
                if not re.search(pattern, part):
                    new_nodes.append(TextNode(part, old_node.text_type, old_node.url))
                else:
                    extracted_image = extract_markdown_images(part)
                    new_nodes.append(TextNode(extracted_image[0][0], "image", extracted_image[0][1]))
            
    
    return new_nodes

def split_nodes_link(old_nodes):
    """
    Splits lists of nodes [node1, node2, ...] into new nodes.

    Takes a list of TextNode objects, splits them according to a 
    pattern [some text](link), and returns a list of new TextNode 
    objects. TextNodes will be TextNode("content", text_type="text")
    if outside matched segments, and the matched patterns will become
    TextNode("some text", text_type="link", "link").
    """
    new_nodes = []
    
    # Pattern to match [some text](link)
    pattern = r"(\[[^\[\]]*\]\([^\(\)]*\))"
    
    for old_node in old_nodes:
        split_parts = re.split(pattern, old_node.text)
        
        for part in split_parts:
            if part:
                if not re.search(pattern, part):
                    new_nodes.append(TextNode(part, old_node.text_type, old_node.url))
                else:
                    extracted_image = extract_markdown_links(part)
                    new_nodes.append(TextNode(extracted_image[0][0], "link", extracted_image[0][1]))
    
    return new_nodes

def text_to_textnodes(text):
    """
    Takes a string and converts it to a list of TextNodes using the above functions.
    
    Args:
        text (string): the string to be converted.
    
    Returns:
        list: a list of new TextNode objects.
    """
    new_nodes = [TextNode(text, "text")]
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", "bold")
    new_nodes = split_nodes_delimiter(new_nodes, "*", "italic")
    new_nodes = split_nodes_delimiter(new_nodes, "`", "code")
    
    return new_nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks]

def block_to_block_type(block):
    """
    Function that tells you what type of block it is.

    Takes a block of markdown text and returns a string representing
    the type of block (heading, code, quote, unordered list, ordered
    list or paragraph).
    """
    # testing if heading
    if block.startswith("#"):
        number_of_hashes = 0
        for ch in block:
            if ch == "#":
                number_of_hashes += 1
            else:
                break
        if 1 <= number_of_hashes <= 6:
            return "heading"
    
    # testing if code
    if block.startswith("```") and block.endswith("```"):
        return "code"
    
    # testing if quote
    is_quote = True
    test_for_quote = block.split("\n")
    for line in test_for_quote:
        if line[0] != ">":
            is_quote = False
            break
    if is_quote:
        return "quote"
    
    # testing if unordered list
    is_unordered_list = True
    test_for_unordered_list = block.split("\n")
    for line in test_for_quote:
        if line[0] not in "*-":
            is_unordered_list = False
    if is_unordered_list:
        return "unordered_list"
    
    # testing if ordered_list
    is_ordered_list = True
    test_for_ordered_list = block.split("\n")
    for line in test_for_ordered_list:
        if line[0] not in "1234567890" and line[1:3] != ". ":
            is_ordered_list = False
    if is_ordered_list:
        return "ordered_list"

    # if none of the above, it is a paragraph
    return "paragraph"