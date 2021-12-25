# 念のため性能を測る
import sys
import random

def split():
  f  = open('svm2.dat')
  s1 = open("train2.dat","a")
  s2 = open("predict2.dat","a")
  for line in f:
    if 0.2 < random.random():
      s1.write(line)
    else:
      s2.write(line)

def dat1():
  s2  = open('predict2.dat')
  s3 = open("predict2_only1.dat","a")
  for line in s2:
    if line[0:1] == "1":
      s3.write(line)

split()
dat1()
