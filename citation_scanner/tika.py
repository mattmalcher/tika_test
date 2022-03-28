from os import listdir, path
import json
import tika
from tika import parser


def parse_dir(dir_path="pdfs", ext=".pdf"):
    """
    Parse a directory of files using apache tika
    :param dir_path: directory to parse
    :param ext: type of file to parse
    :return: creates .json files with tika metadata & .txt files with tika content.
    """

    tika.initVM()

    to_parse_paths = [path.join(dir_path, x) for x in listdir(dir_path) if x.endswith(ext)]

    for pth in to_parse_paths:
        parsed = parser.from_file(pth)

        with open(pth + ".json", 'w') as f:
            json.dump(parsed["metadata"], f)

        with open(pth + ".txt", 'w') as f:
            f.write(parsed["content"])


def read_parsed(path, strip_lines=True):
    """
    Read a single parsed file back in
    :param path: location of file
    :param strip_lines: condense file onto one line or not?
    :return:
    """

    with open(path, "r") as file:
        data = file.read()
        if strip_lines:
            data = data.replace("\n", "")
    return data


def read_parsed_dir(dir_path="pdfs", ext=".txt", strip_lines=True):
    """
    Read a directory of parsed files
    :param dir_path: location of directory
    :param ext: extension to filter to
    :param strip_lines: if True, condense file onto one line
    :return: list of file content
    """

    to_read = [path.join(dir_path, x) for x in listdir(dir_path) if x.endswith(ext)]

    doc_strings = [read_parsed(f, strip_lines=strip_lines) for f in to_read]

    return doc_strings
