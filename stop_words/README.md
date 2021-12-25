# 19stop_words
テキストマイングにおいて除外したいワードリストを作成する

## 地方
- https://www.jma.go.jp/jma/kishou/know/yougo_hp/tiikimei.html
- https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E5%9C%B0%E5%9F%9F

## 天気
- https://www.jma.go.jp/jma/kishou/know/yougo_hp/sakuin.html

##アルファベット判定 
```
def isalnum(s):
    alnum_Reg = re.compile(r'^[a-zA-Z0-9_!-/:-@¥[-`{-~]+$')
    return alnum_Reg.match(s) is not None
  
```


## word2vec
- Word2vecで類義語を作りストップワードを作ることができる
![image](https://user-images.githubusercontent.com/36536038/46347273-f9481180-c685-11e8-9a36-200aecc97522.png)
