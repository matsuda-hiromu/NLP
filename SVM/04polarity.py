import json
import glob
import gzip
import sys
import concurrent.futures
from collections import Counter
import math
import csv
#ポジネガの辞書読み込み
term_weight = json.load(open('term/2term_weight.json'))
term_positive = { term:weight for term,weight in term_weight.items() if weight > 0.0 }
term_negative = { term:weight for term,weight in term_weight.items() if weight < 0.0 }

#urlのBoWを読み込み、点数付け
url_contexts = []
def polarity(url):
    with gzip.open(url,"rt") as f:
      context = f.read()
    url = url.replace("../../../../work/bf/2scraper/bow/","").replace(".gz","")
    terms = context.split()

    # リスト内で、各単語の出現回数nを数え、{term:log(n+1)} にする
    term_freq = dict(Counter(terms))
    freqs = len(terms)
    context = {term:freq/freqs for term, freq in term_freq.items() }

    #URLの点数を計算    点数*log(
    nega = sum( [ term_negative[term] * context[term] for term in terms if term_negative.get(term) ] )
    posi  = sum( [ term_positive[term] * context[term] for term in terms if term_positive.get(term) ] )
    print(url.replace("___","/"),nega,posi,posi+nega)
    # > polarity.csv 吐き出し
    writer.writerow([url.replace("___","/"),posi,posi+nega,nega])
    
    
#分散処理
if __name__ == '__main__':
  outcsv = open("polarity.csv","w")
  writer = csv.writer(outcsv)
  urls = glob.glob("../../../../work/bf/2scraper/bow/*")
  with concurrent.futures.ProcessPoolExecutor(max_workers=12) as executor:
    executor.map(polarity, urls)
