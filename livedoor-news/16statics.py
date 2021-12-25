import os
import json
import sys
import json
import glob
import gzip
import datetime


def tag():
  names = glob.glob('./wakachi/*/*')
  imax  = len(names)
  tag_val = {}
  for i,name in enumerate(names):
    print(i,imax,name)
    with gzip.open(name, "rt") as f:
      text = f.read() 
      html = json.loads(text)
    for tag in html["tag"]:
      if tag_val.get(tag) is None:
        tag_val[tag] = 0
      tag_val[tag] += 1
  print("saving")
  #sys.exit()
  with open('tag.csv','w') as f:
    for tag,val in sorted(tag_val.items(), key=lambda x:x[1]):
      f.write("{tag},{val}\n".format(tag=tag,val=val))


def day():
  names = glob.glob('./wakachi/*/*')
  imax  = len(names)
  day_val = {}
  for i,name in enumerate(names):
    print(i,imax,name)
    with gzip.open(name, "rt") as f:
      text = f.read() 
      html = json.loads(text)
    try:
      dtime = datetime.datetime.strptime(html['time'], "%Y年%m月%d日 %H時%M分") # 2017年12月26日 15時51分
      day = dtime.strftime("%Y-%m-%d")
    
      if day_val.get(day) is None:
        day_val[day] = 0
      day_val[day] += 1
    except:
      pass     
  print("saving")
  with open('day.csv','w') as f:
    for day, val in sorted(day_val.items(), key=lambda x:x[0]):
      f.write("{day},{val}\n".format(day=day,val=val))


def tag_day():
  names = glob.glob('./wakachi/*/*')
  imax  = len(names)
  day_val = {}
  for i,name in enumerate(names):
    #print(i,imax,name)
    with gzip.open(name, "rt") as f:
      text = f.read() 
      html = json.loads(text)
    if "国内の事件・事故" in html["tag"] or "海外の事件・事故" in html["tag"]:
      print(i,imax,html["titles"])
      try:
        dtime = datetime.datetime.strptime(html['time'], "%Y年%m月%d日 %H時%M分") # 2017年12月26日 15時51分
        day = dtime.strftime("%Y-%m-%d")
        if day_val.get(day) is None:
          day_val[day] = 0 
        day_val[day] += 1
      except:
        pass    
  print("saving")
  with open('tag_day.csv','w') as f:
    for day, num in sorted(tag_val.items(), key=lambda x:x[0]):
      f.write("{day},{val}\n".format(day=day,val=val))




if "--tag" in sys.argv:
  tag()
if "--day" in sys.argv:
  day()
if "--tag_day" in sys.argv:
  tag_day()
