from gensim.models import KeyedVectors
import json
import sys
import pickle
def pred():
  model = pickle.loads(open('fasttext.gensim-model_word.pkl', 'rb').read())
  while True:
    words = input().split()
    positive = list(filter(lambda x:x[0]!="-", words))
    negative = list(map(lambda x:x.replace("-", ""), filter(lambda x:x[0]=="-", words)) )
    try:
      scores = model.most_similar(positive=positive, negative=negative)
      print( json.dumps(scores, ensure_ascii=False, indent=2) )
    except KeyError as e:
      print( "指定したキーが存在しませんでした" )


def convert_fasttext2gensim():
  model = KeyedVectors.load_word2vec_format('model_word.vec', binary=False)
  open('fasttext.gensim-model_word.pkl', 'wb').write(pickle.dumps(model) )
  
if __name__ == '__main__':
  if '--convert' in sys.argv:
    convert_fasttext2gensim()
  if '--pred' in sys.argv:
    pred()
