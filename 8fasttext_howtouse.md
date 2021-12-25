# 1.分散表現
### ファイル形式
```
けもの　は　いても　のけもの　は　いない
男　は　いても　女　は　いない　
```


### 学習
```
$ ./fasttext skipgram -input data.txt -output model
```

## 単語の演算
- nardtreeさんが作ってるので拝借しよう
- [入力型類似度計算 fasttext.py](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data/blob/master/fasttext.py)
- [総当り類似度計算  term_similarity.py](https://github.com/GINK03/funnel-generator-rev-2.0/blob/master/term_similarity.py)
- Word2vec版もある
### 読み込みファイル生成
- 不要な部分を コメントアウトしてから実行する
- gemsimを使う
```
fasttext.py

def convert_fasttext2gensim():
  model = KeyedVectors.load_word2vec_format('model.vec', binary=False)
  open('fasttext.gensim-model.pkl', 'wb').write(pickle.dumps(model) )
  #model = KeyedVectors.load_word2vec_format('model.withuser.vec', binary=False)
  #open('fasttext.withuser.gensim-model.pkl', 'wb').write(pickle.dumps(model) )
  sys.exit()
```
```
python3 fastetext.py --convert
```

### 単語の演算とその類似度計算
- 引き算をしたい単語は「-」をつける
```
python3 fastetext.py --pred [単語] [単語] -[単語]
```
### 全単語との類似度計算
- ファイルの入出力を書き換える
- "CV"となっているところを計算したい単語に書き換える
```
python3 term_similarity.py --make_vector --sim --sort
```

<br>
<br>

# 2.テキスト分類学習
### ファイル形式
- ラベル、テキストのBoW
```
__label__海外総合 __label__北朝鮮情勢 __label__韓国の話題 __label__アメリカの話題 __label__海外の事件・事故 写真 拡大 鈴木宗男 ・ 新党大地 代表 と 、 元 外務省 主任 分析官 で 作家 の 佐藤優 氏 による 対談 講演会 「 東京 大地 塾 」 （ ２ ０ １ ６ 年 １２月 ２ ２ 日 開催 ） 。 週プレ ＮＥＷＳ 集中 連載 第 １ 回 目 の テー
```
### 学習
```
$ ./fasttext supervised -input train.txt -output model
```

### 再現度テスト
- 上位k個のラベルに正解が入っている割合を計算してくれる
```
./fasttext test model.bin test.txt k
```
### テキスト分類
- 予測結果を返してくれる
```
#予測結果のみ
./fasttext predict model.bin test.txt k
#確率付き
./fasttext predict-prob model.bin test.txt k
```

### ベクトルについて
- 生成されたベクトルは,演算はできないので注意
- アルゴリズムの関係で、前後の文脈を元にしていないためだと考えられる
- 類似を計算してもあくまで、似たラベルが出やすい単語が出てくるのみです

### 類似度計算(テキスト分類)
```
男
"女",0.7405307292938232
"料理",0.6924278736114502
"ゆで",0.6896716356277466
"レストラン",0.6487624645233154
"生産者",0.6480042338371277
```

### 類似度計算(分散表現)
```
"女",0.8337879180908203
"オトコ",0.7767778635025024
"この女",0.772354006767273
"悪い男",0.7593703269958496
"男なら",0.7511940002441406
```

## パラメーター設定
- wordNgrams:いくつの単語を１塊と見るか
- minn,maxn:サブサンプリングにおいて文字をいくつまで１塊見るか
```
./fasttext skipgram
Empty input or output path.

The following arguments are mandatory:
  -input              training file path
  -output             output file path

The following arguments are optional:
  -verbose            verbosity level [2]

The following arguments for the dictionary are optional:
  -minCount           minimal number of word occurences [5]
  -minCountLabel      minimal number of label occurences [0]
  -wordNgrams         max length of word ngram [1]
  -bucket             number of buckets [2000000]
  -minn               min length of char ngram [3]
  -maxn               max length of char ngram [6]
  -t                  sampling threshold [0.0001]
  -label              labels prefix [__label__]

The following arguments for training are optional:
  -lr                 learning rate [0.05]
  -lrUpdateRate       change the rate of updates for the learning rate [100]
  -dim                size of word vectors [100]
  -ws                 size of the context window [5]
  -epoch              number of epochs [5]
  -neg                number of negatives sampled [5]
  -loss               loss function {ns, hs, softmax} [ns]
  -thread             number of threads [12]
  -pretrainedVectors  pretrained word vectors for supervised learning []
  -saveOutput         whether output params should be saved [false]

The following arguments for quantization are optional:
  -cutoff             number of words and ngrams to retain [0]
  -retrain            whether embeddings are finetuned if a cutoff is applied [false]
  -qnorm              whether the norm is quantized separately [false]
  -qout               whether the classifier is quantized [false]
  -dsub               size of each sub-vector [2]
```

## 参考
- [fasttext公式](https://fasttext.cc/docs/en/support.html)
- [チートシート@公式](https://fasttext.cc/docs/en/cheatsheet.html)を見れば分かる
- [fastTextでテキスト情報から レシピ分類器を作った話](https://speakerdeck.com/atlimited/fasttextdetekisutoqing-bao-kara-resipifen-lei-qi-wozuo-tutahua)
- [fastTextの実装を見てみた](https://www.slideshare.net/shirakiya/fasttext-71760059)
