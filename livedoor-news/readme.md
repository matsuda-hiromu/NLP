## 目的
- livedoorNewsにはタグがついている
- そこで、タグと時間付きのコーパスとして保存する
- それを他の機械学習に用いる
- テキスト分類や時系列解析を行う


## livedoorNewsはタグと時間付きのコーパス

<p align="center">
  <img width="500px" src="https://user-images.githubusercontent.com/36536038/38073544-8507f590-3366-11e8-9dfe-376b15ef96ae.png">
</p>


> 引用 http://news.livedoor.com/article/detail/14500370/
> 問題があれば削除いたします


## プログラム
- 13:クロール
- 14:記事をパース
- 15:記事を分かち書き
- 16:タグと時間について軽く分析
- [形態素の分布も調べました](https://github.com/matsuda-hiromu/NLP/tree/master/EDA)
