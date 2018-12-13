import get_uk_text as get
import re

f = get.get_uk_text().split('\n')
uk_category_list = [line for line in f if "Category" in line]

for line in uk_category_list:
    m = re.search(r'\[\[Category:(.*?)\]\]',line)
    if m is not None:
        print(m.group(1))