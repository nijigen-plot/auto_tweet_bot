import re
from glob import glob


# 文中のURLの数を数える
def url_num_finder(url: str):
    PATTERN = "https?://[\w\(-.!*'\(\)/~:?#=%&@;\+$,)]+"
    result = re.findall(PATTERN, url)
    return len(result)


def main():


if __name__ == "__main__":
    main()
