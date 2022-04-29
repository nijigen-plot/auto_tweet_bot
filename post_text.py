import random
from glob import glob


def choice():
    texts = []
    for i in glob("tweet_text/*.txt"):
        text = open(i, "r", encoding="UTF-8").read()
        texts.append(text)
    choice_text = random.choice(texts)
    return choice_text
