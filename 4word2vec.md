## Word2vec（単語の分散表現）
- 概要
  - Harrisの分布仮説（同じ文脈で用いられる単語は似た意味を持つ）をベースに作られたモデル
  - 従来のDNN(RNNLM)に比べ、次元数が少なく時間が少ない。精度も良好（次元数は600程度）
  - 単語を複数の意味として解釈できる
  - 学習済みとしては東北大学 乾・岡崎研究室が作成した[日本語 Wikipedia エンティティベクトル](http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/)や国立国語研究室が作成した分散表現[nwjc2vec](http://www.anlp.jp/proceedings/annual_meeting/2017/pdf_dir/E1-5.pdf)が用いられる
  - HR領域ベクトルとして[ビズリーチ](https://github.com/bizreach/ai/tree/master/word2vec)が公開している
  - SNS領域ベクトルは[hotlink](https://www.hottolink.co.jp/blog/20190304-2)
  - モデル別学習済みを公開している人もいる[こちら](https://qiita.com/Hironsan/items/8f7d35f0a36e0f99752c)
  - Facebookなんかも公開しているらしい[こちら](http://blog.hassaku-labs.com/post/pretrained-word2vec/)
- 特徴
  - 数十万単位あるである単語群を数百次元のベクトルで表現できる
  - 複数の単語を同一の尺度で一元的に表現できる
  - 単語の意味の近さを表現できる
  - 単語の足し算引き算ができる
  - **一元的に管理することによSVMやNNにかけやすくなる**
- 懸念点
  - 同じ文脈で用いられる対義語も同じ意味だと認識される(例：私は前へ進む、私は後ろへ進む)
  - どのような文脈を学習させるかで結果が変わる（Twitterで学習すると口語表現、Wikipediaで学習すると文語）
  - データ数、次元数を増やすほど意味の精度はよくなる（反面次元数が増えると計算数が増える）

### Harrisの分布仮説
<p align="center">
  <img width="500px" src="https://user-images.githubusercontent.com/36536038/37505192-d68f4ff2-2926-11e8-81d2-5fb15bf85982.png">
</p>

> - 引用 [【論文紹介】Distributed Representations of Sentences and Documents@slideshare](https://www.slideshare.net/TomofumiYoshida2/distributed-representations-of-sentences-and-documents-70011001)
### Word Embedding
<p align="center">
  <img width="500px" src="https://user-images.githubusercontent.com/36536038/37505800-0733a34e-292a-11e8-9ca2-cec27df4dc17.png">
</p>

### CBoW , Skipgram
- CBoWは周辺の順番を考慮していないが、Skipgramは考慮している・・・？
<p align="center">
  <img width="500px" src="https://user-images.githubusercontent.com/36536038/37505813-109fed5c-292a-11e8-8766-1ada6b3472e1.png">
</p>


### 精度実験
#### 表３
- リストを用意してそれを元に精度比較
- （Mikolovの論文では3.2億語、8.2万語彙集（英語）、640次元ベクトルだった）
- ただし、速度やリソースが入っていない点に注意
```
TASK DESCRIPTION
To measure quality of the word vectors, we define a comprehensive test set that contains five types of semantic questions, and nine types of syntactic questions. Two examples from each category are shown in Table 1. Overall, there are 8869 semantic and 10675 syntactic questions. The questions in each category were created in two steps: first, a list of similar word pairs was created manually. Then, a large list of questions is formed by connecting two word pairs. For example, we made a list of 68 large American cities and the states they belong to, and formed about 2.5K questions by picking two word pairs at random. We have included in our test set only single token words, thus multi-word entities are not present (such as New York).

We evaluate the overall accuracy for all question types, and for each question type separately (semantic, syntactic). Question is assumed to be correctly answered only if the closest word to the vector computed using the above method is exactly the same as the correct word in the question; synonyms are thus counted as mistakes. This also means that reaching 100% accuracy is likely to be impossible, as the current models do not have any input information about word morphology. However, we believe that usefulness of the word vectors for certain applications should be positively correlated with this accuracy metric. Further progress can be achieved by incorporating information about structure of words, especially for the syntactic questions.
```

<p align="center">
  <img width="500px" src="https://user-images.githubusercontent.com/36536038/37507424-c2de3166-2931-11e8-83c8-a7b964ffaad3.png">
</p>

> 引用　[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)

## fast text
### Word2Vecからの主な変更点
- 学習速度が速くなっている
- 活用形も認識する
- ラベルによるtext分類機能がある

<p align="center">
  <img width="1000px" src="https://camo.qiitausercontent.com/27ae86df54cc53e4b51d3e1b7c3a270ec04b2e4d/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f32353939302f36623133626561332d373633392d636462372d363735662d3661366562333133656536332e706e67">
</p>

> 引用　https://qiita.com/icoxfog417/items/42a95b279c0b7ad26589

### テキスト分類
- SVMでは分類できない以下の問題を解決している
- 「出力カテゴリーが多用な大規模なコーパスにおいて、低出現頻度カテゴリーの分」
- アルゴリズムはCBoWを応用したもので、「出力：文章ラベル　←入力：f(文章内単語)　」となっている
- 詳しくはfasttext_paper.mdを参照してください
<p align="center">
  <img width="500px" src="https://user-images.githubusercontent.com/36536038/37946195-11e0761c-31bf-11e8-91c8-4cf9463bc668.png">
</p>
> 

## Doc2Vec
- コンテキストと一緒に文書も学習させる仕組み
- CBoWのほうがよいことが実証されている
<p align="center">
  <img width="500px" src="https://cdn-ak.f.st-hatena.com/images/fotolife/k/kento1109/20171117/20171117112613.png">
</p>


## 理論背景
### 自然言語処理
- Word Embedding(単語ベクトル化論)
  - Bag of Words
  - N-gram
  - one-hotベクトル
  - 分散表現
- Harrisの分布仮説
### 数理モデル
- ニューラルネットワーク
- CBoW
- Skipgram
- シグモイド関数
- softmax関数
### 最適化
- Shanonの情報理論
- 情報エントロピー
- 損失関数
- Shanonの補助定理
- カルバックライブラリー情報量
- クロスエントロピー
- Negative Sampling

## 事例集
- 商品レコメンド　[リクルート](https://www.slideshare.net/recruitcojp/ss-56150629)
- 単語の推薦：機械翻訳・チャットボット
- 単語の意味分析：絵文字の分析

## 参考文献
### 理論解説
- [Word2Vec概要](https://deepage.net/bigdata/machine_learning/2016/09/02/word2vec_power_of_word_vector.html)
- [fasttext概要](https://deepage.net/bigdata/machine_learning/2016/08/28/fast_text_facebook.html)
- [Doc2Vec概要](https://deepage.net/machine_learning/2017/01/08/doc2vec.html)
- [Word2Vec vs fasttext](http://catindog.hatenablog.com/entry/2017/03/31/221644)
- [文献紹介：Efficient Estimation of Word Representations in Vector Space @youtube](https://www.youtube.com/watch?v=EIcY4Juy77c)
- [【論文紹介】Distributed Representations of Sentences and Documents@slideshare](https://www.slideshare.net/TomofumiYoshida2/distributed-representations-of-sentences-and-documents-70011001)
- [ゼロからつくるディープラーニング2（プレビュー版）](https://www.dropbox.com/sh/ev6a40fbagw2qtz/AABF2zxkvo12H7-b25eYxsBKa?dl=0)

### 実例
- [fasttext github](https://github.com/facebookresearch/fastText)
- [gensimでDoc2Vec](http://kento1109.hatenablog.com/entry/2017/11/15/181838)
- [fasttext_tutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial)
