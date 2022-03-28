from citation_scanner import download, tika, regex

file_list = download.get_file_list()
download.download_file_list(file_list, loc="pdfs")

tika.parse_dir("pdfs")
docs = tika.read_parsed_dir("pdfs", strip_lines=True)

pattern_list = [r"\[\d{4}\]"]

match_list = regex.get_match_obj(
    pattern=pattern_list[0],
    doc=docs[0],
    window=(100, 25)
)