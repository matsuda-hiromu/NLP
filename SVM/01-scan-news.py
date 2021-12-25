import os
import glob
import json
import MeCab
import pickle
import sys
from collections import Counter
import gzip


# to list メモリ不足で没
if '--step1' in sys.argv:
  for path in glob.glob("../wakachi/contents*"):
    objs = []
    print(path)
    for name in glob.glob("{}/*".format(path)):
      obj = json.load(gzip.open(name,"rt"))
      #リスト化
      obj['bodies'] = obj['bodies'].split()
      #print(obj)
      objs.append(obj)
      
    save =path.replace("../wakachi/contents","")
    with open('./pkl/objs{}.pkl'.format(save), 'wb') as f:
      f.write( pickle.dumps(objs) )


# term index
if '--step2' in sys.argv:
  term_index = {}  
  for path in glob.glob("../wakachi/contents*"):
    for name in glob.glob("{}/*".format(path)):
      print(path,name)
      obj = json.load(gzip.open(name,"rt"))
      obj['bodies'] = obj['bodies'].split()
      for term in obj['bodies']:
        if term_index.get(term) is None:
          term_index[term] = len(term_index)
      #print(term_index)  
  open('term/term_index.json', 'w').write( json.dumps(term_index, indent=2, ensure_ascii=False) )

# make svm format
if '--step3' in sys.argv:
  term_index = json.load( open('term/term_index.json') )
  for path in glob.glob("../wakachi/contents*"):
    #print(path)
    for name in glob.glob("{}/*".format(path)):
      obj = json.load(gzip.open(name,"rt"))
      obj['bodies'] = obj['bodies'].split()
      
      #１つのデータごとにSVM形式
      if "国内の事件・事故" in obj["tag"] or "海外の事件・事故" in obj["tag"]:
        state = 1.0
      else:
        state = 0.0

      # 各単語の出現回数を数える（スペース区切りで数えてくれる）
      term_freq = dict(Counter(obj['bodies']))
    
      #番号と出現回数　、番号は0始まりから1始まりに変換　　　出現回数は形態素の出現頻度を用いる
      freqs = len(obj['bodies'])
      context = [ [term_index[term]+1,freq/freqs] for term, freq in term_freq.items() ]    
      #print(context)

      #liblinearに合わせるため、番号順に並べる
      context = sorted(context, key=lambda x:x[0])
      #print(context)

      #liblinearに合わせるため、 リストからスペース区切りに変換
      context = ' '.join( ['%d:%f'%(term, freq) for term, freq in context] )
    
      # 正解ラベルと特徴量の形に
      print( state, context )
      
# make svm format データ数調整
if '--step3.1' in sys.argv:
  term_index = json.load( open('term/term_index.json') )
  data_num = 0
  for path in glob.glob("../wakachi/contents*"):
    #print(path)
    for name in glob.glob("{}/*".format(path)):
      obj = json.load(gzip.open(name,"rt"))
      obj['bodies'] = obj['bodies'].split()
      
      #１つのデータごとにSVM形式 
      if "国内の事件・事故" in obj["tag"] or "海外の事件・事故" in obj["tag"]:
        state = 1.0
        data_num += 1
      elif data_num > 0:
        state = 0.0
        data_num -= 1
      else:
        continue

      # 各単語の出現回数を数える（スペース区切りで数えてくれる）
      term_freq = dict(Counter(obj['bodies']))
    
      #番号と出現回数　、番号は0始まりから1始まりに変換　　　出現回数は形態素の出現頻度を用いる
      freqs = len(obj['bodies'])
      context = [ [term_index[term]+1,freq/freqs] for term, freq in term_freq.items() ]    
      #print(context)

      #liblinearに合わせるため、番号順に並べる
      context = sorted(context, key=lambda x:x[0])
      #print(context)

      #liblinearに合わせるため、 リストからスペース区切りに変換
      context = ' '.join( ['%d:%f'%(term, freq) for term, freq in context] )
    
      # 正解ラベルと特徴量の形に > svm2.dat
      print( state, context )