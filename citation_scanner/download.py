import requests
import os.path


def get_file_list(input_file="test_data.txt"):
    """
    Read a file to a list with an item per line
    :param input_file:
    :return: List, one item per line
    """

    with open(input_file) as file:
        urls = file.read().splitlines()
    return urls


def download_file_list(urls, loc="pdfs"):
    """
    Download
    :param urls: list of urls to download
    :param loc: where to download files to
    :return:
    """
    for url in urls:
        r = requests.get(url)
        name = os.path.basename(url)
        print(name)
        open(os.path.join(loc, name), "wb").write(r.content)
