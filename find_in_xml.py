import getopt
import sys
import os
import re
from os import listdir
from os.path import isfile, isdir, join
import xml.etree.ElementTree as ET


class Single:
    def __init__(self, file, count):
        self.file = file
        self.count = count


class Return:
    def __init__(self, condition, count):
        self.condition = condition
        self.count = count


def find_parse(root, word_inside, count):
    for child in root:
        attrib = child.attrib
        find = False
        for a in list(attrib):
            if re.search(word_inside, attrib[a]):
                count += 1
                if child.tag == 'BoundLabelBinding':
                    ret = Return(True, count)
                    return ret
                else:
                    find = True

        if find:
            root.remove(child)
        else:
            pippo = find_parse(child, word_inside, count)
            if pippo.condition:
                root.remove(child)
            count = pippo.count

    ret = Return(False, count)
    return ret


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
            single = Single(f, 0)
            tree = ET.parse(f)
            root = tree.getroot()
            single.count = find_parse(root, find_word, 0).count
            tree.write(f)
            result.append(single)

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

    loop = True
    while loop:
        loop = False
        array_result = parse(path, recur, word)
        for x in array_result:
            if x.count > 0:
                loop = True
            print("File: ", x.file, " count: ", x.count)
            print("\n")
