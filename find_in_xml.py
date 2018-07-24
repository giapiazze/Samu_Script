import getopt
import sys
import os
from os import listdir
from os.path import isfile, isdir, join
import xml.etree.ElementTree as ET


# Function to parse xml file in folder recursively
def parse(folder, recursive, word):
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
        only_files = [f for f in listdir(folder) if isfile(join(folder, f))]
        only_folders = [d for d in listdir(folder) if isdir(join(folder, d))]

        if recursive:
            for d in only_folders:
                destination = folder + "/" + d
                result += parse(destination, recursive, word)

        for f in only_files:
            tree = ET.parse(f)
            root = tree.getroot()
            for child in root:
                print(child.tag)       # la proprieta' tag fornisce il nome dell'elemento, incluso l'eventuale namespace
                print(child.text)      # la proprieta' text fornisce il contenuto testuale dell'elemento
                print(child.attrib)    # ovviamente, possiamo ottenere gli attributi di ogni elemento figlio

    return result


# Main module to read start option parameter
# Option parameter: -d 'C:/Documents/' => The folder to search in)


if "__main__" == __name__:
    # Default params options
    path = os.getcwd()
    recur = True
    word = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:r:w", ["directory", "grammar="])
    except getopt.GetoptError as err:
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.exit()
        elif opt in ("-d", "--directory"):
            if arg != 0 or arg is not None:
                path = arg
        elif opt in ("-w", "--word"):
            if arg != 1 or arg == 0:
                word = arg
        elif opt in ("-r", "--recursive"):
            if arg != 2 or arg == 0:
                recur = False

    array_result = parse(path, recur, word)
    for x in array_result:
        print("File: ", x[0], " in: ", x[1])
        print("\n")