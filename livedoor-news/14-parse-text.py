import bs4
import MeCab
import os
import glob
import concurrent.futures
import json
import os
import sys
import gzip

def _map(arg):
  #m = MeCab.Tagger("-Owakati")
  key,names = arg
  nmax = len(names)
  for i,name in enumerate(names):
      print(i,nmax,name)
      save = name.split('/').pop()
      
      if os.path.exists('contents/{save}.gz'.format(save=save)):
        continue
      
      soup = bs4.BeautifulSoup(open(name).read(), "html5lib")

      #タイトル取得してなかったら記事削除として扱っている
      title = soup.find("h1", {"class" : "articleTtl"}) 
      if title is None:
        #print("title None")
        continue
    
      time = soup.find("time", {"class":"articleDate"})
      body = soup.find("div", {"class":"articleBody"} )
      tag = soup.find("meta",{"name":"news_keywords"})
      taglist = tag["content"].split(",")

      time = time.text
      titles = title.text.strip()
      bodies = body.text.strip()
      #bodies = m.parse(bodies).strip()
      
      o = {"time":time, "titles":titles, "bodies":bodies, "tag":taglist }
      gzip.open('contents/{save}.gz'.format(save=save), 'wt').write( json.dumps(o, indent=2, ensure_ascii=False) )


args = {}
for index, name in enumerate(glob.glob('htmls/*')):
  key = index%128
  if args.get(key) is None:
    args[key] = []
  args[key].append( name )
args = [(key,names) for key,names in args.items()]
#_map(args[0])

with concurrent.futures.ProcessPoolExecutor(max_workers=128) as exe:
  exe.map(_map, args)
