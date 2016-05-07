import codecs

import codecs

rep = set()

with codecs.open('url_loaded.csv', mode='r', encoding='utf-8') as f:
    counter = 0
    for line in f:
        counter += 1
        if line.strip() in rep:
            print counter, line
        rep.add(line.strip())
print len(rep)