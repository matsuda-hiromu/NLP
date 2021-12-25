
## 解析ツール
### 形態素解析
- mecab
  - 最もメジャーな形態素解析ツール
  - 論文や公式記事を解析するのに向いている
  - 省略や表記の揺れの無い文章を処理するは最適
  - 処理速度も速い
- juman++
  - ２０１６年に開発されたRNNを使った形態素解析ツール
  - ブログや音声認識を解析するのに向いている
  - 話し言葉や表記揺れに強い
  - 解析が遅く辞書もNelogd少ない
  - 補足：[Nelogdを使う方法](https://qiita.com/Kensuke-Mitsuzawa/items/403256129e812b09c461)

![image](https://user-images.githubusercontent.com/36536038/37570925-8056fe86-2b39-11e8-9223-731eeedf618c.png)
- JUMAN＋＋の最新版が出た
> 引用https://drive.google.com/file/d/1DVnrsWw4skRgC8jU6_RkeofOQEHFwctc/view
- 構文解析
  - Cabocha
  - KNP
- 辞書なし形態素解析ツール
  - KyTea
  - TinySegmenter
- その他
  - janome:mecabよりも導入が簡単。でも辞書が古い・・・？
  - yahooとか

###  辞書
- 辞書は色々あるらしい

### 発展の経緯
- Prolog　 →　 JUMAN,KAKASI → ChaSen  → Mecab →JUMAN++

## 参考
- [入門自然言語処理@Amazon](https://www.amazon.co.jp/%E5%85%A5%E9%96%80-%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%87%A6%E7%90%86-Steven-Bird/dp/4873114705)
- [Juman++作者](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN++)
- [Juman++とは](https://deepage.net/machine_learning/2017/01/16/juman++.html)
- [Mecab_Juman++比較１](https://qiita.com/WaterIsland/items/6f30f0d8904665ac66c8#%E5%95%8F%E9%A1%8C%E7%82%B9-2)
- [Mecab_Juman++比較2](https://qiita.com/riverwell/items/438e88427363511e9f28#juman%E3%81%AE%E3%83%A1%E3%83%AA%E3%83%83%E3%83%88)
