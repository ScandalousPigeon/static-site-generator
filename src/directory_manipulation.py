import os
import shutil

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

