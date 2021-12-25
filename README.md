# NLP
- 自然言語を用いた機械学習をするために１から学ぶ
- 自然言語処理の教科書から最近の研究まで触れる

## 目標
- 使う予定があるSVM,Word2Vec,fasttext,BERTを使った分析を行う
- 文献に書かれていないことまで把握する（行間まで読む）

## 基礎理論
### NLP基礎
- [1NLPの基本用語](https://github.com/matsuda-hiromu/NLP/blob/master/1NLP.md)
- [2形態素解析ツール](https://github.com/matsuda-hiromu/NLP/blob/master/2tokenizer.md)
- [NLP前処理まとめ（外部）](http://yukinoi.hatenablog.com/entry/2018/05/29/120000)
- [前処理、正規表現と名詞抽出](https://github.com/matsuda-hiromu/NLP/blob/master/pre_preprocess.md)
### SVM/Logistic
- [3基本中の基本、SVM理論](https://github.com/matsuda-hiromu/NLP/blob/master/3SVM.md)

### Word2Vec
- [4単語の分散表現理論](https://github.com/matsuda-hiromu/NLP/blob/master/4word2vec.md)
- [5分散表現の応用例](https://github.com/matsuda-hiromu/NLP/blob/master/5word2vec_paper.md)

### fasttext
- [6fasttextの処理能力](https://github.com/matsuda-hiromu/NLP/blob/master/6fasttext_machine.md)
- [7fasttextの理論解読](https://github.com/matsuda-hiromu/NLP/blob/master/7fasttext_theory.md)
- [8fasttextの使い方](https://github.com/matsuda-hiromu/NLP/blob/master/8fasttext_howtouse.md)


## 実装
### 1.用いるデータ
- タグ付きのコーパスであるLivedoorNewsをスクレイピング
- [Livedoor_Newの特徴](https://github.com/matsuda-hiromu/NLP/blob/master/livedoor-news/readme.md)
- [データの状況](https://github.com/matsuda-hiromu/NLP/tree/master/EDA)


### 2.SVM/Logisticによるテキスト分類
- [不均衡データに対するSVM](https://github.com/matsuda-hiromu/NLP/tree/master/SVM)

### 3.fasttext単語の演算・テキスト分類
- [単語の演算・テキスト分類](https://github.com/matsuda-hiromu/NLP/tree/main/Fastext)


### 付録
- [テキスト分類_試し例](https://github.com/matsuda-hiromu/NLP/tree/master/labeling)
- [ストップワード作成](https://github.com/matsuda-hiromu/NLP/tree/main/stop_words)
- Topic Modelによる分類→[プログラム](https://github.com/matsuda-hiromu/NLP/blob/master/topic.py)
- Apriori algorithmによる共起ワードの抽出→[プログラム](https://github.com/matsuda-hiromu/NLP/blob/master/busket.py)
- **日本語の文章をGoogle翻訳にかけて英語にし、、それを機械学習に取り込んだあとで、日本語に戻す手法もある**


## 学習済みモデル
### Node2vecを用いた単語の分散表現(学習済みモデル）
- [Wikipediaの内部リンクを用いた Node2vecによる単語の分散表現](https://repose.hatenadiary.jp/entry/2019/01/25/221303)
- 同じ内部リンク（＝同じ辞書単語が説明文に入っている単語）は近しい意味

### Doc2vecによる単語の分散表現（学習済みモデル）
- [Doc2vecによる単語の分散表現](https://yag-ays.github.io/project/pretrained_doc2vec_wikipedia/)
- 説明文に同じ単語がある単語は近しい意味

### 日本語BERT
- [理論的な解説](https://ledge.ai/bert/)
- [実装例：分散表現と類似度](https://github.com/matsuda-hiromu/NLP/blob/master/Japaneze_BERT.ipynb)

### 学習用コーパス
- [機械学習に使える日本語の対訳コーパスデータセット](https://gengo.ai/ja/datasets/japanese-language-text-datasets/)



## コンペで強いと言われているモデル
- w2vと単次元CNNが一番強いらしい > 参考[CNNを利用したセンチメント分析](http://catindog.hatenablog.com/?page=1471927301)
- またNLPで出来そうなことを一通り打ち込みましたみたいなものもある[FakeNewsコンペ](https://github.com/Cisco-Talos/fnc-1)
<br>
<br>
<br>

## その他
### 文章自動生成
- [応用例：文章自動生成](http://catindog.hatenablog.com/entry/2017/05/26/224530)
- [関連する状態遷移モデルまとめ論文](https://www.jstage.jst.go.jp/article/jasmin/2017f/0/2017f_22/_pdf)
- [rinna社の取り組み](https://prtimes.jp/main/html/rd/p/000000009.000070041.html)

### 自動要約
- [Skip-Thought Vectors](http://ksksksks2.hatenadiary.jp/entry/20160424/1461494269)
- [自動要約　まだ英語のみ](https://techblog.exawizards.com/entry/2018/08/23/121437)
- [簡易要約](http://www.sigwi2.org/wp-content/uploads/2017/12/WI2-2016-26.pdf)
- [中間要約](http://www.anlp.jp/proceedings/annual_meeting/2017/pdf_dir/P7-4.pdf)
- [おまけ：論文要約](http://anlp.jp/proceedings/annual_meeting/2017/pdf_dir/P3-1.pdf)
- [BERT登場後の自動要約](https://qiita.com/siida36/items/4c0dbaa07c456a9fadd0#14-bert%E3%81%AE%E7%99%BB%E5%A0%B4%E3%81%9D%E3%81%97%E3%81%A6%E6%8A%BD%E5%87%BA%E5%9E%8B%E8%A6%81%E7%B4%84%E3%81%AE%E5%86%8D%E6%B5%81%E8%A1%8C-2019)

### TopicModel
- [対話型トピックモデルライブラリーpyLDAvis](https://nbviewer.jupyter.org/github/bmabey/pyLDAvis/blob/master/notebooks/pyLDAvis_overview.ipynb)
- [巨大トピックモデル](https://github.com/Microsoft/LightLDA)
###  metapath2vec
- 状態遷移モデルとしてword2vecから複雑なネットワークに拡張したもの
- [→論文](https://ericdongyx.github.io/papers/KDD17-dong-chawla-swami-metapath2vec.pdf)

### オープンソース日本語NLPライブラリ
- [リクルートGINZA](https://www.recruit.co.jp/newsroom/2019/0402_18331.html)
<br>
<br>
<br>

## その他資料
- [外国語の自然言語処理まとめ](https://github.com/sebastianruder/NLP-progress)
- [wikipediaによるIDF辞書](http://catindog.hatenablog.com/entry/2017/02/15/222915)
- [TF-IDFと正規化について](https://hayataka2049.hatenablog.jp/entry/2018/03/19/125436)
- [SCDV](https://qiita.com/fufufukakaka/items/a7316273908a7c400868#%E6%96%87%E6%9B%B8%E3%83%99%E3%82%AF%E3%83%88%E3%83%AB%E3%81%AE%E5%8F%AF%E8%A6%96%E5%8C%96)
- [TF-hubにおける学習済みモデル](https://tfhub.dev/google/nnlm-en-dim128/1)
- [論文：分散表現の次元数について](https://papers.nips.cc/paper/7368-on-the-dimensionality-of-word-embedding)
- [自然言語処理におけるNNの歴史](http://blog.aylien.com/a-review-of-the-recent-history-of-natural-language-processing/)
- [Word2vecの逐次学習（Yahoo OSSライブラリー）](https://techblog.yahoo.co.jp/oss/yskip/)
- [sentence pice](htps://www.smartbowwow.com/2019/02/sentencepiecepython.html)
