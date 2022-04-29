import re
from glob import glob


# 文中のURLの数を数える
def url_num_finder(pattern: str, url: str):
    result = re.findall(pattern, url)
    return len(result)


# 文中のURL意外の文字数を数える
# https://developer.twitter.com/en/docs/counting-characters
def character_count(pattern: str, url: str):
    result = "".join(re.split(pattern, url))
    # 日本語は2でカウントされるのでSHIFT-JISに変換後len()で文字数をカウントする
    return len(result.encode("SHIFT-JIS"))


class postCharacterCheck:
    def __init__(self, file: str):
        url = open(file, "r", encoding="UTF-8").read()
        PATTERN = r"https?://[\w\(-.!*'()/~:?#=%&@;+$,)]+"
        url_count = url_num_finder(PATTERN, url)
        post_sentence_length = character_count(PATTERN, url)
        total_length = url_count * 23 + post_sentence_length
        if total_length > 280:
            raise ValueError(f"This may violate Twitter's character limit.⇒ {file}")


# tweet_textディレクトリ内のテキストファイルのテキストを取得する
def get_texts():
    texts = []
    for i in glob("tweet_text/*.txt"):
        text = open(i, "r", encoding="UTF-8").read()
        texts.append(text)
    return texts


def main():
    for file in glob("tweet_text/*.txt"):
        postCharacterCheck(file)
    print("Good! Text length is not a problem.")


if __name__ == "__main__":
    main()
