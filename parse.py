from os import listdir, path
import json
import tika
from tika import parser

tika.initVM()

pdf_dir = "pdfs"

pdf_paths = [path.join(pdf_dir, x) for x in listdir(pdf_dir) if x.endswith(".pdf")]

for pth in pdf_paths:
    parsed = parser.from_file(pth)

    with open(pth + ".json", 'w') as f:
        json.dump(parsed["metadata"], f)

    with open(pth + ".txt", 'w') as f:
        f.write(parsed["content"])

