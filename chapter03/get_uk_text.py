import json
import gzip

def get_uk_text():
    with gzip.open("jawiki-country.json.gz") as f:
        for line in f:
            article_dict = json.loads(line)
            if "イギリス" in article_dict["title"]:
                return article_dict["text"]

