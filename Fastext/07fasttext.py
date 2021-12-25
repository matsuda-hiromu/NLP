#contents1424_1480
# *0_*
import glob 
import json
import pickle
import sys
import gzip


def f():
  tag_index = pickle.load( gzip.open('./tag_4keta.pkl.gz', 'rb') )
  f = open("train_4keta.txt","w")
  for path in glob.glob("../../03scraping_challenge/livedoor-news/wakachi/*0_*"):
    print(path)
    for i,name in enumerate(glob.glob("{}/*".format(path))):
      row = ""
      obj = json.load(gzip.open(name,"rt"))
      # ラベル付け
      for tag in obj["tag"]:
        if tag_index.get(tag) is not None:
          row += "__label__{} ".format(tag)
      # 書き込み
      row += (obj["bodies"])
      f.write('{}\n'.format(row))
      
      #if i > 100:sys.exit()
f()
