from htmlnode import TextNode
from directory_manipulation import *

def main():

    destination_path = "/home/suspiciouspigeon/workspace/github.com/ScandalousPigeon/static-site-generator/static"
    source_path = "/home/suspiciouspigeon/workspace/github.com/ScandalousPigeon/static-site-generator/public"
    #copy_and_move_contents(source_path, destination_path)

    template_path = "/home/suspiciouspigeon/workspace/github.com/ScandalousPigeon/static-site-generator/template.html"
    from_path = "/home/suspiciouspigeon/workspace/github.com/ScandalousPigeon/static-site-generator/content"
    from_path_majesty = "/home/suspiciouspigeon/workspace/github.com/ScandalousPigeon/static-site-generator/content/majesty/index.md"
    dest_path = "/home/suspiciouspigeon/workspace/github.com/ScandalousPigeon/static-site-generator/public"


    #generate_pages_recursive(from_path, template_path, dest_path)


if __name__ == "__main__":
    main()


