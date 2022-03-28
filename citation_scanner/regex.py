import re


def get_match_obj(pattern, doc, window=(100, 50)):

    iter_obj = re.finditer(pattern, doc)

    matches = []

    for i in iter_obj:
        print(f"match: '{i.group(0)}' position: {i.start()}-{i.end()} ")
        match_txt = get_window(doc, i.start(), i.end(), window=window)
        print(match_txt)
        matches.extend([i, match_txt])

    return matches


def get_window(doc, pos_start, pos_end, window=(100,50)):

    w_start = max(0, pos_start - window[0])

    w_end = min(len(doc), pos_end + window[1])

    return doc[w_start:w_end]
