from htmlnode import TextNode
from directory_manipulation import *

def main():
    dummy = TextNode("The Infinite Pigeon Theorem", "bold", "https://xmxx.com")
    print(dummy)

    destination_path = "/home/suspiciouspigeon/workspace/github.com/ScandalousPigeon/static-site-generator/static"
    source_path = "/home/suspiciouspigeon/workspace/github.com/ScandalousPigeon/static-site-generator/public"
    copy_and_move_contents(source_path, destination_path)

if __name__ == "__main__":
    main()


