import sys
from collections import Counter

from byakaran.regex import not_word_re, word_re


def _load_data(filename):
    with open(filename, encoding='utf-8') as in_file:
        return in_file.read()


def _lamo(x):
    return (-x[1], x[0])


def main():
    if len(sys.argv) < 2:
        print('File name must be provided.')
        return 1

    total_words = 0
    total_bad_words = 0

    text = _load_data(sys.argv[1])
    words = not_word_re.split(text)

    bag_of_words = Counter(words)
    for word, count in sorted(bag_of_words.most_common(), key=_lamo):
        if not word_re.match(word):
            print(word, count)
            total_bad_words += count
        total_words += count

    print('Percent of bad words', total_bad_words / total_words * 100)


if __name__ == '__main__':
    main()
