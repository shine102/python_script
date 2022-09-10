import re
import os
import sys

def main():
    #get the flag name
    flag = sys.argv[1]
    # Get the path to the current directory
    path = os.getcwd()
    # Get the list of files in the current directory
    files = os.listdir(path)
    files = files[1:]
    # Loop through the files
    for file in files:
        f = open(file, 'r')
        # Read the contents of the file
        contents = f.read()
        if (re.search(flag, contents)):
            print(file)
        f.close()

if __name__ == '__main__':
    main()
