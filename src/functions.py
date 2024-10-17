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
        if node.text_type == "text" and node.text:
            new_text = node.text.split(delimiter)
            for index, part in enumerate(new_text):
                text_node_type = text_type if index % 2 != 0 else "text"
                if part:
                    delimited_nodes.append(TextNode(part, text_node_type))
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
    pattern = r"(!\[[^\[\]]*\]\([^\(\)]*\))"
    
    for old_node in old_nodes:
        split_parts = re.split(pattern, old_node.text)
        
        for part in split_parts:
            if part:
                if re.fullmatch(pattern, part):
                    extracted_image = extract_markdown_images(part)
                    if extracted_image:
                        new_nodes.append(TextNode(extracted_image[0][0], "image", extracted_image[0][1]))
                else:
                    new_nodes.append(TextNode(part, old_node.text_type, old_node.url))
    
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
    pattern = r"(\[[^\[\]]*\]\([^\(\)]*\))"
    
    for old_node in old_nodes:
        split_parts = re.split(pattern, old_node.text)
        
        for part in split_parts:
            if part:
                if re.fullmatch(pattern, part):
                    extracted_link = extract_markdown_links(part)
                    if extracted_link:
                        new_nodes.append(TextNode(extracted_link[0][0], "link", extracted_link[0][1]))
                else:
                    new_nodes.append(TextNode(part, old_node.text_type, old_node.url))
    
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
    # Heading detection
    if block.startswith("#"):
        number_of_hashes = len(block) - len(block.lstrip("#"))
        if 1 <= number_of_hashes <= 6:
            return "heading"

    # Code detection
    if block.startswith("```") and block.endswith("```"):
        return "code"

    # Quote detection
    if all(line.startswith(">") for line in block.split("\n")):
        return "quote"

    # Unordered list detection
    if all(line.lstrip().startswith(("*", "-")) for line in block.split("\n")):
        return "unordered_list"

    # Ordered list detection
    if all(re.match(r"^\d+\.\s", line.lstrip()) for line in block.split("\n")):
        return "ordered_list"

    # Paragraph detection
    return "paragraph"

def parse_raw_text(raw_text):
    return [text_node_to_html_node(node) for node in text_to_textnodes(raw_text)]

def markdown_to_html_node(markdown):
    """
    Function to convert a full markdown document to a single HTMLNode.2
    """

    if not markdown:
        raise Exception("input cannot be empty")

    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case "heading":
                split_block = block.split("\n")
                for line in split_block:
                    number_of_hashes = 0
                    for h in line:
                        if h == "#":
                            number_of_hashes += 1
                        else:
                            break
                    tag = f"h{number_of_hashes}"
                    stripped_line = line.lstrip("#").strip()
                    parsed_raw_text = parse_raw_text(stripped_line)
                    new_child_node = ParentNode(tag=tag, children=parsed_raw_text)
                    children.append(new_child_node)
            case "code":
                tag = "code"
                stripped_block = block.strip().strip("`").strip()
                new_child_node = ParentNode(tag="pre", children=[LeafNode(tag=tag, value=stripped_block)])
                children.append(new_child_node)
            case "quote":
                tag = "blockquote"
                stripped_block = "\n".join([line.lstrip("> ").rstrip() for line in block.split("\n")])
                parsed_raw_text = parse_raw_text(stripped_block)
                new_child_node = ParentNode(tag=tag, children=parsed_raw_text)
                children.append(new_child_node)
            case "unordered_list":
                tag = "ul"
                list_items = block.split("\n")
                parsed_list_items = [ParentNode(tag="li", children=parse_raw_text(item[1:].strip())) for item in list_items]
                new_child_node = ParentNode(tag=tag, children=parsed_list_items)
                children.append(new_child_node)
            case "ordered_list":
                tag = "ol"
                list_items = block.split("\n")
                parsed_list_items = [ParentNode(tag="li", children=parse_raw_text(re.sub(r"^\d+\.\s", "", item).strip())) for item in list_items]
                new_child_node = ParentNode(tag=tag, children=parsed_list_items)
                children.append(new_child_node)
            case "paragraph":
                tag = "p"
                new_child_node = LeafNode(tag=tag, value=block)
                children.append(new_child_node)
            case _:
                raise Exception("invalid block type")

    new_node = ParentNode(tag="div", children=children)
    return new_node

def extract_title(markdown):
    """
    Extract the heading h1 from a given markdown document.
    """
    pattern = r"^#\s+(.*?)$"
    header = re.findall(pattern, markdown, re.MULTILINE)
    if not header:
        return None

    return header[0].strip()