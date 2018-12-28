import sys
from collections import Counter

from byakaran.regex import boundary_re


def _load_data(filename):
    # filename = './data/news'
    with open(filename, encoding='utf-8') as in_file:
        return in_file.read()


def _alpha(x):
    return x[0]


def main():
    if len(sys.argv) < 2:
        print('File name must be provided.')
        return 1

    text = _load_data(sys.argv[1])
    boundaries = [x for x in boundary_re.findall(text)]

    bag_of_words = Counter(boundaries)
    for word, count in sorted(bag_of_words.most_common(), key=_alpha):
        print(word, count)


if __name__ == '__main__':
    main()
