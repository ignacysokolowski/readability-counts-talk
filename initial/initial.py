#!/usr/bin/env python
import sys
import json


def get_first_initial_bad(file_path):
    return json.loads(open(file_path).read())[0]['title'][0].upper()


def get_first_initial_good(file_path):
    with open(file_path) as f:
        json_content = f.read()
    articles = json.loads(json_content)
    first_article = articles[0]
    title = first_article['title']
    first_letter = title[0]
    initial = first_letter.upper()
    return initial


def main(args=sys.argv):
    file_path = sys.argv[1]
    good = sys.argv[2] == 'good'
    if good:
        get_first_initial_good(file_path)
    else:
        get_first_initial_bad(file_path)


if __name__ == '__main__':
    main()
