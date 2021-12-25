# 念のため性能を測る
import sys
import random
f  = open('predict.dat')
s = open("predict_only1.dat","a")   
for line in f:
  if line[0:1] == "1" :
    s.write(line)
   
    