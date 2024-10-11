from htmlnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
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

def extract_markdown_images(text):
    """
    Matches a pattern ![some text](image)
    Returns a list of tuples containing (some text, image)
    """
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []
    
    # Pattern to match markdown images
    pattern = r"(!\[[^\[\]]*\]\([^\(\)]*\))"
    
    for old_node in old_nodes:
        split_parts = re.split(pattern, old_node.text)
        matches = re.findall(pattern, old_node.text)
        
        # Iterate through the parts (split text) and images (matches)
        part_index = 0
        for part in split_parts:
            if part:
                if not re.search(pattern, part):
                    new_nodes.append(TextNode(part, "text"))
            
            # Add corresponding image node if there are matches left
            if part_index < len(matches):
                image_data = extract_markdown_images(matches[part_index])
                if image_data:
                    image_alt, image_link = image_data[0]
                    new_nodes.append(TextNode(image_alt, "image", image_link))
                part_index += 1
    
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    pass

def text_to_textnodes(text):
    pass