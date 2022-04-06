# Tika Test
Having a go at setting up and using apache tika with python.

# Java
On ubuntu, so:
```commandline
sudo apt install default-jre
```

# Tika
Could download from apache: https://dlcdn.apache.org/tika/1.28.1/tika-app-1.28.1.jar but the `tika` pypi package looks to do this for you.

so - in a new virtualenv:


```commandline
python3 -m virtualenv env
source env/bin/activate
pip install tika
pip install jupyter notebook
pip install spacy-annotator
jupyter notebook
```

# Running
Then run `get_test_data.py` to fetch all the urls in `test_data.txt` and run `parse.py` to pass each one through tika and extract content & metadata.

# Next Steps

Try tagging some data with https://github.com/ieriii/spacy-annotator ? 