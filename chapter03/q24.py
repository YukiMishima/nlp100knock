import get_uk_text as get
import re

f = get.get_uk_text().split('\n')
mediafile_list = [line for line in f if "File" or u"ファイル" in line]
r = re.compile(r"\[\[(ファイル|File):(.*?)\|")

for line in mediafile_list:
    match = r.search(line)
    if match:
        print(match.group(2))