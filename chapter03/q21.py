import get_uk_text as get

f = get.get_uk_text().split('\n')

for line in f:
    if "Category" in line:
        print(line)

#内包表記を使うと以下のように書ける
print([line for line in f if "Category" in line])