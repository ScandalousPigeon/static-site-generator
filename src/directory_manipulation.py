import os
import shutil
from functions import *

def delete_directory_contents(directory):

    if not os.path.exists(directory):
        raise FileNotFoundError("directory does not exist")

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

def copy_and_move_contents(source, destination):

    delete_directory_contents(destination)

    if not os.path.exists(source) or not os.path.exists(destination):
        raise FileNotFoundError("directory does not exist")

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path) as file:
        content = file.read()
    
    with open(template_path) as file:
        template_content = file.read()
    title = extract_title(content)
    # assuming that h1 is always first in the document
    removed_title = "".join(content)
    content = markdown_to_html_node(content)
    content = content.to_html()
    new_content = template_content.replace("{{ Title }}", title)
    new_content = template_content.replace("{{ Content }}", content)

    with open(dest_path, "w") as file:
        file.write(new_content)