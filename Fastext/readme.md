## Fasttextによるネット記事自動分類

## 概要
### 目的
- ネットの記事に自動でタグをつけたい
- fasttextによる分類を試してみる

### 実験方法
- データとして、タグ付きニュースサイトである[Livedoornewsをスレピングしたものを](https://github.com/dialectic4th/03scraping_challenge/tree/master/livedoor-news)用いる
- 学習データとテストデータを分けて性能を調査
- 似たような取り組みとしては、[カカクコムにおけるレシピ分類](https://speakerdeck.com/atlimited/fasttextdetekisutoqing-bao-kara-resipifen-lei-qi-wozuo-tutahua)がある

### fasttextの利点
- テキスト分類の基本手法は、２値分類のSVMやナイーブベイズがスタンダードである
- しかし、今回はマルチクラスの問題＆不均衡データなので、SVMだと工数が多くなりがち
- ニューラルネットワークであるfasttextだとそれらに対応できる

## テキスト分類のモデル
- SVMでは分類できない以下の問題を解決している
- 「出力カテゴリーが多用な大規模なコーパスにおいて、低出現頻度カテゴリーの分類」
- アルゴリズムはCBoWを応用したもので、「出力：文章ラベル　←入力：f(文章内単語)　」となっている
- 詳しくはfasttext_paper.mdを参照してください
<p align="center">
  <img width="500px" src="https://user-images.githubusercontent.com/36536038/37946195-11e0761c-31bf-11e8-91c8-4cf9463bc668.png">
</p>

<p align="center">
  <img width="1000px" src="https://camo.qiitausercontent.com/27ae86df54cc53e4b51d3e1b7c3a270ec04b2e4d/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f32353939302f36623133626561332d373633392d636462372d363735662d3661366562333133656536332e706e67">
</p>
> 引用　https://qiita.com/icoxfog417/items/42a95b279c0b7ad26589




## 結果
- [全結果](http://nbviewer.jupyter.org/github/dialectic4th/11NLP_study/blob/master/Fastext/test_cheak.ipynb)
- 全体として7割り程度当たっている
- 例えば、4行目は外れているが、記事を見ると十分妥当(正解ラベルはビューティであるが記事内容は恋愛と言ってよい)
- 12行目は迷っているor複数だと考えているが、当たっている（notebook参照）
- 意味的に内包するものは、判定ができない（アメリカ⊂海外総合)
- データ数としては１万程度あれば精度が７０％程度出る（先行事例と結果が一致）

### 結果(一部)
![image](https://user-images.githubusercontent.com/36536038/38069277-7c439ab0-3350-11e8-904a-517a47048516.png)


### 成功例（３行目）
![image](https://user-images.githubusercontent.com/36536038/38069497-b0b59482-3351-11e8-8deb-d2194c805aa2.png)

> 引用：http://news.livedoor.com/article/detail/12714019/
> 問題があれば削除いたします

### 失敗例（46,21行目）
![image](https://user-images.githubusercontent.com/36536038/38073328-7d9afc7c-3365-11e8-8512-6e36fa4f0167.png)
