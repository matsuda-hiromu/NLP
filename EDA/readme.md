## 探索的分析 （Exploratory data analysis)
- 機械学習をかけるにしても事前にデータの概要は知るべき

## 実験①単語の出現数
### 目的
- 文章の構成単語は、一部に偏ってるというのはNLPでよく聞く話である
- しかし、実際に自分の目で確かめたことはない
- ストップワード削除の検討がてら確かめてる
### 実験結果
- mecabで分解
- 各形態素が出現している記事数を数え、全記事数で割りグラフ化
![image](https://user-images.githubusercontent.com/36536038/37956778-4086a4dc-31e7-11e8-8e4e-a8669b84059e.png)

![image](https://user-images.githubusercontent.com/36536038/37956804-4d3649ee-31e7-11e8-9366-114cada1dea1.png)


## 実験②タグの分布
- http://nbviewer.jupyter.org/github/matsuda-hiromu/NLP/blob/master/EDA/tag_plotly.ipynb
![image](https://user-images.githubusercontent.com/36536038/38081084-191cffca-337e-11e8-8553-197e324f991a.png)
