import os
import shutil
from pathlib import Path
from functions import *

def delete_directory_contents(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist")

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Removed directory: {item_path}")
            else:
                os.remove(item_path)
                print(f"Removed file: {item_path}")
        except Exception as e:
            print(f"Error deleting {item_path}: {e}")

def copy_and_move_contents(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source directory '{source}' does not exist")

    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"Created destination directory: {destination}")

    delete_directory_contents(destination)

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        try:
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path)
                print(f"Copied directory: {src_path} to {dest_path}")
            else:
                shutil.copy2(src_path, dest_path)
                print(f"Copied file: {src_path} to {dest_path}")
        except Exception as e:
            print(f"Error copying {src_path}: {e}")


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)