import getopt
import sys
import os
import re
from os import listdir
from os.path import isfile, isdir, join
import xml.etree.ElementTree as ET


def find_parse(root, word_inside):
    for child in root:
        attrib = child.attrib
        for a in list(attrib):
            if re.search(word_inside, attrib[a]):
                root.remove(child)
                break

            find_parse(child, word_inside)


# Function to parse xml file in folder recursively
def parse(folder, recursive, find_word):
    # """
    # Function to execute the search
    # :param folder: The folder to search in
    # :type folder: string
    # :param recursive: Recursive search
    # :type folder: boolean
    # :return: file name found
    # :rtype: array
    # """
    result = []

    if listdir(folder):
        only_files = [f for f in listdir(folder) if (isfile(join(folder, f)) and f.endswith('.px'))]
        only_folders = [d for d in listdir(folder) if isdir(join(folder, d))]

        if recursive:
            for d in only_folders:
                destination = folder + "/" + d
                result += parse(destination, recursive, find_word)

        for f in only_files:
            tree = ET.parse(f)
            root = tree.getroot()
            find_parse(root, find_word)
            tree.write(f)

    return result


# Main module to read start option parameter
# Option parameter: -d 'C:/Documents/' => The folder to search in)


if "__main__" == __name__:
    # Default params options
    path = os.getcwd()
    recur = False
    word = 'PAM'

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:r:w:", ["directory", "grammar="])
    except getopt.GetoptError as err:
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.exit()
        elif opt in ("-d", "--directory"):
            print('D: ', arg)
            if arg is not None:
                path = arg
        elif opt in ("-w", "--word"):
            print('W: ', arg)
            if arg is not None:
                word = arg
        elif opt in ("-r", "--recursive"):
            print('R: ', arg)
            if arg is not None:
                recur = arg

    array_result = parse(path, recur, word)
    for x in array_result:
        print("File: ", x[0], " in: ", x[1])
        print("\n")