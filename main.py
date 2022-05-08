from post_text import choice
from twitter_bot import Twitter


def main():
    target_text = choice()
    t = Twitter()
    # 以下を有効化することでポストされる
    t.tweet(target_text)
    # 以下を有効化することで実行できるかテストできる
    # t.check(target_text)


if __name__ == "__main__":
    main()
