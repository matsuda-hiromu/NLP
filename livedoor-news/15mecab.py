import bs4
import MeCab
import os
import glob
import concurrent.futures
import json
import os
import sys 
import gzip



# フォルダ作成
for name in glob.glob('contentsall/*'):
  save = name.split('/').pop()
  os.system("mkdir wakachi/{}".format(save))

#分かち書き処理
def _map(arg):
  m = MeCab.Tagger("-Owakati")
  key,names = arg 
  nmax = len(names)
  for i,name in enumerate(names):
    print(i,nmax,name)
    save = name.replace("contentsall","wakachi")
    if os.path.exists('{save}'.format(save=save)):
      continue

    content = json.load(gzip.open(name,"rt"))
    content["bodies"] = m.parse(content["bodies"]).strip()

    #print(content)
    gzip.open('{save}'.format(save=save), 'wt').write( json.dumps(content, indent=2, ensure_ascii=False) )
    

#並列処理
args = {}
for index, name in enumerate(glob.glob('contentsall/contents0*/*')):
  key = index%64
  if args.get(key) is None:
    args[key] = []
  args[key].append( name )
args = [(key,names) for key,names in args.items()]

#_map(args[0])

with concurrent.futures.ProcessPoolExecutor(max_workers=64) as exe:
  exe.map(_map, args)
