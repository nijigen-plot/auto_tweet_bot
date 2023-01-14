import random
from glob import glob


# text展開してからランダムで選択してる。
# 後でランダムで配列を決定してからそれに該当するテキストだけを抽出するようにしたい
def choice():
    texts = []
    for i in glob("tweet_text/*.txt"):
        text = open(i, "r", encoding="UTF-8").read()
        texts.append(text)
    choice_text = random.choice(texts)
    return choice_text
