import json
import gzip

with gzip.open("jawiki-country.json.gz") as f:  #gzipファイルを開いてるだけ
    article_json = f.readline()
    while article_json:
        article_dict = json.loads(article_json)   #1行ずつJSON型の文字列を辞書型に変換
        if article_dict["title"] == u"イギリス":   #'title'キーがイギリスならば
            print(article_dict["text"])           #'text'キーを表示
        article_json = f.readline()

