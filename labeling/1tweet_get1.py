import re
import json
import MeCab
from requests_oauthlib import OAuth1Session

CK = "（用意したConsumer Keyを入力）"
CS = "（用意したConsumer Secretを入力）"
AT = "（用意したAccess Tokenを入力）"
AS = "（用意したAccess Token Secretを入力）"

API_URL = "https://api.twitter.com/1.1/search/tweets.json?tweet_mode=extended"
KEYWORD = "芸能 OR アニメ OR 漫画 OR TV OR ゲーム"            #エンタメ系のキーワードを入力
CLASS_LABEL = "__label__1"

def main():
    tweets = get_tweet()                #ツイートを取得
    surfaces = get_surfaces(tweets)     #ツイートを分かち書き
    write_txt(surfaces)                 #ツイートを書き込み

def get_tweet():
    """
    TwitterからKEYWORDに関連するツイートを取得
    """
    params = {'q' : KEYWORD, 'count' : 100}
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.get(API_URL, params = params)
    results = []
    if req.status_code == 200:
        # JSONをパース
        tweets = json.loads(req.text)
        for tweet in tweets['statuses']:
            results.append(tweet['full_text'])
        return results
    else:
        # エラー
        print ("Error: %d" % req.status_code)

def get_surfaces(contents):
    """
    文書を分かち書きし単語単位に分割
    """
    results = []
    for row in contents:
        content = format_text(row)
        tagger = MeCab.Tagger('')
        tagger.parse('')
        surf = []
        node = tagger.parseToNode(content)
        while node:
            surf.append(node.surface)
            node = node.next
        results.append(surf)
    return results

def write_txt(contents):
    """
    評価モデル用のテキストファイルを作成する
    """
    try:
        if(len(contents) > 0):
            fileNema = CLASS_LABEL + ".txt"
            labelText = CLASS_LABEL + ", "

            f = open(fileNema, 'a')
            for row in contents:
                # 空行区切りの文字列に変換
                spaceTokens = " ".join(row);
                result = labelText + spaceTokens + "\n"
                # 書き込み
                f.write(result)
            f.close()

        print(str(len(contents))+"行を書き込み")

    except Exception as e:
        print("テキストへの書き込みに失敗")
        print(e)

def format_text(text):
    '''
    ツイートから不要な情報を削除
    '''
    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub(r'@[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub(r'&[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub(';', "", text)
    text=re.sub('RT', "", text)
    text=re.sub('\n', " ", text)
    return text

if __name__ == '__main__':
    main()
