import os
import time
for i in range(300):
  os.system("python3 tweet_get1.py")
  time.sleep(30)
  os.system("python3 tweet_get2.py")
  time.sleep(30)
os.system("cat __label__1.txt __label__2.txt" > train.txt)
