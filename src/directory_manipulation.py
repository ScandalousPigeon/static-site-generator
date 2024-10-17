import os
import shutil
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
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'.")

    # Read markdown content
    try:
        with open(from_path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file '{from_path}' does not exist")
    except Exception as e:
        raise Exception(f"Error reading source file '{from_path}': {e}")

    # Read template content
    try:
        with open(template_path, "r") as file:
            template_content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Template file '{template_path}' does not exist")
    except Exception as e:
        raise Exception(f"Error reading template file '{template_path}': {e}")

    # Extract title and remove it from content
    title = extract_title(content)

    # Convert markdown to HTML
    content_html = markdown_to_html_node(content).to_html()

    # Replace placeholders in template
    new_content = template_content.replace("{{ Title }}", title)
    new_content = new_content.replace("{{ Content }}", content_html)

    # Write to destination
    try:
        with open(dest_path, "w") as file:
            file.write(new_content)
            print(f"Page written to '{dest_path}'")
    except Exception as e:
        raise Exception(f"Error writing to destination file '{dest_path}': {e}")
