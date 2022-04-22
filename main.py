from twitter_bot import Twitter


def main():
    t = Twitter()
    t.tweet(
        """HPシンプルで気に入ってる
https://quark-hardcore.com/"""
    )


if __name__ == "__main__":
    main()
