## Item2Vec
- [ITEM2VEC: NEURAL ITEM EMBEDDING FOR COLLABORATIVE FILTERING ](https://arxiv.org/abs/1603.04259)
- アイテムのレコメンドにおいて、直近のみの影響ではなく集合の影響（英文読んだけど日本語がうまい思いつかない）と仮定する。
- つまり、ウインドウを∞とし、Word2Vecを行う
- 解説記事  :http://ohke.hateblo.jp/entry/2017/12/02/230000
- 活用例　   :http://ohke.hateblo.jp/entry/2017/12/08/230000

<p align="center">
  <img  src="https://user-images.githubusercontent.com/36536038/37566827-96b8ed98-2b01-11e8-9dcf-9010c56a65da.png">
</p>

## Webニュースデータのカテゴリ分類　2016
- [教師なしデータを利用した単語の分散表現と事前学習を用いた Web ニュースデータのカテゴリ分類](http://repo.lib.hosei.ac.jp/bitstream/10114/12720/1/14R6204%E5%8A%A0%E8%97%A4%E8%AB%92%E7%A3%A8.pdf)
1. Word2vec
2. 文書ベクトルを単語の平均ベクトルで算出
3. DNNのAutoencoderによる事前学習→少数の教師データでファインチューニング
<p align="center">
  <img width="1000px" src="https://user-images.githubusercontent.com/36536038/37566586-8cf1538e-2afe-11e8-8f8e-b45355c90731.png">
</p>

## Doc2Vecのアルゴリズム検証
- [Paragraph Vector と多層パーセプトロンを用いた有害文書の分類手法](http://oberon.nagaokaut.ac.jp/katsuk/papers/ipsj/15/data/pdf/1Q-09.pdf)
- Doc2vecにおけるPV-CBOWとPV-Skipgramの比較し、PVCBOWのほうがよいことを示唆

## Do2Vec実装例
- [分散表現空間解析モデルに基づく研究トレンドに関する考察](http://db-event.jpn.org/deim2017/papers/305.pdf)
- LDAでやられていたものをdoc2vecで実装し精度比較

## 語義による分散表現
- [教師データを用いた語義の分散表現の構築](http://www.anlp.jp/proceedings/annual_meeting/2017/pdf_dir/E1-1.pdf)
- 語義による分散表現という点で新しい
1. 単語をWordnetによる語義の分散表現の和で表現する（既存研究）
2. 語義を元にした分類手法を提案し、SVMと比較する
3. SVMのほうが精度がよく、素直に負けを認める
- 参考：Word_net
  - https://www.yoheim.net/blog.php?q=20160201

<p align="center">
  <img width="400px" src="https://user-images.githubusercontent.com/36536038/37566795-4499acbe-2b01-11e8-88d2-7c3c8f4ed5e2.png">
</p>

## ウィンドウ数の分析
- [Dependency-Based Word Embeddings](https://levyomer.files.wordpress.com/2014/04/dependency-based-word-embeddings-acl-2014.pdf)
- [arXivTime](https://github.com/arXivTimes/arXivTimes/issues/118)
- [stack overflow](https://stackoverflow.com/questions/22272370/word2vec-effect-of-window-size-used)
- 広くするのほうが文脈に反映されやすいだとか。まぁそうだよね

## 協調フィルタリング
- [nardtree氏によるまとめ](https://github.com/GINK03/bookmeter-recommender)
- [推薦システムのアルゴリズム](http://www.kamishima.net/archive/recsysdoc.pdf)


