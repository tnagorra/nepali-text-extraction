#!/usr/bin/python3

import sys
import os
import re
import json
from bs4 import BeautifulSoup


def main():
    if len(sys.argv) < 2:
        print('Chunk directory must be provided.')
        return 1

    directory = sys.argv[1]

    files = [x for x in os.listdir(directory)][0: 10]
    paths = [os.path.join(directory, x) for x in sorted(files)]
    paths = [x for x in paths if os.path.isfile(x)]


    lst = []
    for path in paths:
        with open(path) as html_doc:
            html = BeautifulSoup(html_doc, 'html.parser')

            for div in html.find_all('div'):

                aes = div.find_all('a')
                if aes and aes[0]:
                    # print(aes[0].get_text())
                    continue

                spans = div.find_all('span')
                for span in spans:
                    style = span.attrs.get('style')
                    if 'font-size:18px' in style and 'Himalayabold' in style:
                        # print('Letter started', span.get_text())
                        pass
                    elif 'Wingdings' in style:
                        # print('Letter terminated')
                        pass
                    else:
                        font_family = re.findall(r"font-family: ?b?'(.+?)'", style)
                        font_size = re.findall(r"font-size: ?(.+?)px", style)
                        sanitized_text = re.sub(r"\s+", " ", span.get_text())
                        lst.append({
                            'text': sanitized_text,
                            'font': font_family[0] if len(font_family) > 0 else None,
                            'size': font_size[0] if len(font_size) > 0 else None,
                        })

    print(json.dumps(lst))

if __name__ == '__main__':
    main()
