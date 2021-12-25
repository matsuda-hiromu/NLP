def doc2wvs(corpus):
    # コーパスを適当に分かち書きにし、一つの配列に入れる
               #text1              #text2
    wvs = [["word1","word2"],["word3","word4"]]
    return wvs
    


def wvs2corpus(wvs):
  # 辞書作成
  dictionary = corpora.Dictionary(wvs)
  dictionary.filter_extremes(no_below=0.0, no_above=0.8)
  dictionary.save_as_text('topic/{}dict.txt'.format(topic_N))
  # コーパスを作成
  corpus = [dictionary.doc2bow(text) for text in wvs]
  corpora.MmCorpus.serialize('topic/{}cop.mm'.format(topic_N), corpus)



def lda_topic(top_N,topic_N ):
  #学習
  dictionary = corpora.Dictionary.load_from_text('topic/{}dict.txt'.format(topic_N))
  corpus = corpora.MmCorpus('topic/{}cop.mm'.format(topic_N))
  lda = models.LdaMulticore(corpus=corpus,workers=4, num_topics=topic_N, id2word=dictionary)  
  # 結果出力

  for i in range(topic_N):
    topic_words = [topic[0] for topic in lda.show_topic(i,topn = top_N)]
    print(topic_words)



#パラメータ設定
top_N   = 5
topic_N = 3
outcsv = open("topic/Topic{}.csv".format(topic_N),"w")
writer = csv.writer(outcsv)
corpus = pickle.load( open('./{}.pkl'.format(fname), 'rb') )


#トピック数以下のコーパスしかない場合はやめる
wvs = doc2wvs(corpus)
if len(wvs) < topic_N:
    print("failed",ids,failed_num)
    break
wvs2corpus(wvs)
lda_topic(top_N,topic_N)
