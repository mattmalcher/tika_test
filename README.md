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
make setup_env
make setup_deps
source env/bin/activate
```

Then

```commandline
jupyter notebook
```

or

```commandline
make train
```

# Running
Then run `get_test_data.py` to fetch all the urls in `test_data.txt` and run `parse.py` to pass each one through tika and extract content & metadata.


# National Archives

[As of April 2022 the National Archives is hosting case law data](https://www.gov.uk/government/news/court-judgments-made-accessible-to-all-at-the-national-archives). They have an alpha service up and running with some notes on [what to expect](https://caselaw.nationalarchives.gov.uk/what-to-expect)

This seems to be a promising source of case law data that is set to expand and will have more permissive licence to use the data (subject to a successful application).

## Manual Document 'Spider' Test
Started at: https://caselaw.nationalarchives.gov.uk/uksc/2022/9

Downloaded the xml at https://caselaw.nationalarchives.gov.uk/uksc/2022/9/data.xml

This has a Neutral Citation tag near the top of the XML. (XML is in Oasis [LegalDocumentML](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=legaldocml) format)

In para 19, for example there is a reference to: [2020] EWCA Civ 663. This is not tagged in the XML as a citation so you would need to use something like the NER in this repo to find it.

If you enter that in the search you get 
https://caselaw.nationalarchives.gov.uk/ewca/civ/2020/663

This looks like a URL in the format:
https://caselaw.nationalarchives.gov.uk/id/{court}[/{sub-division}/]{year}/{neutral-citation-number}


So in principle, you could start from a particular document and traverse a network of citations. You could then visualise this graph starting from an individual document, or better, visualise it for an entire domain and use some graph metric (page rank?) to identify the key citations in a given area.

## Automatic Spidering Prerequisites:

* Need a working Citation recogniser (looks doable based on preliminary tests in this repo)
* Need a way to turn a citation into a NA url (looks possible given manual test above)
* Need the cited document to be on the NA site (wont be in all cases, but looks set to expand)
* Need *permission to use the data/API in this way* (looks like you could apply for it and that a tool like this might get approval)

# Project Next Steps

* NER
    - Tag more data?
    - Split into test/train?
    - Try different tagging schemes?
    - Get spacy training on GPU going

* Look at data collection opportunities?
    - Apply to National Archives for a licence to use the data
    - Figure out how to use National Archive XMLs with spacy for training the model

* Try out networks / visualisations?