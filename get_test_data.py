import requests
import os.path

with open("test_data.txt") as file:
    urls = file.read().splitlines()

for url in urls:
    r = requests.get(url)
    name = os.path.basename(url)
    print(name)
    open(os.path.join("pdfs", name), "wb").write(r.content)
