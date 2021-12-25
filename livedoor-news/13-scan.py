import requests
import concurrent.futures
import random
import os
import sys

def _map(arr):
G  index, iss = arr
  nmax = len(iss)
  base_url = 'http://news.livedoor.com/article/detail/{}/'
  headers = {'User-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
  
  for n,i in enumerate(iss):
    if os.path.exists('htmls2/{i}'.format(i=i)):
      print(n,nmax,i,"already")
      continue
    url = base_url.format(i)
    r = requests.get(base_url.format(i), headers = headers)
    r.encoding = r.apparent_encoding 
    #文字化けしていないかアクセス制限の確認
    if random.random() < 0.01:
      print(r.text)
    
    #削除記事リストは２重アクセスを防ぐため確認として保存
    if '<h1 class="errorTtl">指定されたページまたはファイルは存在しません</h1>' in r.text:
      #with open("deleted_list.txt","a") as f:
      #  f.write(str(i)+",")
      print(n,nmax, i, "deleted")
    else:
      with open('htmls/{i}'.format(i=i),'w') as f:
        f.write(r.text)
      print(n,nmax, i, "crawled---------------")   


arrs = {}
for index, i in enumerate(sorted(range(2000000,14380000), key=lambda x:x*-1)):
  key = index%128  
  if arrs.get(key) is None:
    arrs[key] = []
  arrs[key].append(i)

#昇順にしている
arrs = [ (index, random.sample(iss, len(iss))) for index, iss in arrs.items() ] 
print("start to scan")
#_map(arrs[-1])

#32分割したものを32CPUで並列処理。アクセス権限対策かなんかだろうか・・・
with concurrent.futures.ProcessPoolExecutor(max_workers=128) as ex:
  ex.map(_map, arrs) 
