## 問題意識
- SVMは、マージン最大化するバリアンスが低い識別器
- 計算アルゴリズムも基本はわかる
- （KKT条件・双対問題・ソフトマージンとかで基本手計算めんどい・・・）
- しかし、わからないことがあるので調べる
  - ツール:libSVM,liblinearの違い
  - チューニング
  - カーネル
  - 正則化項
  - オプションに存在するdual primalとは何か
  
 
## ツール
### liblinear
  - 線形カーネルにおける学習に特化したツール
  - 学習が速い
  - ロジスティック回帰もサポート
  - ver2から Cのチューニングができるようになっている
  - 基本は、分類の「L2正則化(L2マージン)SVM双対問題」を使う
  - (公式も行ってるけどL1マージンSVRとかいらんだろ)
  - 確率値がほしいときはロジスティック回帰
  - 分類ののときの誤差項Cはチューニングしてくれる（2017/3追加） 
  - **学習アルゴリズムの都合上スケール調整はしましょう(例えばlogとか)** [参考](http://kamonohashiperry.com/archives/19)
  - **学習データの１行目が１でないと結果が反転する** [参考]（http://dekioto.jugem.jp/?eid=1）
### libSVM
  - 非線形カーネルに対応したツール
  - データ数＞特徴量^2のときに、RBFカーネルを使うとよい
  - 大規模すぎると計算長くなるので注意（もはや勾配Boostingやランダムフォレストでも使えって話）
- 参考
  - [liblinear](https://www.csie.ntu.edu.tw/~cjlin/liblinear/)
  - [lib-linear FAQ](https://www.csie.ntu.edu.tw/~cjlin/liblinear/FAQ.html)
  - [LIBSVMの使用方法全般](http://data-science.gr.jp/implementation/iml_libsvm_usage.html)
  - [SVM実践ガイド](http://d.hatena.ne.jp/sleepy_yoshi/20120624/p1)
  - [長岡自然言語処理研究室](http://www.jnlp.org/lab/graduates/sannomiya/libsvm)
  - [中川研究室](http://www.r.dl.itc.u-tokyo.ac.jp/node/57)
  - [かものはしさんSVMリンク集](http://kamonohashiperry.com/archives/19)
 
## 数理モデル的なお話
- ソフトマージンと正則化回帰は似た問題として落とせる
- 主問題（primal）,双対問題(dual),正則化(regularized)、マージン(loss)に該当（最後は意訳）
- RBFカーネルを使う理由は下記を同時に満たすからである
  - 各データの差分を取ることでN^2にデータを変形（独立しているのはもちろんN個）
  - 差分を正規分布に基づいて配置
  - 事実上分布の仮定をおける&数理的に等価
  - 高次元空間に写像することで、超平面に分離しやすくなる
  - **ただし、次元数が多い場合は、写像せずに超平面で区切ればよい**
- 次元数もデータ数も多いときは学習時間次第でLibSVMかLiblinearか選ぶ
- 正則化項（どうでもいい重みが0に向かう）
  - L1だとスパースになりやすい
- 参考
  - [サポートベクターマシン - 統計数理研究所](http://www.ism.ac.jp/~fukumizu/ISM_lecture_2006/svm-ism.pdf)
  - [クラシックな機械学習の入門　　5. サポートベクターマシン　東京大学中川研究室](https://www.slideshare.net/hirsoshnakagawa3/kernel1a)
  - [線形回帰　東京大学中川研究室](http://www.r.dl.itc.u-tokyo.ac.jp/~nakagawa/SML1/lineaR1.pdf)
  - [ソフトマージン ブログ](http://aidiary.hatenablog.com/entry/20100503/1272889097)
  - [A Dual Coordinate Descent Method for Large-scale Linear SVM](http://www.cs.virginia.edu/~kc2wc/papers/HCLKS08.pdf)
  - [正則化学習法](http://imi.kyushu-u.ac.jp/~waki/ws2013/slide/suzuki.pdf)
  - はじめてのパターン認識
  - イラストで学ぶ機械学習

## 勉強メモ
- ヒンジ関数にSlack変数入れ忘れてるけど気にしない
![image](https://user-images.githubusercontent.com/36536038/37728455-9f6c36ce-2d7d-11e8-9ba7-e115a6bc8f27.png)
![image](https://user-images.githubusercontent.com/36536038/37728490-b7481e3e-2d7d-11e8-8292-763cf1ad8b7e.png)

![image](https://user-images.githubusercontent.com/36536038/37728470-aee0f676-2d7d-11e8-9b38-e9c14264e866.png)
