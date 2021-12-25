
## 正規表現と区別をつける
```
word_normalize = word_normalize.replace("\\","")
word_normalize = word_normalize.replace("*","\*").replace("+","\+").replace(".","\.").replace("?","\?")
word_normalize = word_normalize.replace("^","\^").replace("$","\$").replace("-","\-").replace("|","\|").replace("/","\/")
word_normalize = word_normalize.replace("[","\[").replace("]","\]")
word_normalize = word_normalize.replace("{","\{").replace("}","\}").replace("(","\(").replace(")","\)")
```

## Mecabで名詞のみ抽出

```
m = MeCab.Tagger()
term_details = m.parse(text).split('\n')
for term_detail in term_details:
    if term_detail not in ['EOS',""] and term_detail.split('\t')[1].split(",")[0] in ['名詞']:
        term  = term_detail.split('\t')[0]
```
   
