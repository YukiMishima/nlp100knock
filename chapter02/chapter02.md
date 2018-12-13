# 第２章　UNIXコマンドの基礎

## 10.行数のカウント

>行数をカウントせよ．確認にはwcコマンドを用いよ．

```python
num_lines = sum(1 for line in open('hightemp.txt',encoding='utf-8'))
print(num_lines)
```

`sum()`でこんな書き方ができるとは。  
`for()`使ってるけど縦に長くならなくてうれしい。

```sh
#!/bin/bash

wc hightemp.txt
```

pathの指定と改行コードに気を付けること。  
改行コードの変換は `sed  -i 's/\r\\' <file名>` でできる。

## 11.タブをスペースに置換

>タブ1文字につきスペース一文字に置換せよ。確認にはsedコマンド、trコマンド、もしくはexpandコマンドを用いよ。

```python
f = open('hightemp.txt',encoding='utf-8')
for line in f.readlines():
    print(line.replace('\t',' '))
```

tab1文字は `\t`で表せる。

```sh
#!/bin/bash

sed 's/\t/ /g' hightemp.txt
```

`sed 置換前/置換後/ ファイル名`  
オプションとしていろいろあるので参考にしてください  
[【sed】コマンド(基礎編その4)](http://www.atmarkit.co.jp/ait/articles/1610/17/news015.html)

## 12.1列目をcol1.txtに、２列目をcol2.txtに保存

>各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

```python
f = open('hightemp.txt',encoding='utf-8')
col1 = open('col1.txt','w',encoding='utf-8')
col2 = open('col2.txt','w',encoding='utf-8')

for line in f.readlines():
    word_list = line.split()
    col1.write(word_list[0]+'\n')
    col2.write(word_list[1]+'\n')

col1.close
col2.close
```

ファイルの書き込みにはwを使用。エンコードを指定しないとうまくいかなかった。  
書き込む際に改行コードつけないとだめ。  
with構文を使えば`close`は省略できるらしい。

```sh
#!/bin/bash

cut -f 1 hightemp.txt > col1_comand.txt
cut -f 2 hightemp.txt > col2_comand.txt

```

cutコマンドはテキストファイルの各行から指定した範囲の文字列を取り出して表示させるときに使う。

`cut [オプション][ファイル名]`

今回はフィールド単位で抜き出す範囲を指定した。

[cut【コマンド】とは](http://wa3.i-3-i.info/word12627.html)

## 13. col1.txtとcol2.txtをマージ

>12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ

```python
col1 = open('col1.txt','r',encoding='utf-8')
col2 = open('col2.txt','r',encoding='utf-8')
merge = open('merge.txt','w',encoding='utf-8')

for prefecture,city in zip(col1,col2):
    merge.write(prefecture.rstrip()+'\t'+city.rstrip()+'\n')

col1.close
col2.close
merge.close
```

`rstrip()`を使うと後ろの空白を消してくれる。  
()内に後ろの方の文字を指定すればそこを削除した文字列を返してくれる。

```sh

#!/bin/bash

paste col1.txt col2.txt

```

`paste`コマンドはこんなにもシンプルに書けるなんてすごい。楽勝やんけ。  
タブ区切りでそれぞれの行を結合してくれる。(オプションで`-d`をつけると、結合文字を指定できる。)  
要素を結合しつつも、行列の入れ替えをしたいときは`-s`オプションで。

## 14.先頭からN行を出力

>自然数Nをコマンドライン引数などの手段で受け取り、入力のうち先頭のN行だけを表示せよ。  
確認にはheadコマンドを用いよ。

```python

import sys

f = open('merge.txt','r',encoding='utf-8')
lineslist = f.readlines()
args = sys.argv

n= int(args[1])

for line in lineslist[:n]:
    print(line)
```

sysモジュールの`argv`メソッドを使った。  
これはファイル実行時にコマンド引数を与えてそれを読み込んファイル内で実行してくれる。  
`input()`を使うと、ファイルを実行してから値を入力して。それを使って処理がなされる。

```bash
#!/bin/bash

head -n $1 hightemp.txt
```

`$0`はスクリプト名で、`$1`はコマンド引数の一つ目を指す変数になる。  
`head`で先頭から表示する。デフォルトでは10行表示してくれる。  
オプションで`-n`をつけると行数を指定できる。  

## 15.末尾のN行を出力

>自然数Nをコマンドライン引数などの手段で受け取り、入力のうち末尾のN行だけを表示せよ。  
確認にはtailコマンドを用いよ。

```python
import sys

f = open('merge.txt','r',encoding='utf-8')
lineslist = f.readlines()
args = sys.argv

n= int(args[1])

for line in lineslist[-n:]:
    print(line)
```

前問とほぼ同じ。スライス構造のとこを変えただけ。

```bash
#!/bin/bash

tail -n $1 hightemp.txt
```

前問とほぼ同じ。`head`を`tail`に変えただけ。
使い方もほぼ同じようだ。

## 16.ファイルをN分割する

>自然数Nをコマンドライン引数などの手段で受け取り、入力のファイルを行単位でN分割せよ。  
同様の処理をsplitコマンドで実現せよ。

```python
import sys
import math

f = open('hightemp.txt','r',encoding='utf-8')
lineslist = f.readlines()
args = sys.argv

num_totallines = sum(1 for line in open('hightemp.txt',encoding='utf-8'))
n= int(args[1])
num_lines = math.ceil(num_totallines/n) #切り上げ

print('分割数:',n)
print('１つのパラグラフの行数:',num_lines)

for num_paragraph in range(n):
    print(num_paragraph+1)
    offset = num_paragraph*num_lines

    for line in lineslist[offset:offset+num_lines]:
        print(line)

```

N行ずつ抽出、ではなくてN分割、ということが少し難しかった・・・  
切り上げと切り下げで場合分けをした方がよりN分割ぽさが出ると思う。

```bash
#!/bin/bash

echo -n "分割数は？"
read n

count=`wc -l hightemp.txt | cut -f 1 --delim=" "`
num_lines=`expr $count / $n`
remainder=`expr $count % $n`

if [ $remainder -gt 0 ]; then
    num_lines=`expr $num_lines + 1`
fi

split -l $num_lines hightemp.txt paragraph
```

パイプでコマンドを同時に使えるようになる。  
`cut`のオプションではフィールド指定と、区切り文字の指定をしている.  
`echo`のオプション`-n`は改行なしで出力の意味。  
計算した値を使いたいときは`expr`を使う。  
`split`は`-l`で分割したい行数を指定している。文字数やバイト数の指定もできる。
  
## 17.1列目の文字列の異なり

>1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

```python
f = open('hightemp.txt',encoding='utf-8')
prefecture_set=set()

for line in f.readlines():
    word_list = line.split()
    prefecture_set.add(word_list[0])

print(prefecture_set)
```

setは重複しないデータセットなので、リストをどんどん空のセットにぶちこんで
いくだけでsetができる。支離滅裂な日本語で申し訳ない。

```bash
#!/bin/bash

cut -f 1 hightemp.txt | sort -u > q17_result.txt
```

shellscriptすばらしくない？1行で済んでんけど。
`sort`のオプション`-u(--uniq)`で重複なしの並べ替えをしてくれる。

## 18.各行を3コラム目の数値の降順にソート

>各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）

```python
from operator import itemgetter

with open('hightemp.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

def is_float(s):
    try:
        float(s)
    except ValueError:
        return str(s)
    else:
        return float(s)

s_list = []
line_list = []

for line in lines:
    line = line.split('\t')
    s_list = [is_float(s) for s in line]
    line_list.append(s_list)

print(sorted(line_list, key = itemgetter(2) ,reverse=False))
```

一応ほしい結果は出たけど、もっと簡単な書き方があるはずなんだよなー  
`itemgetter`を使いたくてこうなったのかもしれない。ラムダ式より  
見た目に分かりやすかったので使いたかった。内包表記でlist作成したのも  
関数を自作したのも初めてでいい勉強になった。次回からガンガン使えるように  
なったわけではないけれど・・・  
内包表記で作るリストの方が`append()`よりも速いらしい。

##　19．各行の1コラム目の文字列の出現頻度を求め、出現頻度の高い順に並べる

>各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ

```python
from collections import Counter
from operator import itemgetter

f = open('hightemp.txt', encoding = 'UTF-8')
line_list = f.readlines()

prefecture = []

for line in line_list:
    l = line.split('\t')
    prefecture.append(l[0])

#1つ目の方法
counter = Counter(prefecture)
for word, cnt in sorted(counter.items(), key = itemgetter(1), reverse = True):
    print('%s = %d 回' %(word, cnt))

#2つ目の方法
for word, cnt in counter.most_common():
    print(word, cnt)
```

二通りの書き方を見つけたのでどちらも書いた。  
どちらが優れているのかは分からない。組み込み関数？を使ってる後者のほうが  
速いかもしれない。処理が分かりやすいのは前者かなと思ったので書きました。 

これにて2章終了！お疲れさまでした。