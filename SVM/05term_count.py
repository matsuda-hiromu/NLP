import os
import glob
import json
import MeCab
import pickle
import sys
from collections import Counter
import gzip
import csv

def step1(): # term index
  term_count = {}
  counts = 0
  for i,path in enumerate(glob.glob("../wakachi/contents*")):
    print(i,path)
    for name in glob.glob("{}/*".format(path)):
      obj = json.load(gzip.open(name,"rt"))
      obj['bodies'] = obj['bodies'].split()
      for term in obj['bodies']:
        if term_count.get(term) is None:
          term_count[term] = 0
        term_count[term] += 1
        counts += 1
        
  outcsv = open("term_count_sorted.csv","w")
  writer = csv.writer(outcsv)       
  for term, count in sorted(term_count.items(), key=lambda x:x[1]):
    row = [term,count/counts]
    writer.writerow(row)
  writer.writerow(["all",counts])

#step1()


def step2(): # term index
  term_count = {}
  counts = 0
  for i,path in enumerate(glob.glob("../wakachi/contents*")):
    print(i,path)
    for name in glob.glob("{}/*".format(path)):
      obj = json.load(gzip.open(name,"rt"))
      obj['bodies'] = obj['bodies'].split()
      obj['bodies'] = list(set(obj['bodies']))
      for term in obj['bodies']:
        if term_count.get(term) is None:
          term_count[term] = 0
        term_count[term] += 1
        counts += 1
        
  outcsv = open("term_count_doc.csv","w")
  writer = csv.writer(outcsv)
  i = 0
  writer.writerow(["all",counts])
  for term, count in sorted(term_count.items(), key=lambda x:-x[1]):
    row = [term,count/counts]
    writer.writerow(row)
    i += 1

step2()
