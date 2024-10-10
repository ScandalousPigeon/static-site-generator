from htmlnode import *

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