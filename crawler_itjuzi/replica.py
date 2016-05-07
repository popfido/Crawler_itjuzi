import codecs

rep = set()

with codecs.open('url_loaded.csv', mode='r', encoding='utf-8') as f:
    for line in f:
        rep.add(line.strip())